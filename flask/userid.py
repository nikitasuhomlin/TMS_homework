from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/id', methods = ['GET', 'POST', 'PATCH'])
def id():
    if request.method == "GET":
        return jsonify({"user_id": "user"})
    elif request.method == "POST":
        req_Json = request.json
        user_id = req_Json['user_id']
        return jsonify({"user": "Hi " + user_id})

if __name__ == '__main__':
    app.run(debug=True, port=9090)

    
