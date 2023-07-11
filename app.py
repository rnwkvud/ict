from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'cM3STVa5PwqGUSe5ezSB'
app.config['MYSQL_DB'] = 'shipterm'
app.config['MYSQL_HOST'] = 'ictproject2.cfggn7y2q2g3.ap-northeast-2.rds.amazonaws.com'
mysql = MySQL(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    term_name = req.get('queryResult').get('parameters').get('term')  # "term" is the entity that we create in Dialogflow
    print(req)
    print(req.get('queryResult'), '-1번')
    print(req.get('queryResult').get('parameters'), '0번') 
    print(term_name, '1번')
    term_name = str(term_name[0].strip('[]')) 
    print(term_name, '2번')
    cursor = mysql.connection.cursor()
    search_query = f"""SELECT term_definition FROM shipping_terms WHERE term_name = '{term_name}'"""
    print(search_query)
    cursor.execute(search_query)
    result = cursor.fetchone()
    cursor.close()
    print(result)
    if result:
        return jsonify({
            'fulfillmentText': result[0],
        })
    else:
        return jsonify({
            'fulfillmentText': '해당 용어를 찾을 수 없습니다.',
        })
@app.route('/check', methods=['GET'])
def check():
    return jsonify({'message': 'Hello World'})

if __name__ == '__main__':
    app.run(debug=True)