from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    userfavs_id = db.relationship('UserFavs')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class UserFavs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    planets_id = db.relationship('Planets', lazy=True)
    people_id = db.relationship('People', lazy=True)
    def __repr__(self):
        return '<UserFavs %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets": [Planet.serialize() for Planet in self.planets_id],
            "people": [People.serialize() for People in self.people_id],
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(200), nullable=False)
    skin_color = db.Column(db.String(200), nullable=False)
    eye_color = db.Column(db.String(200), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    homeworld = db.Column(db.String(200), nullable=False)
    favorite_people = db.Column(db.Integer, db.ForeignKey(UserFavs.id))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld

        }



class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(200), nullable=False)
    gravity = db.Column(db.String(200), nullable=False)
    terrain = db.Column(db.String(200), nullable=False)
    population = db.Column(db.Integer, nullable=True)
    favorite_planets = db.Column(db.Integer, db.ForeignKey(UserFavs.id))

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "population": self.population,
        }