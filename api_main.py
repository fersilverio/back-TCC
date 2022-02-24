from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from rede_bayesiana import *

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def func():
    string_entrada = request.get_json()
    prob_final = get_prediction(string_entrada)
    print(prob_final)
    return jsonify({'probabilidade': prob_final})

if __name__ == '__main__':
    app.run(debug=True)