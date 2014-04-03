import unittest
from mock import Mock
from hamcrest import assert_that, equal_to
from automation.room.garage import Garage
from automation.device.arduino_proxy import ArduinoProxy


class GarageTest(unittest.TestCase):

    def setUp(self):
        self.door_relay_pin = 10
        self.door_open_sensor_pin = 11
        self.trigger_length = 0.5
        self.arduino_proxy = ArduinoProxy
        self.arduino_proxy.digital_read = Mock()
        self.arduino_proxy.digital_write = Mock()
        self.arduino_proxy.digital_temporary_toggle = Mock()
        self.garage = Garage(self.arduino_proxy, self.door_relay_pin, 3, 4)

    def test_that_we_can_open_the_door(self):
        self.garage.open_door()
        self.arduino_proxy.digital_temporary_toggle.assert_called_with(self.door_relay_pin, self.trigger_length)

    def test_that_when_opening_the_door_the_correct_state_is_returned(self):
        self.garage.open_door()
        assert_that(self.garage.is_open, equal_to(True))

    def test_that_we_can_close_the_door(self):
        self.garage.open_door()
        self.garage.close_door()
        self.arduino_proxy.digital_temporary_toggle.assert_called_with(self.door_relay_pin, self.trigger_length)

    def test_that_when_closing_the_door_the_correct_state_is_returned(self):
        self.garage.close_door()
        assert_that(self.garage.is_open, equal_to(False))

    def test_that_we_cant_open_the_door_when_its_currently_opened(self):
        self.garage.open_door()
        self.garage.open_door()
        self.arduino_proxy.digital_temporary_toggle.assert_called_once_with(self.door_relay_pin, self.trigger_length)

    def test_that_we_cant_close_the_door_when_its_currently_closed(self):
        self.garage.close_door()
        self.garage.close_door()
        assert not self.arduino_proxy.digital_temporary_toggle.called

    def test_that_the_door_status_is_open_when_opened_sensor_is_high_and_closed_sensor_low(self):
        pass
        # self.arduino_proxy.digital_read.side_effect = [ 1, 0 ]
        # assert_that(self.garage.door_status(), equal_to("Currently opened"))

        # self.arduino_proxy.digital_read.assert_called_with(3)
        # self.arduino_proxy.digital_read.assert_called_with(4)



