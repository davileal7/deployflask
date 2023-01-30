from flask import Flask, render_template

app = Flask(__name__) #sempre para iniciar o site
#route -> hashtagtreinamentos.com/
#função -> o que quer exibir na página
#templates

@app.route("/") #decorator atribuir uma nova funcionalidade para o próximo código
def homepage():
    return render_template("home_page.html")

@app.route('/contatos')
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>") #<usuario dinamico>
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


    # servidor do heroku
    #servidor precisa saber o que vc tem instalado no flask


