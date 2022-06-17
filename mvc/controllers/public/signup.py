import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/public/")

class Signup:
    def GET(self):
        return render.signup()
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            db = firebase.database()
            #storage = firebase.storage()
            formulario = web.input()
            name = formulario.name
            email = formulario.email
            password = formulario.password
            status = 'Enable'
            user= auth.create_user_with_email_and_password(email, password)
            print(user['localId']) 
            data = {
                "name": name,
                "email": email,
                "status": status
            }
            db.child("users").child(user['localId']).child("data_user").set(data)
            #storage.child("users").child(user['localId']).child("data_user/profile.jpg").put("\static\images\image.jpg", user['idToken'])
            web.setcookie('localId', user['localId'], 3600)
            print("localId: ", web.cookies().get('localId'))
            return web.seeother("/login") 
        except Exception as error:
            format = json.loads(error.args[1])
            error = format['error']
            message = error['message']
            print("Error Login.POST: {}".format(message))
            web.setcookie('localId', '', 3600)
            return render.signup(message)