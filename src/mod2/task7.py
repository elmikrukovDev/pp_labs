from flask import Flask, jsonify, request
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)

storage = defaultdict(lambda: defaultdict(int))


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    if number < 0:
        return jsonify({"error": "Expense must be a non-negative integer."}), 400

    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        datetime(year, month, day)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYYMMDD."}), 400

    storage[year][month] += number
    return jsonify({"message": "Expensive added successfully"}), 201


@app.route('/calculate/<int:year>')
def calculate_year(year):
    total_expense = sum(storage[year].values())
    return jsonify({"year": year, "total_expense": total_expense}), 200


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total_expense = storage[year].get(month, 0)
    return jsonify({"year": year, "month": month, "total_expense": total_expense}), 200


if __name__ == "__main__":
    app.run(debug=True)