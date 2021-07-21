from logging import error
from flask import Flask, json, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id' : 1,
        'title' : 'hi',
        'done' : False
    },
    
    {
        'id' : 2,
        'title' : 'cheese',
        'done' : False
    }
    
]

@app.route('/')

def hello():
    return 'hi'

@app.route('/add_data', methods = ['POST'])

def addTask():
    if not request.json:
        return jsonify({
            'status' : 'ERROR', 
            'message' : 'enter task'
        }, 420)
    task = {
        'id' : tasks[-1]['id'] + 1,
        'title' : request.json['title'],
        'done' : False
    }
    tasks.append(task)
    return jsonify({
        'status' : 'Completed',
        'message'  : 'Task added'
    })
    
@app.route('/get_data')

def getTask():
    return jsonify({
        'data' : tasks
    })

if(__name__ == '__main__'):
    app.run()