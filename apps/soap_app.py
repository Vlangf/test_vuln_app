from flask import Flask
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

app = Flask(__name__)


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Unicode)
    def say_hello(ctx, name, times):
        return f"Hello, {name}!" * times


application = Application(
    [HelloWorldService],
    tns="spyne.examples.hello",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

wsgi_application = WsgiApplication(application)


@app.route("/soap", methods=["POST"])
def soap():
    return wsgi_application


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
