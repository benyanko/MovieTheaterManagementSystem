from models.ChairModel import ChairModel
from flask_restful import Resource


class Seeder(Resource):

    def get(self):
        chairs = []
        for row in range(1,21):
            for chair_num in range(1,11):
                 chairs.append(ChairModel(str(row), str(chair_num)))

        try:
            ChairModel.save_all_to_db(chairs)
            return {'message': 'data insert'}, 200
        except Exception as e:
            print("Error {}", e)
            return {'message': e}, 500
