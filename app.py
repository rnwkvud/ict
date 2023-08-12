from flask import Flask, request, jsonify, Response
from flask_mysqldb import MySQL
import json
import os

app = Flask(__name__)
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
mysql = MySQL(app)

@app.route('/webhook/shipterm/<string:term_name>', methods=['POST'])
def shipterm(term_name):
    cursor = mysql.connection.cursor()
    search_query = f"""SELECT term_definition FROM shipping_terms WHERE term_name = '{term_name}'"""
    cursor.execute(search_query)
    result = cursor.fetchone()
    cursor.close()
    if result:
        response_data = {"fulfillmentText": result[0]}
        response_json = json.dumps(response_data, ensure_ascii=False)
        return Response(response_json, content_type="application/json; charset=utf-8")
    else:
        return jsonify({'fulfillmentText': '해당 용어를 찾을 수 없습니다.'})

@app.route('/webhook/certification/<string:certificate_name>', methods=['POST'])
def certification(certificate_name):
    cursor = mysql.connection.cursor()
    search_query = f"""SELECT certificate_details FROM certificates WHERE certificate_name = '{certificate_name}'"""
    cursor.execute(search_query)
    result = cursor.fetchone()
    cursor.close()
    if result:
        response_data = {"fulfillmentText": result[0]}
        response_json = json.dumps(response_data, ensure_ascii=False)
        return Response(response_json, content_type="application/json; charset=utf-8")
    else:
        return jsonify({'fulfillmentText': '해당 자격증을 찾을 수 없습니다.'})

@app.route('/', methods=['GET'])
def test():
    return 'hello world444'

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)
