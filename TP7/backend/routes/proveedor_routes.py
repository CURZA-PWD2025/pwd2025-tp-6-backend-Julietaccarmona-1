from flask import Blueprint, request, jsonify
from controllers.proveedor_controller import ProveedorController

proveedor_bp = Blueprint("proveedor_bp", __name__)

@proveedor_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    proveedor = ProveedorController.get_one(id)
    return jsonify(proveedor) if proveedor else ({"error": "No encontrado"}, 404)

@proveedor_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    nuevo = ProveedorController.create(data)
    return jsonify(nuevo), 201

@proveedor_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    actualizado = ProveedorController.update(id, data)
    return jsonify(actualizado) if actualizado else ({"error": "No encontrado"}, 404)

@proveedor_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(ProveedorController.delete(id))
