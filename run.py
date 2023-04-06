from app.config import Config
from app.server import create_app

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True)
