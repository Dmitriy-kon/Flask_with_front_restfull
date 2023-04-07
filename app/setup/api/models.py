from flask_restx import Model, fields

from app.setup.api import api

genre: Model = api.model("Жанр", {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Хоррор')
})

director: Model = api.model("Режисер", {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Таронтино')
})

movie: Model = api.model("Фильм", {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, example="Монстр в Париже"),
    'description': fields.String(required=True, example="Париж. 1910 год. Ужасный монстр."),
    'trailer': fields.String(required=False, example="Монстр в Париже"),
    'year': fields.Integer(required=True, example=1920),
    'rating': fields.Float(required=True, example=8.2),

    'genre': fields.String(required=True, example="Хоррор"),
    'director': fields.String(required=True, example="Тарантино")
})

user: Model = api.model("Пользователь", {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, example="somemail@gmail.com", unique=True),
    'password': fields.String(required=True, example="Hash"),
    'name': fields.String(required=False, example="Artem"),
    'surname': fields.String(required=False, example="Denisov Artem"),
})
