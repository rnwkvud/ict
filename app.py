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
    print(req, '0번--------')
    intent_name = req.get('queryResult').get('intent').get('displayName')
    print(req.get('queryResult'), '-1번')
    print(req.get('queryResult').get('intent'), '0번') 
    print(intent_name, '1번-------')
    cursor = mysql.connection.cursor()
#         term_name = str(term_name[0].strip('[]'))

    if intent_name == 'shipterm':
        term_name = req.get('queryResult').get('parameters').get('term')
        term_name = str(term_name).strip('[]')
        print(term_name)
        search_query = f"""SELECT term_definition FROM shipping_terms WHERE term_name = '{term_name}'"""
        print(search_query)
        cursor.execute(search_query)
        result = cursor.fetchone()
        if result:
            return jsonify({'fulfillmentText': result[0]})
        else:
            return jsonify({'fulfillmentText': '해당 용어를 찾을 수 없습니다.'})

    elif intent_name == 'Certification':
        certificate_name = req.get('queryResult').get('parameters').get('Certification_Term')
        certificate_name = str(certificate_name).strip('[]')
        print(certificate_name)
        search_query = f"""SELECT certificate_details FROM certificates WHERE certificate_name = '{certificate_name}'"""
        print(search_query)
        cursor.execute(search_query)
        result = cursor.fetchone()
        if result:
            return jsonify({'fulfillmentText': result[0]})
        else:
            return jsonify({'fulfillmentText': '해당 자격증을 찾을 수 없습니다.'})

    cursor.close()

@app.route('/', methods=['GET'])
def test():
    return 'hello world444'

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)