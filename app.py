from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Tobi", "age": 20},
    2: {"name": "Arun", "age": 25},
}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify({"message": "User added", "id": new_id}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id] = data
    return jsonify({"message": "User updated"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"})

app.run(debug=True)