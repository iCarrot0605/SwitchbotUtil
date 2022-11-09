from .switchbot_ir_device import SwitchbotIrDevice


class IrDvd(SwitchbotIrDevice):
    """Switchbot virtual ir Tv"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_mute(self):
        """Mute/unmute"""
        self._body["command"] = "setMute"

        result = self.command(self.deviceId, self._body)
        return result.text

    def fast_forward(self):
        """Fast forward"""
        self._body["command"] = "FastForward"
        result = self.command(self.deviceId, self._body)
        return result.text

    def rewind(self):
        """Rewind"""
        self._body["command"] = "Rewind"
        result = self.command(self.deviceId, self._body)
        return result.text

    def next_track(self):
        """Next track"""
        self._body["command"] = "Next"
        result = self.command(self.deviceId, self._body)
        return result.text

    def previous(self):
        """Last track"""
        self._body["command"] = "Previous"
        result = self.command(self.deviceId, self._body)
        return result.text

    def pause(self):
        """Pause"""
        self._body["command"] = "Pause"
        result = self.command(self.deviceId, self._body)
        return result.text

    def play(self):
        """Play/resume"""
        self._body["command"] = "Play"
        result = self.command(self.deviceId, self._body)
        return result.text

    def stop(self):
        """Stop"""
        self._body["command"] = "Stop"
        result = self.command(self.deviceId, self._body)
        return result.text


class IrSpeaker(IrDvd):
    """IPTV/Streamer class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def volume_add(self):
        """Volume up"""
        self._body["command"] = "volumeAdd"
        result = self.command(self.deviceId, self._body)
        return result.text

    def volume_sub(self):
        """Volume down"""
        self._body["command"] = "volumeSub"
        result = self.command(self.deviceId, self._body)
        return result.text
