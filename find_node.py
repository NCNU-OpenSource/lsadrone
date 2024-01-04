import cv2
import mediapipe as mp

def should_draw_connection(i):
    if (0 <= i <= 10) or (17 <= i <= 22) or (29 <= i <= 32):
        return False
    else:
        return True
    
if __name__ == "__main__":
    # 讀取圖片
    for k in range(11, 18):
        img = cv2.imread(str(k) + '.jpg')
        img = cv2.resize(img, None, fx=0.7, fy=0.7)

        mpPose = mp.solutions.pose
        pose = mpPose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        mpDraw = mp.solutions.drawing_utils
        poseLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=3) # 點的顏色
        poseConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5) # 連線的顏色

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = pose.process(imgRGB)

        # print(result.pose_landmarks)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]

        my_points = {}

        if result.pose_landmarks:
            for i, lm in enumerate(result.pose_landmarks.landmark):
                xPos = int(lm.x * imgWidth)
                yPos = int(lm.y * imgHeight)

                if should_draw_connection(i):
                    cv2.circle(img, (xPos, yPos), 3, (0, 0, 255), -1) # 畫點
                    mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS, poseLmsStyle, poseConStyle) # 畫線
                    cv2.putText(img, str(i), (xPos-25, yPos+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2) # 畫座標
                    print(i, lm.x, lm.y)
                    my_points[i] = (lm.x, lm.y)
        print(my_points)

        cv2.imshow('img' + str(k), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()