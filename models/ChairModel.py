from db import db


class ChairModel(db.Model):
    __tablename__ = 'chairs'

    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(80))
    chair_num = db.Column(db.String(80))
    status = db.Column(db.String(80))
    confirmation_id = db.Column(db.String(80))

    def __init__(self, row, chair_num):
        self.row = row
        self.chair_num = chair_num
        self.status = 'Available'
        self.confirmation_id = None

    def json(self):
        return {
                'id': self.id,
                'row': self.row,
                'chair_num': self.chair_num,
                'status': self.status
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_confirmation_id(cls, confirmation_id):
        return cls.query.filter_by(confirmation_id=confirmation_id).first()

    @classmethod
    def find_available_by_id(cls, _id):
        return cls.query.filter_by(id=_id, status='Available').first()

    @classmethod
    def find_by_row_and_num(cls, row, chair_num):
        return cls.query.filter_by(row=row, chair_num=chair_num).first()

    @classmethod
    def find_available(cls):
        return cls.query.filter_by(status='Available').all()

    @classmethod
    def find_ordered(cls):
        return cls.query.filter_by(status='Ordered').all()

    @classmethod
    def save_all_to_db(cls, main_list):
        db.session.bulk_save_objects(main_list)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()