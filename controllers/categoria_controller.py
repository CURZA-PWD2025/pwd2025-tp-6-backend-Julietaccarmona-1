from models.categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        return CategoriaModel.get_one(id)

    @staticmethod
    def create(data):
        categoria = CategoriaModel.deserializar(data)
        categoria.create()
        return categoria.serializar()

    @staticmethod
    def update(id, data):
        categoria = CategoriaModel.query.get(id)
        if categoria:
            categoria.update(data)
            return categoria.serializar()
        return None

    @staticmethod
    def delete(id):
        categoria = CategoriaModel.query.get(id)
        if categoria:
            categoria.delete()
            return {"message": "Categoría eliminada"}
        return {"error": "Categoría no encontrada"}
