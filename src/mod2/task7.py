"""
Этот модуль содержит Flask приложение с endpoints

Для справки: был обработан скриптом mod3_task5_script.sh
"""

from collections import defaultdict
from datetime import datetime
from flask import Flask, jsonify

EXPENSE_ADD_SUCCESS = "Expense added successfully"
INVALID_DATE_FORMAT = "Invalid date format. Use YYYYMMDD."
NEGATIVE_INTEGER = "Expense must be a non-negative integer."
INVALID_KEY = "Invalid input data."

app = Flask(__name__)

app.storage = defaultdict(lambda: defaultdict(int))

@app.route('/add/<date>/<int:number>', methods=["POST"])
def add_expense(date, number):
    """
    Роут на добавление расхода
    """
    if number < 0:
        return jsonify({"error": NEGATIVE_INTEGER}), 400

    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        datetime(year, month, day)
    except ValueError:
        return jsonify({"error": INVALID_DATE_FORMAT}), 400

    app.storage[year][month] += number
    return jsonify({"message": EXPENSE_ADD_SUCCESS}), 201

@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    """
    Считает затраты за год
    """
    if year in app.storage:
        total_expense = sum(app.storage[year].values())
        return jsonify({"year": year, "total_expense": total_expense}), 200
    return jsonify({"year": year, "total_expense": 0}), 200

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    """
    Считает затраты за месяц
    """
    if year in app.storage:
        total_expense = app.storage[year].get(month, 0)
        return jsonify({"year": year, "month": month, "total_expense": total_expense}), 200
    return jsonify({"year": year, "month": month, "total_expense": 0}), 200

if __name__ == "__main__":
    app.run(debug=True)
