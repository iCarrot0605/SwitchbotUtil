from .onoff_mixin import OnOffMixin


class SwitchbotIrDevice(OnOffMixin):
    """Switchbot virtual ir device"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
