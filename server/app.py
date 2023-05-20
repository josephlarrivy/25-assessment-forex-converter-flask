from flask import Flask, request, jsonify
from flask_cors import CORS
from exchange_rate_api import ExchangeApiRequest

app = Flask(__name__)
CORS(app)

Exchange = ExchangeApiRequest('https://api.exchangerate.host')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    from_currency = data['from']
    to_currency = data['to']
    amount = data['amount']
    response = Exchange.exchange(from_currency, to_currency, amount)

    rounded = round(response['result'], 2)
    formatted_result = "{:,}".format(rounded)
    formatted_amount = "{:,}".format(response['query']['amount'])

    data = {
        'success' : True,
        'from' : response['query']['from'],
        'to' : response['query']['to'],
        'amount' : formatted_amount,
        'rate' : response['info']['rate'],
        'result' : formatted_result
        }
    return jsonify(data)


@app.route('/getSupportedCurrencies', methods=['GET'])
def get_supported_currencies():
    response = Exchange.get_supported_currencies()
    return jsonify({'data': response['symbols']})






if __name__ == '__main__':
    app.run(debug=True)