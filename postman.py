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
            certificate_name = item['자격증']
            certificate_details = item['자격증 내용']

            cursor = mysql.connection.cursor()
            insert_query = """INSERT INTO certificates (certificate_name, certificate_details)
                              VALUES (%s, %s)"""
            cursor.execute(insert_query, (certificate_name, certificate_details))
        mysql.connection.commit()
        cursor.close()

        return {'status': 'success'}, 201


api.add_resource(CreateCertificate, '/certificates')

if __name__ == '__main__':
    app.run(debug=True)



