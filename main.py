import utils
import urllib3
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json

urllib3.disable_warnings()

app = Flask(__name__)
CORS(app)

@app.route('/get_total_ifood', methods=['POST'])
def get_total_ifood():
    data = request.json
    if not data or 'token' not in data:
        return jsonify({"Error": "Token Bearer not provided"}), 400
    
    bearer_token = data['token']
    dados = utils.Data()
    dados.headers["authorization"] = f"Bearer {bearer_token}"
    res, status_code = dados.get_total_ifood()

    response = make_response(json.dumps(res, indent=4, ensure_ascii=False), status_code)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)