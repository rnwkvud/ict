import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
cnx = None  # Here we initialize the cnx variable

try:
    cnx = mysql.connector.connect(user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  host=os.environ.get('MYSQL_HOST'),
                                  database=os.environ.get('MYSQL_DB'), charset='utf8mb4')

    cursor = cnx.cursor()
    cursor.execute("SELECT term_definition FROM shipping_terms LIMIT 5")
    rows = cursor.fetchall()

    for row in rows:
        print(row[0])

except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
finally:
    if cnx:
        cnx.close()
