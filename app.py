# server.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add():
    data = request.get_json()
    print(data)
    with open('./data/test.json', 'w') as f:
    	json.dump(data, f, indent=4)
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)