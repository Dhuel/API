#!flask/bin/python
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
tasks = []


@app.route('/API/Get_last_values', methods=['GET'])
def get_records():
    conn = sqlite3.connect('../Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    for row in cursor:
        tasks.append({'Last Price':row[3]})
    conn.close()
    return jsonify({'Last price BTC_USD': tasks})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
