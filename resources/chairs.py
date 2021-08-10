from flask_restful import Resource, reqparse
from models.ChairModel import ChairModel
from cache import cache


class Chair(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('row',
                        type=str,
                        required=True,
                        help="Pleas insert row"
                        )
    parser.add_argument('chair_num',
                        type=str,
                        required=True,
                        help="Pleas insert chair number"
                        )

    def get(self):
        return {'chairs': [chair.json() for chair in ChairModel.find_available() if cache.get(str(chair.id)) is None]}

    def post(self):
        data = Chair.parser.parse_args()

        if ChairModel.find_by_row_and_num(data['row'], data['chair_num']):
            return {'message': "Chair already exist"}, 400

        chair = ChairModel(data['row'], data['chair_num'])
        try:
            chair.save_to_db()
        except:
            return {"message": "Error inserting item"}, 500

        return chair.json(), 201