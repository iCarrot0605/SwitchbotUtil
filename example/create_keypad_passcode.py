from switchbot_utility.switchbot_keypad import SwitchbotKeypad

keypad = SwitchbotKeypad("KeypadDeviceId")
print(
    keypad.create_key_limited(
        name="Test code",
        type="timeLimit",
        password="1234567890",
        start_time="2022/10/31 12:00:00",
        end_time="2022/11/6 12:00:00",
    )
)
