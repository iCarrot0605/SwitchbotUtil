from switchbot.switchbot_ir_device import SwitchbotIrDevice

class IrTv(SwitchbotIrDevice):
    """Switchbot virtual ir Tv"""
    body = {
    "commandType": "command",
    "parameter": "default"
}

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_channel(self, channel):
        """Next channel"""
        self.body['command'] = 'SetChannel'

        parameter = f'{channel}'
        self.body['parameter'] = parameter
        result = self.command(self.deviceId, self.body)
        return result.text

    def volume_add(self):
        """Volume up"""
        self.body['command'] = 'volumeAdd'
        result = self.command(self.deviceId, self.body)
        return result.text

    def volume_sub(self):
        """Volume down"""
        self.body['command'] = 'volumeSub'
        result = self.command(self.deviceId, self.body)
        return result.text

    def channel_add(self):
        """Next channel"""
        self.body['command'] = 'channelAdd'
        result = self.command(self.deviceId, self.body)
        return result.text

    def channel_sub(self):
        """Previous channel"""
        self.body['command'] = 'channelSub'
        result = self.command(self.deviceId, self.body)
        return result.text

class IrIpTvStreamer(IrTv):
    """IPTV/Streamer class"""
    def __init__(self, deviceId):
         super().__init__(deviceId)

class IrSetTopBox(IrTv):
    """Set Top Box class"""
    def __init__(self, deviceId):
         super().__init__(deviceId)