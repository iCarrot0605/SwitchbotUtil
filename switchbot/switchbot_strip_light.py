from switchbot.switchbot_plug_mini_us import SwitchbotPlugMiniUS

class SwitchbotStripLight(SwitchbotPlugMiniUS):
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def set_brightness(self, brightness):
        """Set brightness"""
        body = {
            "commandType": "command",
            "command": "setBrightness",
        }
        body['parameter'] = brightness
        result = self.command(self.deviceId, body)
        return result.text

    def set_color(self, r, g ,b):
        """Set color

        args: r_value, g_value, b_value 0-255"""
        body = {
            "commandType": "command",
            "command": "setColor",
        }
        body['parameter'] = '{}:{}:{}'.format(r, g, b)
        result = self.command(self.deviceId, body)
        return result.text

    def get_power(self):
        """Returns ON/OFF state"""
        status = self.get_status()
        return status['power']

    def get_brightness(self):
        """Returns the brightness value, range from 1 to 100"""
        status = self.get_status()
        return status['brightness']

    def get_color(self):
        """Returns the color value, RGB '255:255:255'"""
        status = self.get_status()
        return status['color']