
class Garage():

    is_open = False

    def __init__(self, ArduinoProxy, relay_pin, opened_sensor_pin, closed_sensor_pin):
        self.arduino = ArduinoProxy
        self.door_relay_pin = relay_pin
        self.opened_sensor_pin = opened_sensor_pin
        self.closed_sensor_pin = closed_sensor_pin

    def open_door(self):
        if not self.is_open:
            self.arduino.digital_temporary_toggle(self.door_relay_pin, 0.5)
            self.is_open = True

    def close_door(self):
        if self.is_open:
            self.arduino.digital_temporary_toggle(self.door_relay_pin, 0.5)
            self.is_open = False

    def door_status(self):
        opened_sensor_value = self.arduino.digital_read(3)
        closed_sensor_value = self.arduino.digital_read(3)

        if opened_sensor_value and not closed_sensor_value:
            return "Currently opened"
        elif not opened_sensor_value and closed_sensor_value:
            return "Currently closed"

        return "Door is jammed somewhere in between"


    def fake_opened_status(self):
        self.arduino.digital_toggle(self.opened_sensor_pin)

    def fake_closed_status(self):
        self.arduino.digital_toggle(self.closed_sensor_pin)

