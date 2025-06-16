import datetime
import pymysql

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = pymysql.connect(user='root', password='Minon#616747', database='gs')

  return __cnx
