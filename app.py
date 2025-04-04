from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to VPS Health Checker!"

@app.route('/ping')
def ping():
    return "pong", 200

@app.route('/health')
def health():
    # You can add more diagnostics here if needed
    status = {
        "status": "healthy",
        "message": "The VPS is running smoothly."
    }
    return jsonify(status), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
