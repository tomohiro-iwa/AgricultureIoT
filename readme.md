# 教材

## TODO
温度センサ- 使える所まで行きたい
raspberrypi OS焼きたい


## Linux
 
### sudo コマンド
たとえば`sudo vim ` だと管理者権限で編集が出来る
`sudo shutdown` 

### apt コマンド
ライブラリやソフトをインストールしたり更新したりするコマンド
基本的にsudo必須。

apt-getというコマンド名になっている時も、だいたい意味は一緒。aptに変えてもだいたい動く




## Raspberry

### Grove base hat
コネクタの形は一緒だが、通信手段が違うので刺す場所を間違うとちょっと危険

i2cならモジュールにSDAとSCLと書いてある

### gpioコマンド
gpioの現在の状態を見たい時は
`gpio readall`で見れる

状態を変更したい時は
`gpio -g mode write`等でgpioの読み込み/書き込み状態を変更したあと
`gpio -g write 1`等で電圧を変更出来る

### i2c
`sudo raspi-config`でi2cの利用を有効可出来る

`sudo i2cdetect -y 1`でモジュールが認識されているか確認出来る


## トラブルシューティング
### python実行時に問題があった場合
python3 python 両方で実行してみる。
両方エラーの場合は両方の実行結果のスクリーンショット

### i2cのセンサーで問題が起きたら
スクリーンショット
`sudo raspi-config` と再起動後に試してみてうまく行くかの確認
`sudo i2cdetect -y 1`の実行結果のスクリーンショット

### GPIOのセンサーで問題があった場合
gpio readallの結果のスクリーンショット







