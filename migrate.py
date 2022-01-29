from ensurepip import bootstrap
import psycopg2

conn = None

try:
  conn = psycopg2.connect("dbname='rolldb' user='flaskadmin' host='localhost' password='flaskadmin1'")
except:
  print("I am unable to connect to the database")

with open("./migrations/bootstrap.sql") as file:
  sql = file.read()
  cur = conn.cursor()
  cur.execute(sql)
