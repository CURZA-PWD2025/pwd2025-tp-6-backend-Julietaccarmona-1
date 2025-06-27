from flask import Blueprint, request, jsonify
from controllers.categoria_controller import CategoriaController

categoria_bp = Blueprint("categoria_bp", __name__)

@categoria_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    categoria = CategoriaController.get_one(id)
    return jsonify(categoria) if categoria else ({"error": "No encontrada"}, 404)

@categoria_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    nueva = CategoriaController.create(data)
    return jsonify(nueva), 201

@categoria_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    actualizada = CategoriaController.update(id, data)
    return jsonify(actualizada) if actualizada else ({"error": "No encontrada"}, 404)

@categoria_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(CategoriaController.delete(id))
