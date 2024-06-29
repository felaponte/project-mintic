from database.db import *
from flask import render_template, request
from controller.admin_s3 import connection_s3, save_file, upload_file, consult_file

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")
    
def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    ownername = request.form["ownername"]
    ownerlastname = request.form["ownerlastname"]
    birthday = request.form["birthday"]
    animal = request.form["animal"]
    breed = request.form["breed"]
    print("ok")
    photo = request.files["photo"]
    print("aca")
    confirm_user = add_user(id, name, ownername, ownerlastname, birthday, animal, breed)
    print("aca vamos")
    if confirm_user:
        s3_resource = connection_s3() # conexion s3
        print("conected to S3")
        photo_path_local = save_file(photo) # se guarda foto en local
        confirm_photo = upload_file(s3_resource, photo, photo_path_local, id) # se carga foto con nombre de id
        if confirm_photo:
            return "<h1>the user and the photo were saved</h1>"
        else:
            return "<h1>the user was created without photo</h1>"
    else:
        return "<h1>Error: the user was not created</h1>"
        
def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    passw = obj_user["passw"] #es solo para una prueba
    result_data = consult_user(id)
    if result_data != False and len(result_data) != 0:
        s3_resource = connection_s3() #conexion a s3
        file_found = consult_file(s3_resource, id) # se busca el archivo
        if file_found != None:
            url_file = "https://proy-vet-mintic.s3.amazonaws.com/" + file_found # la url va ser la urla del bucket + el path de la imagen en S3
        else :
            url_file = "No photo"
        response = {
            'status' : "ok",
            'id' : id,
            'name' : result_data[0][1],
            'ownername' : result_data[0][2],
            'ownerlastname' : result_data[0][3],
            'birthday' : result_data[0][4],
            'animal' : result_data[0][5],
            'breed' : result_data[0][6],
            'url_photo' : url_file
        }
    else:
        response = {
            'status' : "error"
        }
    return response