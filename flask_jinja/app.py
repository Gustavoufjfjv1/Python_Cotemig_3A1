from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dados_usuario = {
        "nome": "Ana",
        "idade": 17,
        "email": "ana@email.com",
    }

    lista_alunos = [
        {"nome": "Ana", "nota": 5},
        {"nome": "Bia", "nota": 7},
        {"nome": "Pedro", "nota": 3},
        {"nome": "Matheus", "nota": 9}
    ]

    return render_template('index.html', usuario=dados_usuario, alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)
