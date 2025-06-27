from models.proveedor_model import ProveedorModel
from app import db

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel.get_one(id)

    @staticmethod
    def create(data):
        nuevo = ProveedorModel.deserializar(data)
        nuevo.create()
        return nuevo.serializar()

    @staticmethod
    def update(id, data):
        proveedor = ProveedorModel.query.get(id)
        if proveedor:
            proveedor.update(data)
            return proveedor.serializar()
        return None

    @staticmethod
    def delete(id):
        proveedor = ProveedorModel.query.get(id)
        if proveedor:
            proveedor.delete()
            return {"message": "Proveedor eliminado"}
        return {"error": "Proveedor no encontrado"}
