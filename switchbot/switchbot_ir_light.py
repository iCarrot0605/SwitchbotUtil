from switchbot.switchbot_ir_device import SwitchbotIrDevice

class IrLight(SwitchbotIrDevice):
    """Switchbot virtual IR fan"""
    body = {
    "commandType": "command",
    "parameter": "default"
}

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def brightness_up(self):
        """Brightness up"""
        self.body['command'] = 'brightnessUp'
        result = self.command(self.deviceId, self.body)
        return result.text

    def brightness_down(self):
        """Brightness down"""
        self.body['command'] = 'brightnessDown'
        result = self.command(self.deviceId, self.body)
        return result.text