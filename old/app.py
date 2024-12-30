from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint
@app.route('/data', methods=['GET'])
def get_data():
    # Sample data to return
    data = {
        "message": "Hello from the Flask API!",
        "status": "success",
        "data": {
            "id": 1,
            "name": "Example"
        }
    }
    return jsonify(data), 200

# Example POST endpoint
@app.route('/data', methods=['POST'])
def post_data():
    if not request.json:
        return jsonify({"error": "No JSON data provided"}), 400
    
    user_data = request.json
    return jsonify({"message": "Data received", "data": user_data}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
