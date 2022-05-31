import web

urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.login.Login',
    '/signup', 'mvc.controllers.public.signup.Signup',
    '/inicio', 'mvc.controllers.user.inicio.Inicio',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()