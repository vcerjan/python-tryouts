from flask import Flask, jsonify, request
from random import randint

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

@app.route('/roll', methods=['GET', 'POST'])
def handle_roll():
  if request.method == 'POST':
    data = request.get_json()
    total = 0
    rollResults = []

    diceSides = data['diceSides']
    numberOfRolls = data['numberOfRolls']

    for x in range(numberOfRolls):
      roll = randint(1, diceSides)
      rollResults.append(roll)
      total += roll

    response = {
      'query': str(numberOfRolls) + 'd' + str(diceSides),
      'rollResults': rollResults,
      'total': total
    }

    return jsonify(response)
  if request.method == 'GET':
    return '<p>Roll a dice (UI is WIP)</p>'
