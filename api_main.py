from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from rede_bayesiana import *

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def func():
    req = request.get_json()
    req_tratada = req['entrada']
    string_entrada = req_tratada
    prob_final = get_prediction(string_entrada)
    return jsonify({'probabilidade': prob_final})

if __name__ == '__main__':
    app.run(debug=True)
