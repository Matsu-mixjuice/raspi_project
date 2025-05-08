from picamera2 import Picamera2, Preview
import time

# カメラインスタンス作成
picam2 = Picamera2()

# プレビュー設定（解像度など）
preview_config = picam2.create_preview_configuration(main={"size": (1280, 720)})
picam2.configure(preview_config)

# ここで "Preview.QTGL" を指定してプレビュー開始！
picam2.start_preview(Preview.QTGL)

# カメラ起動
picam2.start()

# ずっと表示
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# 停止処理
picam2.stop_preview()
picam2.stop()
