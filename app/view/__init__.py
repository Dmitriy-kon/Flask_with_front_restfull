from .auth import auth_ns
from .director import directors_ns
from .favorites import favorite_ns
from .genre import genre_ns
from .movie import movies_ns
from .user import user_ns

__all__ = [
    "auth_ns",
    "directors_ns",
    "favorite_ns",
    "genre_ns",
    "movies_ns",
    "user_ns"
]
