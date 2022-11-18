from .onoff_device import OnOffDevice


class SwitchbotIrDevice(OnOffDevice):
    """Switchbot virtual ir device"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
