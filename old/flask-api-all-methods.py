from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" to store example items
items = [{"id": 1, "name": "Akash Singh"}]

@app.route('/api/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'GET':
        # Return the list of items
        return jsonify({"items": items}), 200
    
    if request.method == 'POST':
        # Add a new item to the list
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input. 'name' field is required."}), 400
        new_item = {"id": len(items) + 1, "name": data['name']}
        items.append(new_item)
        return jsonify({"message": "Item added successfully.", "item": new_item}), 201


@app.route('/api/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_single_item(item_id):
    # Find the item by ID
    item = next((item for item in items if item["id"] == item_id), None)
    
    if not item:
        return jsonify({"error": "Item not found."}), 404

    if request.method == 'GET':
        # Return the single item
        return jsonify({"item": item}), 200

    if request.method == 'PUT':
        # Update the item's name
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input. 'name' field is required."}), 400
        item['name'] = data['name']
        return jsonify({"message": "Item updated successfully.", "item": item}), 200

    if request.method == 'DELETE':
        # Remove the item from the list
        items.remove(item)
        return jsonify({"message": "Item deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
