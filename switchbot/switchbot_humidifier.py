from switchbot.switchbot_device import SwitchbotDevice

class SwitchbotHumidifier(SwitchbotDevice):
    """Switchbot Humicifier class"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def set_mode(self,mode):
        """Set device mode"""
        body = {
            "commandType": "command",
            "command": "setMode"
        }
        body['parameter'] = mode

        result = self.command(self.deviceId, body)
        return result.text

    def get_power(self):
        """Returns ON/OFF state"""
        status = self.get_status()
        return status['power']

    def get_humidity(self):
        """Returns humidity percentage"""
        status = self.get_status()
        return status['humidity']

    def get_temperature(self):
        """Returns temperature in celsius"""
        status = self.get_status()
        return status['temperature']

    def get_nebulization_efficiency(self):
        """Returns atomization efficiency percentage"""
        status = self.get_status()
        return status['nebulizationEfficiency']

    def get_auto(self):
        """Returns if a Humidifier is in Auto Mode or not"""
        status = self.get_status()
        return status['auto']

    def get_child_lock(self):
        """Returns if a Humidifier's safety lock is on or not"""
        status = self.get_status()
        return status['childLock']

    def get_sound(self):
        """Returns if a Humidifier is muted or not"""
        status = self.get_status()
        return status['sound']

    def get_lack_water(self):
        """Returns if the water tank is empty or not"""
        status = self.get_status()
        return status['lackWater']