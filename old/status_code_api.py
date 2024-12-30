from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    """Respond with different HTTP status codes based on a query parameter."""
    status = request.args.get('status', default=200, type=int)
    messages = {
        200: {"message": "Success! Everything is OK."},
        404: {"message": "Resource not found."},
        500: {"message": "Internal server error. Something went wrong."},
        401: {"message": "Unauthorized. Please provide authentication."},
        403: {"message": "Forbidden. You don't have access to this resource."},
    }
    response = messages.get(status, {"message": "Custom status code returned."})
    return jsonify(response), status

if __name__ == '__main__':
    app.run(debug=True, port=5000)
