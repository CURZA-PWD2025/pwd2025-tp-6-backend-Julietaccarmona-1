from app import db

class MarcaModel(db.Model):
    __tablename__ = "marcas"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False, unique=True)

    # CRUD 
    @staticmethod
    def get_all() -> list[dict]:
        return [m.serializar() for m in MarcaModel.query.all()]

    @staticmethod
    def get_one(_id: int) -> dict | None:
        marca = MarcaModel.query.get_or_404(_id)
        return marca.serializar()

    def create(self, data: dict):
        self.descripcion = data["descripcion"]
        db.session.add(self)
        db.session.commit()

    def update(self, data: dict):
        self.descripcion = data.get("descripcion", self.descripcion)
        db.session.commit()

    @staticmethod
    def delete(_id: int):
        marca = MarcaModel.query.get_or_404(_id)
        db.session.delete(marca)
        db.session.commit()

    # DESERIALIZACIÓN 
    def serializar(self) -> dict:
        return {"id": self.id, "descripcion": self.descripcion}

    @staticmethod
    def deserializar(data: dict) -> "MarcaModel":
        return MarcaModel(descripcion=data["descripcion"])


