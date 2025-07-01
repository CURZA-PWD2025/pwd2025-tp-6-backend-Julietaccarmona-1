from flask import Blueprint, request, jsonify
from controllers.marca_controller import MarcaController

marca_bp = Blueprint("marcas", __name__)

@marca_bp.get("/")
def get_all():
    return jsonify(MarcaController.get_all())

@marca_bp.get("/<int:_id>")
def get_one(_id):
    return jsonify(MarcaController.get_one(_id))

@marca_bp.post("/")
def create():
    data = request.get_json()
    return jsonify(MarcaController.create(data)), 201

@marca_bp.put("/<int:_id>")
def update(_id):
    data = request.get_json()
    return jsonify(MarcaController.update(_id, data))

@marca_bp.delete("/<int:_id>")
def delete(_id):
    return jsonify(MarcaController.delete(_id))
