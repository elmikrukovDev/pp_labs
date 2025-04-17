import unittest
import json
import copy
from mod2 import task7

class TestAddFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = task7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def test_add_expense_valid(self):
        response = self.app.post('/add/20230101/200')
        self.assertEqual(response.status_code, 201)
        self.assertIn(task7.EXPENSE_ADD_SUCCESS.encode('utf-8'), response.data)

    def test_add_expense_increases_total(self):
        self.app.post('/add/20230101/200')
        response = self.app.get('/calculate/2023/1')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 1200)

    def test_add_invalid_date_format(self):
        response = self.app.post('/add/2023-01-01/200')
        self.assertIn(task7.INVALID_DATE_FORMAT.encode('utf-8'), response.data)

class TestYearFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = task7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def test_calculate_year_valid(self):
        response = self.app.get('/calculate/2023')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 1500)

    def test_calculate_year_no_data(self):
        temp_storage = copy.deepcopy(self.app.application.storage)
        self.app.application.storage.clear()
        response = self.app.get('/calculate/2023')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)
        self.app.application.storage = temp_storage

    def test_calculate_year_nonexistent(self):
        response = self.app.get('/calculate/2024')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)

class TestMonthFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = task7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def test_calculate_month_valid(self):
        response = self.app.get('/calculate/2023/2')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 500)

    def test_calculate_month_no_data(self):
        temp_storage = copy.deepcopy(self.app.application.storage)
        self.app.application.storage.clear()
        response = self.app.get('/calculate/2023/1')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)
        self.app.application.storage = temp_storage

    def test_calculate_month_nonexistent(self):
        response = self.app.get('/calculate/2023/3')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)

if __name__ == '__main__':
    unittest.main()