"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, UserFavs
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)




#ALL GET OPTIONS


@app.route('/users', methods=['GET'])
def handle_hello():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200


#Peoples and People ID
@app.route('/people', methods=['GET'])
def get_all_people():
    users = People.query.all()
    all_people = list(map(lambda x: x.serialize(), users))
    return jsonify(all_people), 200



@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_id(people_id):
    people = People.query.get(people_id)
    return jsonify(people.serialize()), 200

#Planets and Planets ID


@app.route('/planets', methods=['GET'])
def get_all_planets():
    users = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), users))
    return jsonify(all_planets), 200



@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet_id(planets_id):
    planet = Planets.query.get(planets_id)
    return jsonify(planet.serialize()), 200



#User Favs
@app.route('/users/favorites', methods=['GET'])
def get_all_userfavs():
    users = UserFavs.query.all()
    all_favs = list(map(lambda x: x.serialize(), users))
    return jsonify(all_favs), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize()), 200

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favs(user_id):
    userfavs = UserFavs.query.filter_by(user_id=user_id)
    alluserfavs = list(map(lambda x: x.serialize(), userfavs))
    return jsonify(alluserfavs), 200



#ALL POST OPTIONS

#User Favs
@app.route('/users/<int:user_id>/favorites/planets/<int:planet_id>', methods=['POST'])
def add_favorite_planet(user_id, planet_id):
    user = User.query.get(user_id)
    planet = Planets.query.get(planet_id)

    if user is None or planet is None:
        return jsonify({'error': 'User or planets not found'}), 404


    favplanet = UserFavs(user_id=user.id, planets_id=planet.id)
    db.session.add(favplanet)
    db.session.commit()
    return jsonify(favplanet.serialize()), 201


@app.route('/users/<int:user_id>/favorites/peoples/<int:people_id>', methods=['POST'])
def add_favorite_people(user_id, people_id):
    user = User.query.get(user_id)
    people = People.query.get(people_id)
    favpeople = people(user_id=user.id, people_id=people.id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(favpeople.serialize()), 201




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
