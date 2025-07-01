from app import db

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            descripcion=data.get("descripcion")
        )

    @staticmethod
    def get_all():
        return [c.serializar() for c in CategoriaModel.query.all()]

    @staticmethod
    def get_one(id):
        c = CategoriaModel.query.get(id)
        return c.serializar() if c else None

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        self.descripcion = data.get("descripcion", self.descripcion)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
