from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo='Bienvenido', mensaje='¡Hola desde Flask!')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre Nosotros')

if __name__ == '__main__':
    app.run(debug=True)
