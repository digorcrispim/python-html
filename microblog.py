from flask import Flask #ultimo Flask é escrito em maiusculo # antes de tudo pip install flask

app = Flask("microblog")


@app.route("/")  #linka a função index a URL # acessando a url o flask aciona a função index
def index(): # função
    return "Olá Mundo"


app.run()