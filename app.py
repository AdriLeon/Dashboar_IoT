import web

urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.login.Login',
    '/signup', 'mvc.controllers.public.signup.Signup',
    '/inicio', 'mvc.controllers.user.inicio.Inicio',
    '/logout', 'mvc.controllers.user.logout.Logout',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
    '/setup', 'mvc.controllers.user.setup.Setup',
    '/about', 'mvc.controllers.public.about.About',
    '/user_about', 'mvc.controllers.user.user_about.User_About',
    '/suspender', 'mvc.controllers.user.suspender.Suspender'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()