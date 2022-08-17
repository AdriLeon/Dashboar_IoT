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
                b = random.randint(10000000, 19999999)
                c = random.randint(20000000, 29999999)
                widt = hex(b)
                widhm = hex(c)
                localId = web.cookies().get('localId')
                datat = {
                    "name": widget,
                    "temperatura": 0
                }
                datah = {
                    "name": widget,
                    "humedad": 0
                }
                db.child("users").child(localId).child("data_widget").child("sensor").child(type).child("temperatura").child(widt).set(datat)
                db.child("users").child(localId).child("data_widget").child("sensor").child(type).child("humedad").child(widhm).set(datah)
                return web.seeother("/inicio")
            elif type == "distancia":
                b = random.randint(30000000, 40000000)
                wid = hex(b)
                localId = web.cookies().get('localId')
                data = {
                    "name": widget,
                    "distancia": 0
                }
                db.child("users").child(localId).child("data_widget").child("sensor").child(type).child(wid).set(data)
                return web.seeother("/inicio")
            elif type == "velocidad":
                b = random.randint(50000000, 60000000)
                wid = hex(b)
                localId = web.cookies().get('localId')
                data = {
                    "name": widget,
                    "velocidad": 0
                }
                db.child("users").child(localId).child("data_widget").child("sensor").child(type).child(wid).set(data)
                return web.seeother("/inicio")
            elif type == "sonido":
                b = random.randint(70000000, 80000000)
                wid = hex(b)
                localId = web.cookies().get('localId')
                data = {
                    "name": widget,
                    "sonido": 0
                }
                db.child("users").child(localId).child("data_widget").child("sensor").child(type).child(wid).set(data)
                return web.seeother("/inicio")
            elif type == "power":
                b = random.randint(90000000, 100000000)
                wid = hex(b)
                localId = web.cookies().get('localId')
                data = {
                    "name": widget,
                    "value": 0,
                    "power": "Apagado"
                }
                db.child("users").child(localId).child("data_widget").child("controlador").child(type).child(wid).set(data)
                return web.seeother("/inicio")
            else:
                return web.seeother("/inicio")
        except Exception as error:
            print("Error Inicio.POST: {}".format(error))