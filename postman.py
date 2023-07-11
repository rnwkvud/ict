from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'cM3STVa5PwqGUSe5ezSB'
app.config['MYSQL_DB'] = 'shipterm'
app.config['MYSQL_HOST'] = 'ictproject2.cfggn7y2q2g3.ap-northeast-2.rds.amazonaws.com'

mysql = MySQL(app)

class CreateTerm(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        term_name = json_data['용어 명'] # postman으로 json형식으로 넣을때 앞에 값
        term_definition = json_data['용어 정의']
        
        cursor = mysql.connection.cursor()
        insert_query = """INSERT INTO shipping_terms (term_name, term_definition)
                          VALUES (%s, %s)"""
        cursor.execute(insert_query, (term_name, term_definition))
        mysql.connection.commit()
        cursor.close()
        
        return {'status': 'success'}, 201

api.add_resource(CreateTerm, '/terms')

if __name__ == '__main__':
    app.run(debug=True)
