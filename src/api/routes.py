"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, Fav_people, Fav_planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

#--------------------------------TABLA USER ------------------------------------------- #
#USERS GET
@api.route('/user', methods=['GET'])
def getUser():
    all_User = User.query.all()
    arr_user = list(map(lambda x:x.serialize(), all_User))
    return jsonify({"Users": arr_user})

#PEOPLE_ID GET
@api.route('/user/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    one_user = User.query.get(user_id)
    if one_user:
        return jsonify({"Person": one_user.serialize()})
    else:
        return "error!"

@api.route('/user', methods=["POST"])
def createUsers():
    data = request.get_json()
    user = User(email=data["email"],password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"user": user.serialize()}),200

#--------------------------------TABLA PEOPLE ------------------------------------------- #
#PEOPLE GET
@api.route('/people', methods=['GET'])
def getPeople():
    #funcion query all de alquemy
    all_people = People.query.all()#retorna arreglo de clases
    #traigo todos los personajes y le aplico un serialize
    arr_people = list(map(lambda x:x.serialize(), all_people))
    return jsonify({"People": arr_people})

#PEOPLE_ID GET
@api.route('/people/<int:people_id>', methods=['GET'])
def getPeopleID(people_id):
    one_people = People.query.get(people_id)
    if one_people:
        return jsonify({"Person": one_people.serialize()})
    else:
        return "error!"

#--------------------------------TABLA PLANET ------------------------------------------- #
#PLANETS GET
@api.route('/planets', methods=['GET'])
def getPlanets():
    all_planets = Planets.query.all()
    arr_planets = list(map(lambda x:x.serialize(), all_planets))
    return jsonify({"Planetas": arr_planets})

#PLANETS_ID GET
@api.route('/planets/<int:planets_id>', methods=['GET'])
def getPlanetsID(planets_id):
    one_planet = Planets.query.get(planets_id)
    if one_planet:
        return jsonify({"Planets": one_planet.serialize()})
    else:
        return "error!"

#--------------------------------TABLA FAVORITES ------------------------------------------- #
#USER_FAV_PEOPLE GET
@api.route('/favorite_people', methods=['GET'])
def getPeopleFav():
    all_favPeople = Fav_people.query.all()
    arr_fav = list(map(lambda x:x.serialize(), all_favPeople))
    return jsonify({"People Favs": arr_fav})

#USER_FAV_PLANETS GET
@api.route('/favPlanets', methods=['GET'])
def getPlanetsFav():
    all_favPlanets = Fav_planets.query.all()
    arr_fav = list(map(lambda x:x.serialize(), all_favPlanets))
    return jsonify({"Planets Favs": arr_fav})

#FAV_PEOPLE POST
@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def addFavPeople(people_id):
    user = request.get_json()
    #validar si existe usuario
    checkUser = User.query.get(user['id'])
    if checkUser:
        #crear nuevo registro de fav
        Fav_planets.create(id_user=user['id'], people_id=people_id)

        return("ok")
    else:
        return ("user doesn't exist")

#FAV_PLANETS POST
@api.route('/favorite/planets/<int:planets_id>', methods=['POST'])
def addFavPlanets(planets_id):
    user = request.get_json()
    #validar si existe usuario
    checkUser = User.query.get(user['id'])
    if checkUser:
        #crear nuevo registro de fav
        Fav_planets.create(id_user=user['id'], id_planets=planets_id)

        return("ok")
    else:
        return ("user doesn't exist")


#FAV_PEOPLE DELETE
@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def deleteFavPeople(people_id):
    user = request.get_json() #{id:1}
    allFavs = Fav_people.query.filter_by(id_user=user['id'],id_people=people_id).all()
    for i in allFavs:
        db.session.delete(i)
    db.session.commit()

    return('deleted character')

#FAV_PLANETS DELETE
@api.route('/favorite/planets/<int:planets_id>', methods=['DELETE'])
def deleteFavPlanets(planets_id):
    user = request.get_json() #{id:1}
    allFavs = Fav_planets.query.filter_by(id_user=user['id'],id_planets=planets_id).all()
    for i in allFavs:
        db.session.delete(i)
    db.session.commit()

    return('deleted planet')
    
