from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "qwhdu&*UJdwqdqw"

@app.route('/test', methods=['POST'])
def testing_api():
    data = request.get_json()
    response = User.test(data)
    return response