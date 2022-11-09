from .switchbot_plug import SwitchbotPlug


class SwitchbotPlugMiniUS(SwitchbotPlug):
    """Switchbot Plug Mini(US) class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def toggle(self):
        """Toggle plug state"""
        self._body["command"] = "toggle"
        result = self.command(self.deviceId, self._body)
        return result.text

    def get_voltage(self):
        """Returns the voltage of the device, measured in Volt"""
        status = self.get_status()
        return status["voltage"]

    def get_weight(self):
        """Returns the power consumed in a day, measured in Watts"""
        status = self.get_status()
        return status["weight"]

    def get_electricity_of_day(self):
        """Returns the duration that the device has been used during a day(min)"""
        status = self.get_status()
        return status["electricityOfDay"]

    def get_electric_current(self):
        """Returns the current of the device at the moment, measured in Amp"""
        status = self.get_status()
        return status["electricCurrent"]
