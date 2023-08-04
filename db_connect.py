import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
cnx = None  # Here we initialize the cnx variable

try:
    cnx = mysql.connector.connect(user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'),
                                  host=os.environ.get('MYSQL_HOST'),
                                  database=os.environ.get('MYSQL_DB'))

    print("Database connection successful")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
finally:
    if cnx:  # Now, even if the connection fails, cnx is defined and this line won't raise an error
        cnx.close()
