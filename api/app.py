from flask import Flask, request, jsonify
import base64
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/base64', methods=['POST'])
def convert_base64():
    args = request.json
    url = args.get('url')
    if url:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            data = rsp.content
            return jsonify({"data": base64.b64encode(data).decode(), "msg": "success"})
        else:
            return jsonify({"data": "network failed", "msg": "fail"})

    else:
        return jsonify({"data": "invalid url", "msg": "fail"})


if __name__ == '__main__':
    app.run()
