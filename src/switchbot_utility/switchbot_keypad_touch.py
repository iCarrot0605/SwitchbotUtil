from .switchbot_keypad import SwitchbotKeypad


class SwitchbotKeypadTouch(SwitchbotKeypad):
    """Switchbot Keypad touch class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)
