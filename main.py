from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"received": data}), 200

if __name__ == '__main__':
    app.run(port=5000)