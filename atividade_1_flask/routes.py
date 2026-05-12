from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Mundo!'

@app.route('/decorator')
def decorator():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Decorator</title>
        </head>
        <body>
            <h1>Decorator</h1>

            <p>
            É um padrão de projeto estrutural ou um recurso de linguagem (como em Python) que permite adicionar funcionalidades novas a um objeto, função ou classe existente dinamicamente, sem alterar seu código-fonte original
            </p>

        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)