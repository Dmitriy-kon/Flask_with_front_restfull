import os


class Config(object):
    # app
    TESTING = True
    DEBUG = True
    SECRET_HERE = "asd@DASxz56k)(2asX[@!#$jsbT_IU34YBHp8&^%$xj2"
    PWD_HASH_SALT = b"a23sd3jxTY2nzxcrvgfgh^521gtHwuyu27"
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 15

    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}

    # db
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_ALGORITHM = 'HS256'
