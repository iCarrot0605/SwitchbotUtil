from switchbot_utility.command_mixin import CommandMixin
from switchbot_utility.onoff_mixin import OnOffMixin
from switchbot_utility.switchbot import Switchbot


class SwitchbotIrDevice(Switchbot, OnOffMixin, CommandMixin):
    """Switchbot virtual ir device"""

    def __init__(self, deviceId):
        """Constructor"""
        self.deviceId = deviceId
