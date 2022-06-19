import web
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/user/")

class Logout:
    def GET(self):
        web.setcookie('localId', None, 3600)
        print("Logout.GEt localId: ", web.cookies().get('localId'))
        return web.seeother('/login')

