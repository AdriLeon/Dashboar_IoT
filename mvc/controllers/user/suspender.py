import web
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/user/")

class Suspender:
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            formulario = web.unput()
            email = formulario.email
            localId = web.cookies().get('localId')
            user = db.child
