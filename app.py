from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinema.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#tabelas
class Filme(db.Model):
    id_filme = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    classificacao = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)

    sessoes = db.relationship('Sessao', back_populates='filme')

class Sala(db.Model):
    id_sala = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

    sessoes = db.relationship('Sessao', back_populates='sala')

class Sessao(db.Model):
    id_sessao = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)

    filme_id = db.Column(db.Integer, db.ForeignKey('filme.id_filme'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)

    filme = db.relationship('Filme', back_populates='sessoes')
    sala = db.relationship('Sala', back_populates='sessoes')

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.drop_all()
    db.create_all()


#rotas para adicionar novas linhas --------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_filme', methods=['GET', 'POST'])
def add_filme():
    if request.method == 'POST':
        titulo = request.form['titulo']
        classificacao = request.form['classificacao']
        genero = request.form['genero']

        filme_existente = Filme.query.filter_by(titulo=titulo).first()
        
        #para checar se as informações já estão no banco de dados
        if filme_existente is None:
                novo_filme = Filme(titulo=titulo, classificacao=classificacao, genero=genero)
                db.session.add(novo_filme)
                db.session.commit()
                return 'Novo Filme registrado!.'
        else:
            return 'Esse filme já registrado no banco de dados.'

    return render_template('filme_cadastro.html')

@app.route('/add_sala', methods=['GET', 'POST'])
def add_sala():
    if request.method == 'POST':
        nome_sala = request.form['nome']
        capacidade = request.form['capacidade']
        
        sala_existente = Sala.query.filter_by(nome=nome_sala).first()

        #para checar se as informações já estão no banco de dados
        if sala_existente is None:
                nova_sala = Sala(nome=nome_sala, capacidade=capacidade)
                db.session.add(nova_sala)
                db.session.commit()
                return 'Nova Sala registrada!.'
        else:
            return 'Essa sala já registrado no banco de dados.'

    return render_template('sala_cadastro.html')
        
@app.route('/add_sessao', methods=['GET', 'POST'])
def add_sessao():
    if request.method == 'POST':
        data = request.form['data']
        horario = request.form['horario']
        filme_sessao = request.form['filme']
        sala_sessao = request.form['sala']

        filme_sessao_existente = Filme.query.filter_by(titulo=filme_sessao).first()
        sala_sessao_existente = Sala.query.filter_by(nome=sala_sessao).first()
        
        #verificando se já existe uma sessao nesse horario
        sessao_existente = Sessao.query.filter_by(data=data, horario=horario, sala=sala_sessao_existente).first()
        
        if filme_sessao_existente and sala_sessao_existente:
            if sessao_existente:
                return 'Não é possível criar uma sessão. (Sala já ocupada nesse dia e horário)'
            else:
                nova_sessao = Sessao(
                    data=datetime.strptime(data, '%Y-%m-%d').date(),
                    horario=datetime.strptime(horario, '%H:%M').time(),
                    filme=filme_sessao_existente,
                    sala=sala_sessao_existente
                )
                db.session.add(nova_sessao)
                db.session.commit()
                return 'Nova Sessão registrada!'
        else:
            return 'Filme ou sala não registrados. Registre-os primeiro.'

    return render_template('sessao_cadastro.html')

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome_cliente = request.form['nome']
        email = request.form['email']

        cliente_existente = Cliente.query.filter_by(email=email).first()

        if cliente_existente:
                return 'Não é possível registrar esse cliente. (Email já registrado)'
        else:
            novo_cliente = Cliente(nome=nome_cliente, email=email) # type: ignore
            db.session.add(novo_cliente)
            db.session.commit()
            return 'Novo Cliente registrado!'

    return render_template('cliente_cadastro.html')

#rotas para as listagens --------------------------------------------------------
@app.route('/filmes')
def filmes():
    lista_filmes = Filme.query.all()
    return render_template('filmes.html', lista_filmes=lista_filmes)

@app.route('/salas')
def salas():
    lista_salas = Sala.query.all()
    return render_template('salas.html', lista_salas=lista_salas)

@app.route('/sessoes')
def sessoes():
    lista_sessoes = Sessao.query.all()
    return render_template('sessoes.html', lista_sessoes=lista_sessoes)

@app.route('/clientes')
def clientes():
    lista_clientes = Cliente.query.all()
    return render_template('clientes.html', lista_clientes=lista_clientes)

#rotas para a edição --------------------------------------------------------
@app.route('/update_filme/<int:filme_id>', methods=['GET', 'POST'])
def update_filme(filme_id):
    #busca o filme existente pelo id
    filme = Filme.query.get_or_404(filme_id)

    if request.method == 'POST':
        #coleta os dados enviados do cadastro
        titulo = request.form['titulo']
        classificacao = request.form['classificacao']
        genero = request.form['genero']

        #atualiza os atributos
        filme.titulo = titulo
        filme.classificacao = classificacao
        filme.genero = genero

        db.session.commit()
        return 'Filme foi atualizado!'
    
    return render_template('update_filme.html', filme=filme)

@app.route('/update_sala/<int:sala_id>', methods=['GET', 'POST'])
def update_sala(sala_id):
    sala = Sala.query.get_or_404(sala_id)

    if request.method == 'POST':
        nome_sala = request.form['nome']
        capacidade = request.form['capacidade']

        sala.nome = nome_sala
        sala.capacidade = capacidade

        db.session.commit()
        return 'Sala foi atualizada!'

    return render_template('update_sala.html', sala=sala)

@app.route('/update_sessao/<int:sessao_id>', methods=['GET', 'POST'])
def update_sessao(sessao_id):
    # Busca a sessão pelo ID, ou retorna 404 se não encontrar
    sessao = Sessao.query.get_or_404(sessao_id)

    if request.method == 'POST':
        # Coleta os dados do formulário e atualiza a sessão
        sessao.data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
        sessao.horario = datetime.strptime(request.form['horario'], '%H:%M:%S').time()
        filme_sessao = request.form['filme']
        sala_sessao = request.form['sala']

        # Checa se o filme e a sala existem
        filme_existente = Filme.query.filter_by(titulo=filme_sessao).first()
        sala_existente = Sala.query.filter_by(nome=sala_sessao).first()

        if filme_existente and sala_existente:
            sessao.filme = filme_existente
            sessao.sala = sala_existente
            db.session.commit()
            return 'Sessão atualizada com sucesso!'
        else:
            return 'Filme ou sala não encontrados. Atualização falhou.'

    # Passa a sessão ao template
    return render_template('update_sessao.html', sessao=sessao)

@app.route('/update_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def update_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)

    if request.method == 'POST':
        nome_cliente = request.form['nome']
        email = request.form['email']

        cliente.nome = nome_cliente
        cliente.email = email

        db.session.commit()
        return 'Cliente foi atualizado!'

    return render_template('update_cliente.html', cliente=cliente)

#rotas para excluir --------------------------------------------------------
@app.route('/delete_filme/<int:filme_id>')
def delete_filme(filme_id):
    filme = Filme.query.get_or_404(filme_id)
    db.session.delete(filme)
    db.session.commit()
    return 'Filme excluído!'

@app.route('/delete_sala/<int:sala_id>')
def delete_sala(sala_id):
    sala = Sala.query.get_or_404(sala_id) 
    db.session.delete(sala)  
    db.session.commit() 
    return 'Sala excluída!'

@app.route('/delete_sessao/<int:sessao_id>')
def delete_sessao(sessao_id):
    sessao = Sessao.query.get_or_404(sessao_id) 
    db.session.delete(sessao) 
    db.session.commit()
    return 'Sessão excluída!'

@app.route('/delete_cliente/<int:cliente_id>')
def delete_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return 'Cliente excluído!'

if __name__ == '__main__':
    app.run(debug=True)