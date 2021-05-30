import cv2
import os
from statistics import mean
def heart_beat(video):
    user_video=video


    cap = cv2.VideoCapture(user_video)
    i = 0
    while (cap.isOpened()):
        flag, frame = cap.read()

        if flag == False:
            break
        cv2.imwrite("heart" + str(i) + ".jpg", frame)
        i = i + 1


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    cap = cv2.VideoCapture( user_video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = round(cap.get(cv2.CAP_PROP_FPS))
    red = []
    for i in range(0, length - 1, fps):
        img1 = cv2.imread('heart' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
        b, g, r = (img1[300, 300])
        red.append(r)

    for i in range(0, length):
        os.remove('heart' + str(i) + '.jpg')


    inten = mean(red)
    heartbeat = ((inten * fps) / 60) - 30
    heartbeat=str(heartbeat)
    return heartbeat