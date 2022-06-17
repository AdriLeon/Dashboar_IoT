import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/user/")

class Inicio:
    def GET(self):
        try:#Se intenta con este codigo
            print("Inicio.GEt localId: ", web.cookies().get('localId'))#imprime la ID de la cookie
            if web.cookies().get('localId') == "None" : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            elif web.cookies().get('localId') == None : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            else:
                firebase = pyrebase.initialize_app(token.firebaseConfig)
                db = firebase.database()
                users = web.cookies().get('localId')
                name = db.child("users").child(users).get()
                print(name.val()['name'])
                return render.inicio_user(name)#si contiene datos, se nos renderiza a la pagina de inicio
        except Exception as error:
            print("Error Inicio.GET: {}".format(error))