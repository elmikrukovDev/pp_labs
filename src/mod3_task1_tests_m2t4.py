import unittest
from freezegun import freeze_time
from mod2 import task4

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = task4.app.test_client()
        self.app.testing = True

    @freeze_time("2025-03-31")
    def test_can_get_correct_username_with_weekdate_on_monday(self):
        response = self.app.get('/hello_world/Daniel')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Daniel. Хорошего понедельника!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-01")
    def test_can_get_correct_username_with_weekdate_on_tuesday(self):
        response = self.app.get('/hello_world/Хорошего вторника')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего вторника. Хорошего вторника!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-02")
    def test_can_get_correct_username_with_weekdate_on_wednesday(self):
        response = self.app.get('/hello_world/Хорошей среды')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей среды. Хорошей среды!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-03")
    def test_can_get_correct_username_with_weekdate_on_thursday(self):
        response = self.app.get('/hello_world/Хорошего четверга')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего четверга. Хорошего четверга!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-04")
    def test_can_get_correct_username_with_weekdate(self):
        response = self.app.get('/hello_world/Саша')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Саша. Хорошей пятницы!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-05")
    def test_can_get_correct_username_with_weekdate_on_saturday(self):
        response = self.app.get('/hello_world/Хорошей субботы')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей субботы. Хорошей субботы!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-06")
    def test_can_get_correct_username_with_weekdate_on_sunday(self):
        response = self.app.get('/hello_world/Хорошего воскресенья')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего воскресенья. Хорошего воскресенья!'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()