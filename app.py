from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")

def index():
    return "Hello DevOPs, Flask CI/CD"

@app.route("/healthz")
def healthz():
    return jsonify({"Status":"ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)