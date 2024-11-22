from switchbot_utility.switchbot_color_bulb import SwitchbotColorBulb


class SwitchbotCeilingLight(SwitchbotColorBulb):
    """Switchbot Ceiling Light class"""

    def set_color(self, r, g, b):
        """Do nothing"""

    def get_power(self):
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def get_brightness(self):
        """Returns the brightness value, range from 1 to 100"""
        status = self.get_status()
        return status["brightness"]

    def get_color_temperature(self):
        """Returns the color temperature value, range from 2700 to 6500"""
        status = self.get_status()
        return status["colorTemperature"]
