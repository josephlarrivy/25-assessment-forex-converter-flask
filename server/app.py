from flask import Flask, request, jsonify
from flask_cors import CORS
from exchange_rate_api import ExchangeApiRequest


#      https://api.exchangerate.host
#      /convert?from=USD&to=EUR

app = Flask(__name__)
CORS(app)

# app.config["SECRET_KEY"] = "qwhdu&*UJdwqdqw"

Exchange = ExchangeApiRequest('https://api.exchangerate.host')


@app.route('/convert', methods=['POST'])
def testing_api():
    data = request.get_json()
    from_currency = data['from']
    to_currency = data['to']
    amount = data['amount']
    # print(from_currency)
    # print(to_currency)
    # print(amount)
    response = Exchange.exchange(from_currency, to_currency, amount)
    print(response)

    # print('###########')
    # print(response['success'])
    # print(response['query'])
    # print(response['query']['from'])
    # print(response['query']['to'])
    # print(response['query']['amount'])
    # print(response['info']['rate'])
    # print(response['result'])
    # print('###########')

    data = {
        'success' : True,
        'from' : response['query']['from'],
        'to' : response['query']['to'],
        'amount' : response['query']['amount'],
        'rate' : response['info']['rate'],
        'result' : response['result']
        }
    return jsonify(data)

    






if __name__ == '__main__':
    app.run(debug=True)