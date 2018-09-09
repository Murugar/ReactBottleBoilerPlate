import os


from bottle import get, post, run, static_file, template, request, redirect, hook, response


ROOT = os.getcwd()


@hook('after_request')
def enable_cors():
    """
    Allows the client side application running in dev mode to request API endpoints
    """
    response.headers['Access-Control-Allow-Origin'] = 'localhost:3000'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


################################################################################
#                           Client side app delivery.                          #
###############################################################################


@get('/client/<filename:path>')
def client(filename):
    """
    Exposes our client side app's /build directory at the /client endpoint.
    """
    return static_file(filename, root=ROOT + '/client/build')


@get('/')
def index():
    """
    Delivers the .html page containing our compiled and optimized client side app.
    """
    return redirect('/client/index.html')


################################################################################
#                   API endpoints for our client side app.                     #
###############################################################################


if __name__ == '__main__':
    run(server='tornado', host='localhost', port=8080, debug=True)
