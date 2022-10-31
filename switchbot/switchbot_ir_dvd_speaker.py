from .switchbot_ir_device import SwitchbotIrDevice

class IrDvd(SwitchbotIrDevice):
    """Switchbot virtual ir Tv"""
    body = {
    "commandType": "command",
    "parameter": "default"
    }

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_mute(self):
        """Mute/unmute"""
        self.body['command'] = 'setMute'

        result = self.command(self.deviceId, self.body)
        return result.text

    def fast_forward(self):
        """Fast forward"""
        self.body['command'] = 'FastForward'
        result = self.command(self.deviceId, self.body)
        return result.text

    def rewind(self):
        """Rewind"""
        self.body['command'] = 'Rewind'
        result = self.command(self.deviceId, self.body)
        return result.text

    def next_track(self):
        """Next track"""
        self.body['command'] = 'Next'
        result = self.command(self.deviceId, self.body)
        return result.text

    def previous(self):
        """Last track"""
        self.body['command'] = 'Previous'
        result = self.command(self.deviceId, self.body)
        return result.text

    def pause(self):
        """Pause"""
        self.body['command'] = 'Pause'
        result = self.command(self.deviceId, self.body)
        return result.text

    def play(self):
        """Play/resume"""
        self.body['command'] = 'Play'
        result = self.command(self.deviceId, self.body)
        return result.text

    def stop(self):
        """Stop"""
        self.body['command'] = 'Stop'
        result = self.command(self.deviceId, self.body)
        return result.text

class IrSpeaker(IrDvd):
    """IPTV/Streamer class"""
    def __init__(self, deviceId):
         super().__init__(deviceId)

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