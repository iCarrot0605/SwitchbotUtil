from switchbotpy.switchbot_plug import SwitchbotPlug
plug = SwitchbotPlug('PlugDeviceId')
print(plug.get_power())
