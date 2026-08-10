import json
from urllib.request import urlopen

from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from models import Tarefa, db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    tarefas = Tarefa.listar()
    return render_template("dashboard.html", tarefas=tarefas, frase=frase_motivacional())

@dashboard_bp.route("/dashboard")
def dashboard():
    return index()


def frase_motivacional():
    try:
        with urlopen("https://api.adviceslip.com/advice", timeout=3) as resposta:
            return json.load(resposta)["slip"]["advice"]
    except (OSError, KeyError, TypeError, json.JSONDecodeError):
        return "Cada tarefa concluída aproxima você do objetivo."


@dashboard_bp.route("/nova_tarefa", methods=["GET", "POST"])
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "Pendente")
        if titulo and descricao and status in {"Pendente", "Em andamento", "Concluída"}:
            tarefa = Tarefa(titulo=titulo, descricao=descricao, status=status)
            db.session.add(tarefa)
            db.session.commit()
        return redirect(url_for("dashboard.index"))
    return render_template("formulario.html")


@dashboard_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "Pendente")
        if titulo and descricao and status in {"Pendente", "Em andamento", "Concluída"}:
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.status = status
            db.session.commit()
        return redirect(url_for("dashboard.index"))
    return render_template("formulario.html", tarefa=tarefa)


@dashboard_bp.route("/excluir/<int:id>")
def excluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("dashboard.index"))


@dashboard_bp.route("/concluir/<int:id>")
def concluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.status = "Concluída"
    db.session.commit()
    return redirect(url_for("dashboard.index"))


@dashboard_bp.route("/api/tarefas")
def api_tarefas():
    status = request.args.get("status")
    consulta = Tarefa.query
    if status in {"Pendente", "Em andamento", "Concluída"}:
        consulta = consulta.filter_by(status=status)
    tarefas = consulta.order_by(Tarefa.titulo).all()
    return jsonify([
        {
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "descricao": tarefa.descricao,
            "status": tarefa.status,
        }
        for tarefa in tarefas
    ])