from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
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

@app.route('/', methods=['GET'])
def test():
    return 'hello world'

if __name__ == '__main__':
    app.run(port=80)