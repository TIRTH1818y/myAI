from flask import Flask, jsonify, request
import speech


app = Flask(__name__)

data = " hello "

# def get_data():
#     return data
# Endpoint to fetch the string data
@app.route('/api/data', methods=['GET'])
def get_data():

    return jsonify({"message :::::": data})


# Endpoint to update the string data
@app.route('/api/data', methods=['POST'])
def post_data():
    global data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    new_message = request.json.get("message")
    if new_message:
        data = new_message
        response= speech.AI(data)

        return jsonify({"message":"Data updated successfully!","response":response}), 201
    return jsonify({"error": "Invalid data!"}), 400


if __name__ == '__main__':
    # Consider using app.run() only in development. Use a production server for production systems.
    app.run(host='0.0.0.0', port=5000)

