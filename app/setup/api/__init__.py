from flask_restx import Api

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask project",
    doc="/docs",
    security="Bearer"
)
