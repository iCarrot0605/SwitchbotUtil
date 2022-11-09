from .switchbot_device import SwitchbotDevice


class SwitchbotRobotVacuumCleanerS1(SwitchbotDevice):
    """Switchbot Robot Vacuum Cleaner S1 class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def start(self):
        """Start vacuuming"""
        self._body["command"] = "start"
        result = self.command(self.deviceId, self._body)
        return result.text

    def stop(self):
        """Stop vacuuming"""
        self._body["command"] = "stop"
        result = self.command(self.deviceId, self._body)
        return result.text

    def dock(self):
        """Return to charging dock"""
        self._body["command"] = "dock"
        result = self.command(self.deviceId, self._body)
        return result.text

    def power_level(self, powerlevel):
        """Set suction power level

        arg: 0-3"""
        self._body["command"] = "PowLevel"
        self._body["parameter"] = powerlevel
        result = self.command(self.deviceId, self._body)
        return result.text

    def get_working_status(self):
        """Returns the working status of the device"""
        status = self.get_status()
        return status["workingStatus"]

    def get_online_status(self):
        """Returns the connection status of the device"""
        status = self.get_status()
        return status["onlineStatus"]

    def get_battery(self):
        """Returns the current battery level"""
        status = self.get_status()
        return status["battery"]
