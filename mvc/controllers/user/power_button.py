import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/user/")

class Power_Button:
    def GET(self, wid):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            localId = web.cookies().get('localId')
            power = db.child("users").child(localId).child("data_widget").child("controlador").child("power").child(wid).get()
            if power.val()['value'] == 0 or power.val()['value'] == "0":
                data = {
                        "value": 1,
                        "power": "Encendido"
                    }
                db.child("users").child(localId).child("data_widget").child("controlador").child("power").child(wid).update(data)
                return web.seeother('/inicio')
            elif power.val()['value'] == 1 or power.val()['value'] == "1":
                data = {
                        "value": 0,
                        "power": "Apagado"
                    }
                db.child("users").child(localId).child("data_widget").child("controlador").child("power").child(wid).update(data)
                return web.seeother('/inicio')
            else:
                print("Error al actualizar los datos")
                return web.seeother('/inicio')
        except Exception as error:
            print("Error Power Button.GET: {}".format(error))