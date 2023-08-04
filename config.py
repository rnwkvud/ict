import os
from dotenv import load_dotenv

load_dotenv()

db_db = os.environ.get('MYSQL_DB')
db_host = os.environ.get('MYSQL_HOST')
db_user = os.environ.get('MYSQL_USER')
db_password = os.environ.get('MYSQL_PASSWORD')
print(db_db)
print(db_host)
print(db_password)
