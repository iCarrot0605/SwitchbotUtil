from .onoff_device import OnOffDevice


class SwitchbotStripLight(OnOffDevice):
    """Switchbot Strip Light class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def toggle(self) -> str:
        """Toggle state"""
        self._body["command"] = "toggle"
        result = self.command(self.deviceId, self._body)
        return result.text

    def set_brightness(self, brightness: int) -> str:
        """Set brightness"""
        self._body["command"] = "setBrightness"
        self._body["parameter"] = brightness
        result = self.command(self.deviceId, self._body)
        return result.text

    def set_color(self, r: int, g: int, b: int) -> str:
        """Set color

        args: r_value, g_value, b_value 0-255"""
        self._body["command"] = "setColor"
        self._body["parameter"] = "{}:{}:{}".format(r, g, b)
        result = self.command(self.deviceId, self._body)
        return result.text

    def get_power(self) -> str:
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def get_brightness(self) -> str:
        """Returns the brightness value, range from 1 to 100"""
        status = self.get_status()
        return status["brightness"]

    def get_color(self) -> str:
        """Returns the color value, RGB '255:255:255'"""
        status = self.get_status()
        return status["color"]
