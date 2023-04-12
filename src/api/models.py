from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
#creo tabla people
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation = db.Column(db.Integer, unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation": self.rotation,
            # do not serialize the password, its a security breach
        }

class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    people = db.relationship('People')
    user = db.relationship('User')

    def serialize(self):
        return {
            "id": self.id,
            "id_people": self.id_people,
            "id_user": self.id_user,
            # do not serialize the password, its a security breach
        }


class Fav_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets = db.relationship('Planets')
    user = db.relationship('User')

    def serialize(self):
        return {
            "id": self.id,
            "id_planets": self.id_planets,
            "id_users": self.id_user,
        }

