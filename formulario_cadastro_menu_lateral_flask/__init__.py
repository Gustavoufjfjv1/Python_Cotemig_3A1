from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    usuarios = {
        1: ["Gustavo", "12402095"],
        2: ["Marcos", "cotemig2026"],
        3: ["Janaina", "cotemig2026"]
    }

    for dados in usuarios.values():
        if usuario == dados[0] and senha == dados[1]:
            return f"<h1>Bem-vindo, {usuario}!</h1>"
        
    return "<h1>Login inválido</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)