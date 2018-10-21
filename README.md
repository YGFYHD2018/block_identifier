# python版 ブロック認識への取り組み

## 背景

Maker Faire Tokyo 2018では、ブロック認識プログラムはC++で実装されたものを使用していた。しかし当日の環境による影響でブロック認識率が悪くなってしまった。  
ひとつの改善策として、カメラをマニュアルモードにして環境による変化を受けないようにすることを検討した。カメラをマニュアルで使用するためにはPython版のカメラライブラリが必要となるため、C++のコードをPythonへ移植することとした。

## 構成

本プログラムは、GOフレームワークと連携して稼働します。  
https://github.com/YGFYHD2018/3d_led_cube_go

## 環境構築

* SDカードイメージ  
2018-04-18-raspbian-stretch.zip
* SSH有効  
sshという名称の空ファイルを作る
* sshアクセス  
ラズパイをイーサネットケーブルでPCと同じネットワークに接続する(DHCPサーバー必要)  
ラズパイを起動する  
１分後くらいにPCのターミナルからsshアクセスする  
`ssh pi@raspberrypi.local`  
パスワードは`raspberry`
* コンフィグ設定  
コンフィグ画面起動  
`sudo raspi-config`  
（以下設定後、自動的に再起動）
  * パスワード変更（to 警告消す）  
1 Change Your Password  
`root` を入力
  * ホスト名変更  
2 Network Options  
N1 Hostname  
`block-identifier` を入力
  * カメラ有効（注：カメラ繋がないと起動しなくなる）  
5 Interfacing Options  
P1 Camera  
<Yes>

* 再びsshでアクセス（ホスト名、パスワードが変更されている）  
`ssh pi@block-identifier.local`
* apt-getアップデート（時間かかる）  
`sudo apt-get update`  
`sudo apt-get upgrade`
* vimインストール  
`sudo apt-get install vim`
* FTP有効（PCとファイル交換するのに便利）  
http://yamaryu0508.hatenablog.com/entry/2014/12/02/102648
* リモートデスクトップ有効  
`sudo apt-get install xrdp`
* pythonのライブラリをインストール  
`sudo apt-get install libopencv-dev python-opencv python-dev python-picamera`
* 本プログラム取得  
`git clone https://github.com/hiroshi-mikuriya/block_identifier`
* 自動起動設定  
`sudo vim /etc/rc.local`  
以下、追記  
`cd /home/pi/block_identifier`  
`python pi_main.py`
* GOフレームワークインストール  
[3d_led_cube_go](https://github.com/YGFYHD2018/3d_led_cube_go)のインストール手順を実施する。

## リンク

* [効果音ラボ](https://soundeffect-lab.info)  
音声ファイルを使用させていただいております。

## よく使うコマンド等

### SDカードバックアップ手順（Mac用）

SDカードをMacに挿す。  
ドライブ番号を調べる。  
/Volumes/boot が /dev/dusk4s1なので/dev/disk4がSDカードである。

```
$ df
Filesystem    512-blocks       Used Available Capacity iused               ifree %iused  Mounted on
/dev/disk4s1       86872      44839     42033    52%       0                   0  100%   /Volumes/boot
```

バックアップを実行する。  
１時間弱所要する。

```
$ sudo dd if=/dev/disk4 | gzip > backup`date +%Y%m%d`.img.gz
```

### SDカード書き込み手順（Mac用）

Etcherというツールを使う。（無料）  
上記でバックアップしたファイルと、書き込み先のSDカードを指定して実行する。  
30分程度所要する。