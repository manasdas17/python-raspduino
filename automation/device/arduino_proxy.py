from time import sleep
from pyfirmata import Arduino


class ArduinoProxy():

    def __init__(self, device):
        self.board = Arduino(device)

    def digital_write(self, pin, value):
        self.board.digital[pin].write(value)

    def digital_read(self, pin):
        return self.board.digital[pin].read()

    def digital_toggle(self, pin):
        self.digital_write(pin, int(not self.digital_read(pin)))

    def digital_temporary_toggle(self, pin, delay_in_secs):
        self.digital_write(pin, 1)
        sleep(delay_in_secs)
        self.digital_write(pin, 0)