from flask import Flask, request, send_file
from jsonrpcserver import method, dispatch, Success

app = Flask(__name__)


@method
def hello(name: str) -> str:
    return Success(f"Hello, {name}!")


@app.route("/jsonrpc", methods=["POST"])
def handle_jsonrpc():
    response = dispatch(request.get_data(as_text=True))
    return response, 200


@app.route("/postman_collection.json", methods=["GET"])
def get_postman_collection():
    try:
        return send_file("postman_collection.json")
    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/api.apib", methods=["GET"])
def get_apib():
    try:
        return send_file("api.apib")
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443)
