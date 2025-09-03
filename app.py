from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Gym Management System"

@app.route('/members')
def get_members():
    members = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(members)

if __name__ == "__main__":
    app.run(debug=True)
