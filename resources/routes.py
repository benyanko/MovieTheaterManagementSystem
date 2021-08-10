from flask_restful import Api
from resources.chairs import Chair
from resources.orders import Order, PayOrder
from resources.seeder import Seeder


def register_routes(api: Api):
    api.add_resource(Chair, "/chair")
    api.add_resource(Order, "/order", "/order/<int:_id>")
    api.add_resource(PayOrder, "/pay/<int:_id>/<string:confirmation_id>")
    api.add_resource(Seeder, "/seeder")
