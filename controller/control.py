from database.db import *
from flask import render_template, request

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")
    
def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    ownername = request.form['ownername']
    ownerlastname = request.form["ownerlastname"]
    birthday = request.form["birthday"]
    animal = request.form["animal"]
    breed = request.form["breed"]
    print(id, name, ownername, ownerlastname, birthday, animal, breed)
    return "ok"