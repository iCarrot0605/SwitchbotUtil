from SwitchbotDevice import SwitchbotDevice
from datetime import datetime as dt

class SwitchbotKeypad(SwitchbotDevice):
    """Switchbot Keypad class"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def _convert_datetime(self, datetime):
        """Convert datetime string to unixtime"""
        return int(dt.timestamp(dt.strptime(datetime, '%Y/%m/%d %H:%M:%S')))

    def create_key(self, name, type, password, start_time, end_time):
        """Create a new passcode

        args:
            name: passcode name
            type: type of passcode permanent, timeLimit, disposable, or urgent
            password: a 6 to 12-digit passcode in plain text
            start_time: start time like 2000/12/31 23:59:15
            end_time: end time like start_time"""
        parameter = {}
        parameter['name'] = name
        parameter['type'] = type
        parameter['password'] = password
        parameter['startTime'] = self._convert_datetime(start_time)
        parameter['endTime'] = self._convert_datetime(end_time)

        body = {
            "commandType": "command",
            "command": "createKey"
        }
        body['parameter'] = parameter

        result = self.command(self.deviceId, body)
        return result.text