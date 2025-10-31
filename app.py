from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ Correct CORS setup
CORS(app, origins=["https://realtimeproject-frontend.vercel.app/"], supports_credentials=True)

from frontend_process.login_routes import login
app.register_blueprint(login, url_prefix='/login')

if __name__ == '__main__':
    app.run(debug=True)
