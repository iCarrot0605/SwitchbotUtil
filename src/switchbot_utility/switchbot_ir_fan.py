from .switchbot_ir_device import SwitchbotIrDevice


class IrFan(SwitchbotIrDevice):
    """Switchbot virtual IR fan"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def swing(self) -> str:
        """Swing"""
        self._body["command"] = "swing"
        result = self.command(self.deviceId, self._body)
        return result.text

    def timer(self) -> str:
        """Set timer"""
        self._body["command"] = "timer"
        result = self.command(self.deviceId, self._body)
        return result.text

    def low_speed(self) -> str:
        """set fan speed to low"""
        self._body["command"] = "lowSpeed"
        result = self.command(self.deviceId, self._body)
        return result.text

    def middle_speed(self) -> str:
        """set fan speed to middle"""
        self._body["command"] = "middleSpeed"
        result = self.command(self.deviceId, self._body)
        return result.text

    def high_speed(self) -> str:
        """set fan speed to high"""
        self._body["command"] = "highSpeed"
        result = self.command(self.deviceId, self._body)
        return result.text
