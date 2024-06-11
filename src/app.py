from flask import Flask, render_template, request
from config import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/nuevolibro")
def nuevo_libro():
    return render_template('nuevo_libro.html')

@app.route("/agregarlibro", methods=['POST'])
def agregar_libro():
    titulo = request.form['book-title']
    return render_template('nuevo_libro.html', resultado=f'El título del libro es: "{titulo}"')

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.run()