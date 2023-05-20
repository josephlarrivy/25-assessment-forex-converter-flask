from flask import Flask, request
import unittest
import json
from exchange_rate_api import ExchangeApiRequest
from app import app



class AppFlaskTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.exchange = ExchangeApiRequest('https://api.exchangerate.host')

    def test_get_supported_currencies_route(self):
        response = self.app.get('/getSupportedCurrencies')
        self.assertEqual(response.status_code, 200)

    def test_convert_route(self):
        data = {
            'from': 'USD',
            'to': 'EUR',
            'amount': 100
        }
        response = self.app.post('/convert', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        returned = json.loads(response_data)
        # print('#####')
        # print(data)
        # print('#####')
        self.assertTrue(returned['success'])
        self.assertEqual(int(returned['amount']), data['amount'])