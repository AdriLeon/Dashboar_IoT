import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/login', 'mvc.controllers.login.Login',
    '/signup', 'mvc.controllers.signup.Signup',
    '/inicio', 'mvc.controllers.inicio.Inicio',
    '/logout', 'mvc.controllers.logout.Logout',
    '/recuperar', 'mvc.controllers.recuperar.Recuperar',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()