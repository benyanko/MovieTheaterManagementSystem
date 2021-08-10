from flask_restful import Api
from setup import *
from db import db
from cache import cache
from resources.routes import register_routes


api = Api(app)
register_routes(api)
db.init_app(app)
cache.init_app(app)


if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0")

