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


@app.route("/api.raml", methods=["GET"])
def get_postman_collection():
    try:
        return send_file("api.raml")
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8880)
