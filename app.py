# Import WSGI ref for importing the serving library
from wsgiref.simple_server import make_server

# Configurator defines all the settings and configs in your web app
from pyramid.config import Configurator

# FileResponse is used to respond with an file (ex. HTML document)
from pyramid.response import FileResponse

# FileResponse to return home page HTML
def home_page(request):
    path = 'index.html'
    return FileResponse(path)

# This line is to tell the interpreter to start execution from here
if __name__ == '__main__':
    
    with Configurator() as config:
        # Create a route that handles server HTTP requests at: /
        config.add_route('home', '/')
        config.add_view(home_page, route_name='home')

        # Configure the directory for static resources
        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        # This is the overall compiled app with the given configurations
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6000, app)
    server.serve_forever()
