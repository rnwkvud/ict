from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')

mysql = MySQL(app)

class CreateCertificate(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        for item in json_data:
            term_name = item['용어 명']
            term_definition = item['용어 정의']

            cursor = mysql.connection.cursor()
            insert_query = """INSERT INTO shipping_terms (term_name, term_definition)
                              VALUES (%s, %s)"""
            cursor.execute(insert_query, (term_name, term_definition))
        mysql.connection.commit()
        cursor.close()

        return {'status': 'success'}, 201


api.add_resource(CreateCertificate, '/certificates')

if __name__ == '__main__':
    app.run(debug=True)



