from .switchbot_device import SwitchbotDevice


class IrOthers(SwitchbotDevice):
    """IR viertual device others class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def customize(self, button_name: str):
        """Execute customized command

        button_name should be quoted.
        e.g. "on", "off"
        """

        body = {"commandType": "customize", "parameter": "default"}
        body["command"] = button_name

        response = self.command(self.deviceId, body)
        return response.text
