from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()  # <-- se define global, sin app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # <-- esto es clave

    # importar rutas
    from routes.marca_routes import marca_bp
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    
    from routes.categoria_routes import categoria_bp
    app.register_blueprint(categoria_bp, url_prefix="/categorias")

    from routes.proveedor_routes import proveedor_bp
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")

    from routes.articulo_routes import articulo_bp
    app.register_blueprint(articulo_bp, url_prefix='/articulos')

    return app
