from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    stores = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price, "store_id": self.store_id}

        # A method for searching data by name    
    @classmethod
    def findByname(cls, name):
        return cls.query.filter_by(name=name).first()
        # -> The return means "SELECT * FROM items WHERE name=name LIMIT 1"

    @classmethod
    def getAll(cls):
        return cls.query.all()

    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()
