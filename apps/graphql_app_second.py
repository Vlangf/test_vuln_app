from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, world!")


schema = graphene.Schema(query=Query)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8089)
