from .onoff_mixin import OnOffMixin
from .switchbot_device import SwitchbotDevice


class SwitchbotIrDevice(SwitchbotDevice, OnOffMixin):
    """Switchbot virtual ir device"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
