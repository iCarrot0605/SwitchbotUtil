from .onoff_device import OnOffDevice


class SwitchbotCurtain(OnOffDevice):
    """Switchbot Curtain class"""

    def __init(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def set_position(self, position: int) -> str:
        """Set curtain position 0-100%

        arg: position curtain position 0-100%"""

        self._body["command"] = "setPosition"
        self._body["parameter"] = "0,ff,{}".format(position)
        result = self.command(self.deviceId, self._body)
        return result.text

    def open(self) -> str:
        """Aliase of turn on command"""
        return self.turn_on()

    def close(self) -> str:
        """Aliase of turn off command"""
        return self.turn_off()

    def get_curtain_position(self) -> dict:
        """Returns curtain position 0(open) to 100(close)"""
        status = self.get_status()
        return status["slidePosition"]
