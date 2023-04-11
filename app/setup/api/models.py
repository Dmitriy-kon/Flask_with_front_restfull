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
    'favorite_genre': fields.Integer(required=False, example=3)
})

auth: Model = api.model("Регистрация", {
    'email': fields.String(required=True, example="somemail@gmail.com"),
    'password': fields.String(required=True, example="sjY65TBG2=71")
})

tokens_model = api.model('Tokens', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True)
})

passwords = api.model('Смена пароля', {
    'old_password': fields.String(example="my_password"),
    'new_password': fields.String(example='my_new_password')
})
