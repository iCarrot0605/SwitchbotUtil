from .onoff_device import OnOffDevice


class SwitchbotHumidifier(OnOffDevice):
    """Switchbot Humicifier class"""

    def __init__(self, deviceId: str):
        """Constructor"""
        super().__init__(deviceId)

    def set_mode(self, mode: int):
        """Set device mode"""
        self._body["command"] = "setMode"
        self._body["parameter"] = mode

        result = self.command(self.deviceId, self._body)
        return result.text

    def get_power(self):
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def get_humidity(self):
        """Returns humidity percentage"""
        status = self.get_status()
        return status["humidity"]

    def get_temperature(self):
        """Returns temperature in celsius"""
        status = self.get_status()
        return status["temperature"]

    def get_nebulization_efficiency(self):
        """Returns atomization efficiency percentage"""
        status = self.get_status()
        return status["nebulizationEfficiency"]

    def get_auto(self):
        """Returns if a Humidifier is in Auto Mode or not"""
        status = self.get_status()
        return status["auto"]

    def get_child_lock(self):
        """Returns if a Humidifier's safety lock is on or not"""
        status = self.get_status()
        return status["childLock"]

    def get_sound(self):
        """Returns if a Humidifier is muted or not"""
        status = self.get_status()
        return status["sound"]

    def get_lack_water(self):
        """Returns if the water tank is empty or not"""
        status = self.get_status()
        return status["lackWater"]
