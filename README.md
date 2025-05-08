# raspi_project
Raspberry Piとカメラモジュールを使って、いろんなことをしてみよう。  
使うもの：  
・Raspberry Pi 5  
・AI camera  
## raspberry piを動かす環境の作り方  
1. パッケージ情報を最新にする。  
    `sudo apt update`
2. uvをインストールして、ターミナルを一度消してから3へ。
3. PyQtをインストール  
    `sudo apt install python3-pip`  
    `sudo apt install qtbase5-dev`  
    `sudo apt install python3-pyqt5`  
4. 仮想環境を作る  
    `uv venv 名前 --system-site-packages --python3.11`
5. 仮装環境に入る(memo　仮想環境から出たい時は`deactivate`)
6. カメラ系のモジュールのインストール  
    `sudo apt install imx500-all`  
※必要があれば、`uv pip install モジュール名`でその都度インストールする。
## ライブストリーム
