from flask import Flask, request
from xmlrpc.server import SimpleXMLRPCDispatcher

app = Flask(__name__)
dispatcher = SimpleXMLRPCDispatcher(allow_none=True, encoding="utf-8")


@app.route("/xmlrpc", methods=["POST"])
def handle_xmlrpc():
    response = dispatcher._marshaled_dispatch(request.data)
    return response, 200, {"Content-Type": "text/xml"}


def hello(name):
    return f"Hello, {name}!"


dispatcher.register_function(hello, "hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
