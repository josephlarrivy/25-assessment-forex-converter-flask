from flask import Flask, request, jsonify
from flask_cors import CORS
from exchange_rate_api import ExchangeApiRequest


#      https://api.exchangerate.host
#      /convert?from=USD&to=EUR

app = Flask(__name__)
CORS(app)

# app.config["SECRET_KEY"] = "qwhdu&*UJdwqdqw"

Exchange = ExchangeApiRequest('https://api.exchangerate.host')


@app.route('/test', methods=['POST'])
def testing_api():
    return jsonify({'data':'good request'})







if __name__ == '__main__':
    app.run(debug=True)