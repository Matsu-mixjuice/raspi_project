from picamera2 import Picamera2
import cv2
import time
import numpy as np
import mediapipe as mp

# Mediapipe 初期化
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Picamera2 初期化
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (640, 480),"format":"RGB888"})
picam2.configure(video_config)
picam2.start()

# OpenCV ウィンドウ表示設定
cv2.namedWindow("FaceMesh", cv2.WINDOW_NORMAL)

try:
    while True:
        # カメラからフレーム取得（numpy配列）
        frame = picam2.capture_array()

        # Mediapipe用にRGB変換
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # フェイスメッシュ検出
        results = face_mesh.process(rgb_frame)

        # メッシュを描画
        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    image=frame,
                    landmark_list=landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles
                        .get_default_face_mesh_tesselation_style()
                )

        # 表示
        cv2.imshow("FaceMesh", frame)

        # ESCキーで終了
        if cv2.waitKey(1) & 0xFF == 27:
            break

except KeyboardInterrupt:
    pass

# 後処理
face_mesh.close()
cv2.destroyAllWindows()
picam2.stop()
