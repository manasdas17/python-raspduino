from flask import Flask, Response
from automation.room.garage import Garage
from automation.device.arduino_proxy import ArduinoProxy


app = Flask(__name__)
garage = Garage(ArduinoProxy('/dev/tty.usbmodem1421'), 10)

@app.route('/door/open')
def open():
    return Response(garage.open_door(), status=202)

@app.route('/door/close')
def close():
    return Response(garage.close_door(), status=202)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)