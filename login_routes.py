from flask import Blueprint, jsonify, request, session

login = Blueprint("login", __name__)

users = []

@login.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        age = data.get("age")

        if not all([name, email, password, phone, age]):
            return jsonify({"error": "All fields are required"}), 400

        # ✅ Check if user already exists
        for u in users:
            if u["email"] == email:
                return jsonify({"error": "Email already registered"}), 400

        # ✅ Save new user
        user = {
            "name": name,
            "email": email,
            "password": password,  # (Later: hash it)
            "phone": phone,
            "age": age
        }
        users.append(user)

        return jsonify({"message": "Registration successful", "user": user}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    login.run(debug=True)  