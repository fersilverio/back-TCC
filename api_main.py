from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from rede_bayesiana import get_prediction

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/', methods=['GET','POST'])
@cross_origin()
def func():
    if request.method == 'POST':
        req = request.get_json()
        prob_final = get_prediction(req)
        return jsonify({'probabilidade': prob_final})

if __name__ == '__main__':
    app.run(debug=True)