from .switchbot_robot_vacuum_cleaner_s1 import SwitchbotRobotVacuumCleanerS1


class SwitchbotRobotVacuumCleanerS1Plus(SwitchbotRobotVacuumCleanerS1):
    """Switchbot Vacuum Cleaner S1 Plus class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
