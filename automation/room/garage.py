
class Garage():

    is_open = False

    def __init__(self, ArduinoProxy, door_pin):
        self.arduino = ArduinoProxy
        self.door_relay_pin = door_pin

    def open_door(self):
        if not self.is_open:
            self.arduino.digital_toggle(self.door_relay_pin)
            self.is_open = True

    def close_door(self):
        if self.is_open:
            self.arduino.digital_toggle(self.door_relay_pin)
            self.is_open = False



