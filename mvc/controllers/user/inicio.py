import web
import pyrebase
import firebase_config as token 
import app as app
import json
import random

render = web.template.render("mvc/views/user/")

class Inicio:
    def GET(self):
        try:
            print("Inicio.GEt localId: ", web.cookies().get('localId'))
            if web.cookies().get('localId') == "None" :
                return web.seeother("/login")
            elif web.cookies().get('localId') == None :
                return web.seeother("/login")
            else:
                firebase = pyrebase.initialize_app(token.firebaseConfig)
                storage = firebase.storage()
                db = firebase.database()
                users = web.cookies().get('localId')
                name = db.child("users").child(users).child("data_user").get()
                url = storage.child("users").child(users).child("data_user/profile.jpg").get_url(users)
                print(name.val()['name'])
                return render.inicio(name, url)
        except Exception as error:
            print("Error Inicio.GET: {}".format(error))
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            formulario = web.input()
            widget = formulario.widget
            type = formulario.type
            if type == "humedad":
                b = random.radint(10000000,20000000)
                wid = hex(b)
                localId = web.cookies().get('localId')
                data = {
                    "widget": widget,
                    "temperatura": None,
                    "humedad": None
                }
                db.child("users").child(localId).child("data_widget").child(wid).set(data)
                return web.seeother("/inicio")
            else:
                return web.seeother("/inicio")
        except Exception as error:
            print("Error Inicio.POST: {}".format(error))