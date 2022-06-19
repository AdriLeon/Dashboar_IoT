import web 
import pyrebase
import firebase_config as token
import app as app
import json

render = web.template.render("mvc/views/public/")

class Login:
    def GET(self):
        try: 
            message = None
            return render.login(message)
        except Exception as error: 
            message = "Error en el sistema"
            print("Error Login.GET: {}".format(error))
            return render.login(message)

    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            db = firebase.database()
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            print(email)
            user = auth.sign_in_with_email_and_password(email, password)
            print(user['localId'])
            web.setcookie('localId', user['localId'], 3600)
            print("localId: ", web.cookies().get('localId'))
            results = db.child("users").child(user['localId']).child("data_user").get()
            print(results.val())
            if results.val()['status'] == 'Enable':
                return web.seeother("/inicio")
            else:
                message = 'Cuenta Deshabilitada, Por favor ponerse en contacto con Soporte'
                return render.login(message)
        except Exception as error:
            format =json.loads(error.args[1])
            error = format['error']
            message = error['message']
            print("Error Login.POST: {}".format(message))
            web.setcookie('localId', '', 3600)
            return render.login(message)