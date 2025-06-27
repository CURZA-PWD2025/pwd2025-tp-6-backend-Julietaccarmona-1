from models.marca_model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(_id: int):
        return MarcaModel.get_one(_id)

    @staticmethod
    def create(data: dict):
        nueva = MarcaModel.deserializar(data)
        nueva.create(data)
        return nueva.serializar()

    @staticmethod
    def update(_id: int, data: dict):
        marca = MarcaModel.query.get_or_404(_id)
        marca.update(data)
        return marca.serializar()

    @staticmethod
    def delete(_id: int):
        MarcaModel.delete(_id)
        return {"message": "Marca eliminada"}
