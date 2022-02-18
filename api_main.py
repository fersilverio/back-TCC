from flask import Flask, jsonify, request
from flask_cors import CORS
from rede_bayesiana import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def func():
    string_entrada = request.get_json()
    prob_final = get_prediction(string_entrada['entrada'])
    return jsonify({'probabilidade': prob_final})


if __name__ == '__main__':
    app.run(debug=True)