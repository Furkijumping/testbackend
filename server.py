from flask import Flask, request, jsonify

app = Flask(__name__)

# Basit veritabanı simülasyonu
users = []


@app.route("/")
def home():
    return "Backend API Çalışıyor!"


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "Kullanıcı eklendi!", "user": data}), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if 0 <= user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({"error": "Kullanıcı bulunamadı!"}), 404


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if 0 <= user_id < len(users):
        data = request.get_json()
        users[user_id] = data
        return jsonify({"message": "Kullanıcı güncellendi!", "user": data})
    return jsonify({"error": "Kullanıcı bulunamadı!"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if 0 <= user_id < len(users):
        deleted_user = users.pop(user_id)
        return jsonify({"message": "Kullanıcı silindi!", "user": deleted_user})
    return jsonify({"error": "Kullanıcı bulunamadı!"}), 404


if __name__ == "__main__":
    app.run(debug=True)
