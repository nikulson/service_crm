from src import app
from src import views


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True,
        load_dotenv=False
    )
