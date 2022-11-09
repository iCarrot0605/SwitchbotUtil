from .switchbot import Switchbot


class OnOffAbility(Switchbot):
    """On/Off Ability to some Switchbot devices."""

    def __init__(self):
        super().__init__()

    def turn_on(self):
        """Turn on device"""
        self._body["command"] = "turnOn"
        result = self.command(self.deviceId, self._body)
        return result.text

    def turn_off(self):
        """Turn off device"""
        self._body["command"] = "turnOff"
        result = self.command(self.deviceId, self._body)
        return result.text
