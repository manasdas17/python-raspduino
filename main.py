from functools import wraps
from flask import Flask, Response, request
from automation.room.garage import Garage
from automation.device.arduino_proxy import ArduinoProxy


app = Flask(__name__)
garage = Garage(ArduinoProxy('/dev/tty.usbmodem1421'), 10)

def check_auth(username, password):
    return username == 'admin' and password == '6gy7cg'

def authenticate():
    return Response('Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/door/open')
@requires_auth
def open():
    return Response(garage.open_door(), status=202)

@app.route('/door/close')
@requires_auth
def close():
    return Response(garage.close_door(), status=202)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)