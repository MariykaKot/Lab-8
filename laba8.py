import cv2
import time
import numpy as np

def zq():
    image=cv2.imread("variant-9.jpg")
    height, width=imape.shape[:2]
    for i in range(1, 5):
        reduce_image=cv2.resixe(image, None, fx=1/i, fy=1/i, interpolation=cv2.INTER_AREA)
        reduced_height, reduced_width=reduce_image.shape[:2]
        x_offset=0
        y_offset=0

        image[y_offset:y_offset+reduced_height, x_offset:x_offset+reduced_width]=reduce_image

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindow()

def z2_3():
    cap=cv2.VideoCapture(0)
    down_points=(640, 480)
    i=0
    while True:
        ret, frame=cap.read()
        if not ret:
            break
        frame=cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        glay=cv2.cvtColor(frame, cv2.COLOR_DGR2GRAY)
        glay=cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh=cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours)>0:
            c=max(contours, key=cv2.contourArea)
            x, y, w, h=cv2.boundingRect(c)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if i % 5 == 0:
                    sredn_koordinata = np.sqrt([x1+x2/2, (y1+y2/2)])
                    print('Средняя координата равна: ', sredn_koordinata)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()
    v2.waitKey(0)
    cv2.destroyAllWindows()

