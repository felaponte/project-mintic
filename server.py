from flask import Flask, render_template, request
#from database.db import *

app = Flask(__name__)

@app.route("/")
def home_page():
    #connectionSQL()
    return render_template("home.html")

@app.route("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/consult_page")
def consult_page():
    return render_template("consult.html")
    
@app.route("/register_user", methods=["post"])    
def register_user():
    id = request.form["id"]
    name = request.form["name"]
    ownername = request.form['ownername']
    ownerlastname = request.form["ownerlastname"]
    birthday = request.form["birthday"]
    animal = request.form["animal"]
    breed = request.form["breed"]
    print(id, name, ownername, ownerlastname, birthday, animal, breed)
    return "ok"
    
#@app.route("/consult_user", methods=["post"])    
#def consult_user():
 #   print(id, name, lastname, birthday)
  #  return "ok"
    
if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port)