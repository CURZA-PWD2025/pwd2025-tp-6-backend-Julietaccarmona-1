from flask import Flask
from data.data_productos import productos, categorias
app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, soy Julieta Carmona, estudiante de 2do año de Desarrollo Web del CURZA."

@app.route("/productos")
def listar_productos():
    resultado = ""
    for p in productos:
        resultado += f"ID: {p['id']} - Descripción: {p['descripcion']} - Categoría ID: {p['categoria_id']}<br>"
    return resultado

@app.route("/categorias")
def listar_categorias():
    resultado = ""
    for c in categorias:
        resultado += f"ID: {c['id']} - Descripción: {c['descripcion']}<br>"
    return resultado

if __name__ == "__main__":
    app.run(debug=True)
