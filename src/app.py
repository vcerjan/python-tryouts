from crypt import methods
from flask import Flask, jsonify, request
from random import randint
import psycopg2

conn = None

try:
  conn = psycopg2.connect("dbname='rolldb' user='flaskadmin' host='localhost' password='flaskadmin1'")
except:
  print("I am unable to connect to the database")

app = Flask(__name__)

@app.route('/')
def handle_root():
  return '<p>Hello World</p>'

@app.route('/data/<id>')
def handle_data(id):
  data = {
    'users': [
      {
        'id': id,
        'first_name': 'Vjeko',
        'last_name': 'Slav',
        'age': 24
      }
    ]
  }
  return jsonify(data)

@app.route('/roll', methods=['POST'])
def handle_roll():
  data = request.get_json()
  total = 0
  rollResults = []

  diceSides = data['diceSides']
  numberOfRolls = data['numberOfRolls']

  for _ in range(numberOfRolls):
    roll = randint(1, diceSides)
    rollResults.append(roll)
    total += roll

  response = {
    'query': str(numberOfRolls) + 'd' + str(diceSides),
    'rollResults': rollResults,
    'total': total
  }

  return jsonify(response)


@app.route('/stuff', methods=['GET'])
def handle_stuff():
  cur = conn.cursor()
  
  cur.execute('select * from stuff;')
  result = cur.fetchall()
  
  return jsonify(result)