import os

import cv2
import numpy as np
from detector import run_detection

if __name__ == '__main__':
    detected_objects = run_detection('./test-images/sejour.jpg')
    print("NUM CLASSES DETECTED", len(detected_objects))
    print(detected_objects.keys())
    for k in detected_objects:
        print(len(detected_objects[k]))

    for class_name in detected_objects:
        images = detected_objects[class_name]
        for image in images:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
