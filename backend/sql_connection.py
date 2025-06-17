import datetime
import pymysql

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = pymysql.connect(user='root', password='root', database='gs')

  return __cnx
#Password set default // change to required when running.