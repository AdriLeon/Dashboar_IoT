import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/public/")

class Recuperar:
    def GET(self):
        return render.recuperar()
    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth() # Este nos permitira autenticar con firebase
        formulario = web.input() #tomara los datos del formulario
        email = formulario.email #el email del formulario se almacena en la variable
        result = auth.send_password_reset_email(email)
        print(result)
        return web.seeother("/login")