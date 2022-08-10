import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/user/")

class Delete_Data:
    def GET(self, wid):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            localId = web.cookies().get('localId')
            db.child("users").child(localId).child("data_widget").child("controlador").child("power").child(wid).remove()
            return web.seeother('/inicio')
        except Exception as error:
            print("Error Delete Data.GET: {}".format(error))