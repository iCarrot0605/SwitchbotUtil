# SwitchbotUtil

## Switchbot Utilities

元々、[Switchbot API V1.1用の署名ヘッダー作成プログラム](https://qiita.com/hide19710605/items/25316411cc277df2835b)を作り、それを利用するためのプログラムを作ろうとしていました。Pythonのclassを勉強するためにこんな感じになりました。

## 使い方

tokenとsecretの入手

1. Switchbot App(V6.14以降)をダウンロード

1. 「プロフィール」＞「設定」へと進み、「アプリバージョン」のフィールドを10回タップすると表示される「開発者向けオプション」から取得することができます。

以下のようなsettings.jsonファイルを作成しtokenとsecretを記入

```python
{
    "token": "",
    "secret": ""
}
```

`python3 get_devicelist.py`で同じディレクトリ内にdeviceList.txtというSwitchbotデバイス一覧ファイルが作成されます。

deviceList.txt内のdeviceIDを使って各種デバイスを操作します。

## サンプルプログラム

Switchbot Botの電源ON/OFFを確認する

```python
from switchbot.switchbot_bot import SwitchbotBot
bot = SwitchbotBot('BotdeviceId')
print(bot.get_power())
```

Switchbot Lockを解除する

```python
from switchbot.switchbot_lock import SwitchbotLock
lock = SwitchbotLock('LockDeviceId')
lock.unlock()
```

## TODO

1. Switchbot Keypad/Keypad touchのパスコード作成は今のところちゃんと動作していません。原因不明です。
1. PyPiに登録したいけど、登録できるような形に仕上げる能力がありません。
