import mysql.connector

cnx = None  # Here we initialize the cnx variable

try:
    cnx = mysql.connector.connect(user='admin', password='cM3STVa5PwqGUSe5ezSB',
                                  host='ictproject2.cfggn7y2q2g3.ap-northeast-2.rds.amazonaws.com',
                                  database='shipterm')
    print("Database connection successful")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
finally:
    if cnx:  # Now, even if the connection fails, cnx is defined and this line won't raise an error
        cnx.close()
