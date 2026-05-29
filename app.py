import flask
from flask import jsonify

app = flask.Flask(__name__)
@app.route('/')
def index():
    return jsonify(message="Hello CI/CD with Flask and Docker!")

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')