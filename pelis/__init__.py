from flask import Flask, render_template

app = Flask(__name__)

@app.route('/messi')
def hello():
    return 'Hello, messi!'

@app.route('/actor')
def actor():
    consulta = """
        SELECT first_name, last_name FROM actor  
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db() # type: ignore
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    paginaActor = render_template("actor.html",
                              actores=lista_actores)
    return paginaActor



@app.route('/lenguaje')
def lenguaje():
    consulta = """
        SELECT first_name, last_name FROM actor  
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db() # type: ignore
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    paginalenguaje = render_template("lenguaje.html",
                              lenguaje=lista_lenguaje)
    return paginalenguaje