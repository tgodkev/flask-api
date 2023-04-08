from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    response = {"message": "Hello, Flask API!"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
