from SwitchbotDevice import SwitchbotDevice

class SwitchbotCurtain(SwitchbotDevice):
    """Switchbot Curtain class"""
    def __init(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def set_position(self, position):
        """Set curtain position 0-100%

        arg: position curtain position 0-100%"""
        body = {
            "commandType": "command",
            "command": "setPosition"
        }
        body["parameter"] = '0,ff,{}'.format(position)
        result = self.command(self.deviceId, body)
        return result.text

    def open(self):
        """Aliase of turn on command"""
        return self.turn_on()

    def close(self):
        """Aliase of turn off command"""
        return self.turn_off()

    def get_curtain_position(self):
        """Returns curtain position 0(open) to 100(close)"""
        status = self.get_status()
        return status['slidePosition']