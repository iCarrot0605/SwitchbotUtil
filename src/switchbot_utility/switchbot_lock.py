from .switchbot_device import SwitchbotDevice


class SwitchbotLock(SwitchbotDevice):
    """Switchbot Lock class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def lock(self) -> str:
        """Lock a lock"""
        body = {
            "commandType": "command",
            "parameter": "default",
            "command": "lock",
        }
        result = self.command(self.deviceId, body)
        return result.text

    def unlock(self) -> str:
        """Unlock a lock"""
        body = {
            "commandType": "command",
            "parameter": "default",
            "command": "unlock",
        }
        result = self.command(self.deviceId, body)
        return result.text

    def get_lock_state(self) -> str:
        """Returns if locked or not"""
        status = self.get_status()
        return status["lockState"]

    def get_door_state(self) -> str:
        """Returns if closed or not"""
        status = self.get_status()
        return status["doorState"]
