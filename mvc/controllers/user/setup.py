import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/user/")

class Setup:
    def GET(self):
        try:
            print("Setup.GEt localId: ", web.cookies().get('localId'))
            if web.cookies().get('localId') == "None" :
                return web.seeother("/login")
            elif web.cookies().get('localId') == None :
                return web.seeother("/login")
            else:
                localId =  web.cookies().get('localId')
                firebase = pyrebase.initialize_app(token.firebaseConfig)
                db = firebase.database()
                user = db.child("users").child(localId).child("data_user").get()
                return render.setup(user, localId)
        except Exception as error:
            print("Error Setup.GET: {}".format(error))
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            formulario = web.input()
            name = formulario.name
            email = formulario.email
            localId =  web.cookies().get('localId')
            data = {
                "name": name,
                "email": email
            }
            db.child("users").child(localId).child("data_user").update(data)
            return web.seeother("/inicio")
        except Exception as error:
            print("Error Setup.GET: {}".format(error))