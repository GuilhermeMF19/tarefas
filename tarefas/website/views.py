from flask import (Blueprint, render_template, request,
    flash, redirect, url_for, jsonify)
from flask_login import login_required, current_user
import json

from website import db
from .models import Tarefa

views = Blueprint('views', __name__)

#Rota inicial
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # Captura os dados do formulário enviado por POST
        titulo = request.form.get('titulo')
        texto = request.form.get('tarefa')

        # Validação de entrada de dados
        if len(titulo) == 0:
            flash('Título da tarefa é muito curto!', category='error')
        elif len(texto) < 1:
            flash('Texto da tarefa é muito curto!', category='error')
        else:  
            # Cria uma nova instância de Tarefa e a adiciona ao banco de dados
            nova_tarefa = Tarefa(titulo=titulo, texto=texto, usuario_id=current_user.id, status_id=1)
            db.session.add(nova_tarefa)
            db.session.commit()
            flash("Tarefa incluída!", category="success")
            return redirect(url_for('views.home')) # Redireciona de volta para a página inicial

    # Renderiza o template 'home.html' e passa o usuário atual para o template
    return render_template("home.html", usuario=current_user)

# Rota para atualizar o status de uma tarefa
@views.route('/update/<int:tarefa_id>', methods=['GET', 'POST'])
def update(tarefa_id):
    #Utiliza a variável tarefa para pegar um Tarefa existente
    tarefa = Tarefa.query.get(tarefa_id)

    if request.method == 'POST':
        # Obtém o novo status da tarefa do formulário
        status = request.form.get('status')

        # Atualiza o status da tarefa com base na escolha do usuário        
        if status == 'pronto':
            tarefa.status_id = 2
            flash("Tarefa marcada como Pronto!", category="success")
        elif status == 'afazer':
            tarefa.status_id = 1
            flash("Tarefa marcada como A fazer!", category="error")

        db.session.commit() # Salva as alterações no banco de dados
        return redirect(url_for('views.home')) # Redireciona de volta para a página inicial

    # Renderiza o template 'update_tarefa.html' com os detalhes da tarefa
    return render_template('update_tarefa.html', tarefa=tarefa)

# Rota para excluir uma tarefa                    
@views.route('/delete-Tarefa', methods=['POST'])
def delete_tarefa():
    data = json.loads(request.data)
    tarefa_id = data['tarefaId']
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        if tarefa.usuario_id == current_user.id:
            tarefa.status_id = 3 # Define o status para 'excluído'
            db.session.commit() # Salva as alterações no banco de dados
            flash("Tarefa excluída!", category="success")
    return jsonify({}) # Retorna uma resposta JSON vazia
