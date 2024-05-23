from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/editar")
def editar():
    return render_template('editar.html')

@app.route("/nuevolibro")
def nuevo_libro():
    return render_template('nuevo-libro.html')

@app.route("/leyendo", methods=['POST'])
def leyendo():
    titulo = request.form['book-title']
    return render_template('index.html', resultado=f'El título del libro es: "{titulo}"')

if __name__=="__main__":
    app.run(debug=True)