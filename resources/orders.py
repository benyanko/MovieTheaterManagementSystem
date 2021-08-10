from flask_restful import Resource, reqparse
from models.ChairModel import ChairModel
from cache import cache
import uuid


class Order(Resource):

    def get(self):
        return {'chairs': [chair.json() for chair in ChairModel.find_ordered()]}

    def post(self, _id):
        chair = ChairModel.find_available_by_id(_id)
        if chair:
            confirmation_id = str(uuid.uuid4())
            # add - Works like set() but does not overwrite the values of already existing keys (False for already existing keys).
            if cache.add(str(_id), confirmation_id, timeout=(5 * 60)):
                chair.status = 'In Order'
                return {'message': 'order must complete in the next 5 minutes',
                        'chair': chair.json(),
                        'confirmation_id': confirmation_id}
            else:
                return {'message': 'chair not available'}, 404
        else:
            return {'message': 'chair not found'}, 404


class PayOrder(Resource):

    def post(self, _id, confirmation_id):
        value = cache.get(str(_id))
        if confirmation_id == str(value):
            chair = ChairModel.find_available_by_id(_id)
            if chair is None:
                return {'message': 'chair not found'}, 404
            else:
                if chair.confirmation_id == None:
                    chair.status = 'Ordered'
                    chair.confirmation_id = confirmation_id
                    chair.save_to_db()
                    return {'message': 'order completed',
                            'chair': chair.json(),
                            'confirmation_id': confirmation_id}
                else: return {'message': 'chair not available'}, 404

        else:
            return {'message': 'wrong confirmation id'}, 404

    def put(self, _id, confirmation_id):
        chair = ChairModel.find_by_confirmation_id(confirmation_id)
        if chair is None:
            return {'message': 'chair not found'}, 404
        else:
            chair.status = 'Available'
            chair.confirmation_id = None
        chair.save_to_db()

        return {'message': 'order canceled',
                'chair': chair.json()}
