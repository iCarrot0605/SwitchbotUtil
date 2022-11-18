from .switchbot_ir_device import SwitchbotIrDevice


class IrTv(SwitchbotIrDevice):
    """Switchbot virtual ir Tv"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_channel(self, channel: int) -> str:
        """Next channel"""
        self._body["command"] = "SetChannel"
        parameter = f"{channel}"
        self._body["parameter"] = parameter
        result = self.command(self.deviceId, self._body)
        return result.text

    def volume_add(self) -> str:
        """Volume up"""
        self._body["command"] = "volumeAdd"
        result = self.command(self.deviceId, self._body)
        return result.text

    def volume_sub(self) -> str:
        """Volume down"""
        self._body["command"] = "volumeSub"
        result = self.command(self.deviceId, self._body)
        return result.text

    def channel_add(self) -> str:
        """Next channel"""
        self._body["command"] = "channelAdd"
        result = self.command(self.deviceId, self._body)
        return result.text

    def channel_sub(self) -> str:
        """Previous channel"""
        self._body["command"] = "channelSub"
        result = self.command(self.deviceId, self._body)
        return result.text


class IrIpTvStreamer(IrTv):
    """IPTV/Streamer class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)


class IrSetTopBox(IrTv):
    """Set Top Box class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)
