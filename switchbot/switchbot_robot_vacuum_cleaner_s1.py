from switchbot.switchbot_device import SwitchbotDevice

class SwitchbotRobotVacuumCleanerS1(SwitchbotDevice):
    """Switchbot Robot Vacuum Cleaner S1 class"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def start(self):
        """Start vacuuming"""
        body = {
           "commandType": "command",
           "command": "start",
           "parameter": "default"
        }
        result = self.command(self.deviceId, body)
        return result.text

    def stop(self):
        """Stop vacuuming"""
        body = {
            "commandType": "command",
            "command": "stop",
            "parameter": "default"
        }
        result = self.command(self.deviceId, body)
        return result.text

    def dock(self):
        """Return tu charging dock"""
        body = {
            "commandType": "command",
            "command": "dock",
            "parameter": "default"
        }
        result = self.command(self.deviceId, body)
        return result.text

    def power_level(self, powerlevel):
        """Set suction power level

        arg: 0-3"""
        body = {
            "commandType": "command",
            "command": "PowLevel"
        }
        body['parameter'] = powerlevel
        result = self.command(self.deviceId, body)
        return result.text

    def get_working_status(self):
        """Returns the working status of the device"""
        status = self.get_status()
        return status['workingStatus']

    def get_online_status(self):
        """Returns the working status of the device"""
        status = self.get_status()
        return status['onlineStatus']

    def get_battery(self):
        """Returns the current battery level"""
        status = self.get_status()
        return status['battery']