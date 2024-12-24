[![PyPI -
Downloads](https://img.shields.io/pypi/dm/switchbot-utility?style=plastic)](https://pypi.org/project/switchbot-utility/)
[![PyPI](https://img.shields.io/pypi/v/switchbot-utility?style=plastic)](https://pypi.org/project/switchbot-utility/)
[![PyPI -
License](https://img.shields.io/pypi/l/switchbot-utility?style=plastic)](https://pypi.org/project/switchbot-utility/)

# Switchbot_utility

Python Switchbot Utilities using Switchbot API.

## Installing

```plain
pip install switchbot-utility
```

## Getting start

Get token and secret,

1. Download the SwitchBot app on App Store or Google Play Store
2. Register a SwitchBot account and log in into your account
3. Generate an Open Token within the app
a) Go to Profile > Preference
b) Tap App Version 10 times. Developer Options will show up
c) Tap Developer Options
d) Copy token and secret

create `settings.json` file, and fill token and secret.

```python
{
    "token": "",
    "secret": ""
}
```

Run example script.

```python
import switchbot_utility.switchbot as sbu

switchbot = sbu.Switchbot()
switchbot.devicelist()
```

Scripts makes `deviceList.txt`. You can manipulate device using diviceId in this file.

## Other Example

### Get temperature from SwitchbotMeter

```python
import switchbot_utility as sbu

meter = sbu.SwitchbotMeter("meterDeviceId")
print(meter.get_temperature())
```

### Unlock SwitchbotLock

```python
import switchbot_utility as sbu

lock = sbu.SwitchbotLock("lockDeviceId")
lock.unlock()
```

## Commands reference

[Read the document](https://icarrot0605.github.io/switchbot_utility_docs/)

## Supported device

| Term                         | Description                                                  | Model No.    |Tested|
| ---------------------------- | ------------------------------------------------------------ | ------------ |------|
| Hub Mini                     | Short for SwitchBot Hub Mini                                 | W0202200 | Yes |
| Hub Plus                     | Short for SwitchBot Hub Plus                                 | SwitchBot Hub S1| No |
| Hub 2                     | Short for SwitchBot Hub 2 | W3202100      | Yes |
| Bot                          | Short for SwitchBot Bot | SwitchBot S1               | Yes |
| Curtain                      | Short for SwitchBot Curtain | W0701600               | Yes |
| Curtain 3                    | Short for SwitchBot Curtain 3 |W2400000              | No |
| Plug                         | Short for SwitchBot Plug | SP11. | Yes |
| Meter                        | Short for SwitchBot Thermometer and Hygrometer | SwitchBot MeterTH S1 | Yes |
| Meter Plus (JP)              | Short for SwitchBot Thermometer and Hygrometer Plus (JP) | W2201500 | Yes |
| Meter Plus (US)              | Short for SwitchBot Thermometer and Hygrometer Plus (US) | W2301500 | No |
| Motion Sensor                | Short for SwitchBot Motion Sensor | W1101500         | No |
| Contact Sensor               | Short for SwitchBot Contact Sensor | W1201500        | Yes |
| Color Bulb                   | Short for SwitchBot Color Bulb | W1401400            | Yes |
| Strip Light                  | Short for SwitchBot LED Strip Light | W1701100       | No |
| Plug Mini (US)               | Short for SwitchBot Plug Mini (US) | W1901400 and W1901401 | No |
| Plug Mini (JP)               | Short for SwitchBot Plug Mini (JP) | W2001400 and W2001401 | Yes |
| Lock                         | Short for SwitchBot Lock | W1601700                  | Yes |
| Keypad                         | Short for SwitchBot Lock | W2500010                  | No |
| Keypad Touch                         | Short for SwitchBot Lock | W2500020                  | Yes |
| Robot Vacuum Cleaner S1      | Short for SwitchBot Robot Vacuum Cleaner S1 | W3011000  | No |
| Robot Vacuum Cleaner S1 Plus | Short for SwitchBot Robot Vacuum Cleaner S1 Plus | W3011010 | No |
| Ceiling Light      | Short for SwitchBot Ceiling Light | W2612230 and W2612240 | No |
| Ceiling Light Pro | Short for SwitchBot Ceiling Light Pro | W2612210 and W2612220 | No |
| Indoor Cam | Short for SwitchBot Indoor Cam | W1301200                  | No |
| Pan/Tilt Cam | Short for SwitchBot Pan/Tilt Cam | W1801200                  | No |
| Pan/Tilt Cam 2K | Short for SwitchBot Pan/Tilt Cam 2K | W3101100                  | No |
| Blind Tilt | Short for SwitchBot Blind Tilt | W2701600 | No |
