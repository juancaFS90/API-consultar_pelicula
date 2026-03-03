
from api.db import collection
from service.publisher import publish_message
from flask import Blueprint, request, jsonify
from api.schemas.schemas import PeliculaSch, PeliculaUpdate

from bson import ObjectId
from marshmallow import ValidationError

routes=Blueprint("routes", __name__)

pelicula_schema=PeliculaSch()
pelicula_update=PeliculaUpdate()


@routes.route("/createMovie", methods=["POST"])
def create_movie():

    try:
        data=pelicula_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    result=collection.insert_one(data)

    publish_message({"action": "create", "movi_id": str(result.inserted_id)})

    return jsonify({"mensaje": "Pelicula creada"}), 201


@routes.route("/Obtain_all_movie", methods=["GET"])
def obtain_all_movie():
    peliculas=[]

    for pelicula in collection.find():
        pelicula["_id"]=str(pelicula["_id"])
        peliculas.append(pelicula)

    return jsonify(peliculas), 200


@routes.route("/Obtain_one_movie/<id>", methods=["GET"])
def Obtain_one_movie(id):

    try:
        pelicula=collection.find_one({"_id": ObjectId(id)})

        if not pelicula:
            return jsonify({"error": "Pelicula no encontrada"}), 404
        
        pelicula["_id"]=str(pelicula["_id"])

        return jsonify(pelicula), 200
    
    except Exception:
        return jsonify({"error": "ID invalido"}), 400
    
@routes.route("/updateMovie/<id>", methods=["PUT"])
def updateMovie(id):

    try:
        data=pelicula_update.load(request.get_json())

        if not data:
            return jsonify({"error": "Se necesitan datos"}), 400
        
        result=collection.update_one({"_id": ObjectId(id)}, {"$set":data})

        if result.matched_count == 0:
            return jsonify({"error": "Pelicula no encontrada"}), 404
        
        publish_message({"action": "update", "movie_id":id, "data": data})

        return jsonify({"message": "Pelicula actualizada"}), 200
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    except Exception:
        return jsonify({"error": "ID invalido"}), 400
    
@routes.route("/deleteMovie/<id>", methods=["DELETE"])
def deleteMovie(id):
    try:

        result=collection.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({"error": "Pelicula no encontrada"}), 404
        
        publish_message({"action": "delete", "movie_id": id})

        return jsonify({"message": "Pelicula eliminada"}), 200
    
    except Exception:
        return jsonify({"error": "ID invalido"}), 400
    