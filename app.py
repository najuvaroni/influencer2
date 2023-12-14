from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request,redirect, session, flash

app = Flask(__name__)
app.secret_key= 'Senai'
class cadInfluencers:
    def __init__(self,nome,plataforma,seguidores,areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas

lista=[]

@app.route('/Influenciadores')
def pokemon():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template(' Influenciadores.html',Titulo = "Cadastro de Influenciadores Digitais:",ListaInfluenciadores = lista)

@app.route('/Cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro de  Influenciadores")

@app.route('/')
def login():
    session.clear() #assim que eu acessar a rota, limpa oque tem dentro da sessão.
    return render_template('Login.html', Titulo="Faça o seo login")

@app.route('/autenticar', methods=['POST']) #essa rotas é para quando o usuário
# se cadastrar caso não tiver login e se caso tiver o login já entra direto.
def autenticar():
    if request.form['usuario'] == 'Anaju' and request.form['senha'] =='123':
        session['Usuario_Logado'] = request.form['usuario'] #usuarioL é uma parametro
        flash('Usuario Logado com Sucesso')
        return redirect('/Cadastro')
    else:
        flash('Usuário não encontrado') #flash manda uma mensagem
        return redirect('/login')

@app.route('/criar', methods=['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        plataforma = request.form['plataforma']
        seguidores = request.form['seguidores']
        areas = request.form['areas']
        obj =cadInfluencers(nome,plataforma,seguidores,areas)
        lista.append(obj)
        return redirect('/Influenciadores')
    elif 'deslogar' in request.form:
        session.clear()
        return redirect('/')

@app.route('/excluir/<nomeinflu>', methods=['GET','DELETE'])
def excluir(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            lista.pop(i)
            break
    return redirect('/Influenciadores')

@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, Influ in enumerate(lista):
        if Influ.nome == nomeinflu:
            return render_template('Editar.html', Influencer = Influ, titulo="Alterar influencer")

@app.route('/alterar', methods=['POST', "PUT"])
def alterar():
    nome = request.form['nome']
    for i, influ in enumerate(lista): # o request acessa as informações do formulário
        if influ.nome == nome:
            influ.nome = request.form['nome']
            influ.plataforma = request.form['plataforma']
            influ.seguidores = request.form['seguidores']
            influ.areas = request.form['areas']
    return  redirect('/Influenciadores')


if __name__ == '__main__':
    app.run()
