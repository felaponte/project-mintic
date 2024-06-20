from flask import Flask, render_template, request

app = Flask(__name__)

from routes.route import *
    
#@app.route("/consult_user", methods=["post"])    
#def consult_user():
 #   print(id, name, lastname, birthday)
  #  return "ok"
    
if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host, port)