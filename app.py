from flask import Flask
from flask_restful import Api
from db import db
from cache import cache
from resources.routes import register_routes


app = Flask(__name__)
app.config.from_pyfile('setup/config.py')
api = Api(app)
register_routes(api)
db.init_app(app)
cache.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
