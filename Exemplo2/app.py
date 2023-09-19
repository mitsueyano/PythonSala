from flask import Flask, render_template, request

app = Flask(__name__)

listaitens_acamp = []
listadescricao = []
listareceita = []
listaingredientes = []
listacontatos = []
listaTarefas = []

@app.route("/",methods=["GET","POST"])
def principal():
    if request.method=="POST":
         if request.form.get("itens_acamp"):
              listaitens_acamp.append(request.form.get("itens_acamp"))
    return render_template("listaAcampamento.html",listaitens_acamp=listaitens_acamp)

@app.route("/itemDescricao",methods=["GET","POST"])
def itemDescricao():
        if request.method=="POST":
         if request.form.get("item") and request.form.get("descricao"):
              listadescricao.append({"item":request.form.get("item"),"descricao":request.form.get("descricao")})
        return render_template("itemDescricao.html",listadescricao=listadescricao)

@app.route("/receita", methods=["GET", "POST"])
def receita():
    if request.method == "POST":
        if request.form.get("nome"):
            nome_receita = request.form.get("nome")
            ingredientes = request.form.getlist("ingredientes[]")
            listareceita.append({"nome": nome_receita})
            listaingredientes.append(ingredientes)
    return render_template("receita.html", listareceita=listareceita, listaingredientes=listaingredientes)

@app.route("/contatos", methods=["GET", "POST"])
def contatos():
        if request.method=="POST":
         if request.form.get("nomecontato") and request.form.get("numero"):
                listacontatos.append({"nomecontato":request.form.get("nomecontato"), "numero":request.form.get("numero")})
        return render_template("contatos.html", listacontatos=listacontatos)

@app.route("/listaTarefas", methods=["GET", "POST"])
def Tarefas():
    if request.method == "POST":
        if request.form.get("tarefa"):
            listaTarefas.append({"tarefas": request.form.get("tarefa")})
    return render_template("listaTarefas.html", listaTarefas=listaTarefas)


if __name__=="__main__":
	app.run(debug=True)