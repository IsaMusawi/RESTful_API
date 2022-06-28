from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    items = db.relationship('ItemModel', lazy='dynamic')
        
    def __init__(self, name):
        self.name = name

    def jsonpost(self):
        return {"id": self.id, "name": self.name}

    def json(self):
        return { "id": self.id, "name": self.name, "items": [item.json() for item in self.items]}

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
