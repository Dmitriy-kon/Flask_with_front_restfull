import base64
import hashlib
import hmac

from flask import current_app


class Security_hash:
    @staticmethod
    def __generate_password_bytes(password: str) -> bytes:
        return hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=current_app.config['PWD_HASH_SALT'],
            iterations=current_app.config['PWD_HASH_ITERATIONS']
        )

    def generate_password_hash(self, password):
        byte_password = self.__generate_password_bytes(password)
        return base64.b64encode(byte_password).decode('utf-8')

    def compare_password(self, password_hash: str, password_passed: str):
        # Декодируем в бинарный код
        decode_pass = base64.b64decode(password_hash.encode('utf-8'))

        # Кодируем полученный пароль от пользователя
        user_pass = base64.b64decode(self.generate_password_hash(password_passed))

        is_equal = hmac.compare_digest(decode_pass, user_pass)
        return is_equal
