from .switchbot_ir_device import SwitchbotIrDevice

class IrFan(SwitchbotIrDevice):
    """Switchbot virtual IR fan"""
    body = {
    "commandType": "command",
    "parameter": "default"
}

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def swing(self):
        """Swing"""
        self.body['command'] = 'swing'
        result = self.command(self.deviceId, self.body)
        return result.text

    def timer(self):
        """Set timer"""
        self.body['command'] = 'timer'
        result = self.command(self.deviceId, self.body)
        return result.text

    def low_speed(self):
        """set fan speed to low"""
        self.body['command'] = 'lowSpeed'
        result = self.command(self.deviceId, self.body)
        return result.text

    def middle_speed(self):
        """set fan speed to middle"""
        self.body['command'] = 'middleSpeed'
        result = self.command(self.deviceId, self.body)
        return result.text

    def high_speed(self):
        """set fan speed to high"""
        self.body['command'] = 'highSpeed'
        result = self.command(self.deviceId, self.body)
        return result.text