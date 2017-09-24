!flask/bin/python
from flask import Flask, jsonify
import sqlite3, time, datetime

app = Flask(__name__)


@app.route('/API/V1.1/Get/LastValues', methods=['GET'])
def get_last_values():
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    for row in cursor:
        tasks.append({'Last Price': row[3]})
        tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
    conn.close()
    return jsonify({'Last price BTC_USD': tasks})


@app.route('/API/V1.1/Get/HighValues', methods=['GET'])
def get_high_values():
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    for row in cursor:
        tasks.append({'High': row[5]})
        tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
    conn.close()
    return jsonify({'Highs BTC_USD': tasks})


@app.route('/API/V1.1/Get/LastValuesByHour', methods=['GET'])
def get_last_values_hour():
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    hour_counter = 0
    for row in cursor:
        if hour_counter == 0:
            tasks.append({'Last Price': row[3]})
            tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
            hour_counter = hour_counter + 1
        else:
            hour_counter = hour_counter + 1
            if hour_counter == 60:
                hour_counter = 0
    conn.close()
    return jsonify({'Last values by hour BTC_USD': tasks})


@app.route('/API/V1.1/Get/LastValuesByDay', methods=['GET'])
def get_last_values_day():
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    hour_counter = 0
    for row in cursor:
        if hour_counter == 0:
            tasks.append({'Last Price': row[3]})
            tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
            hour_counter = hour_counter + 1
        else:
            hour_counter = hour_counter + 1
            if hour_counter == 1440:
                hour_counter = 0
    conn.close()
    return jsonify({'Last values by day BTC_USD': tasks})


@app.route('/API/V1.1/Get/LastValuesByWeek', methods=['GET'])
def get_last_values_week():
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    hour_counter = 0
    for row in cursor:
        if hour_counter == 0:
            tasks.append({'Last Price': row[3]})
            tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
            hour_counter = hour_counter + 1
        else:
            hour_counter = hour_counter + 1
            if hour_counter == 10080:
                hour_counter = 0
    conn.close()
    return jsonify({'Last values by week BTC_USD': tasks})


@app.route('/API/V1.1/Get/LastValuesWithin/<string:start_date>/<string:end_date>', methods=['GET'])
def get_last_values_start_end(start_date, end_date):
    tasks = []
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    for row in cursor:
        start = start_date.split('-')
        end = end_date.split('-')
        epoch_start_date = (datetime.datetime(int(start[0]), int(start[1]), int(start[2]),
                                             int(start[3]), int(start[4]), int(start[5])) -
                                             datetime.datetime(1970, 1, 1)).total_seconds()
        epoch_end_date = (datetime.datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]),
                                           int(end[4]), int(end[5])) - datetime.datetime(1970, 1, 1)
                                           ).total_seconds()
        if float(row[7]) >= epoch_start_date & float(row[7]) <= epoch_end_date:
            tasks.append({'Last Price': row[3]})
            tasks.append({'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[7])))})
    conn.close()
    return jsonify({'Last values within date range ': tasks})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
