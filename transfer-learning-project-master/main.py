import base64
import glob
import uuid
import cv2
from flask import Flask, render_template
from objectDetector.detector import run_detection
from websearch.scrap import run
import os

WORK_DIR = 'static'  # 'workDir'
WORK_DIR_PERSIST = 'workDirPersist'
app = Flask(__name__)


def create_work_dirs():
    if not os.path.exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    if not os.path.exists(WORK_DIR_PERSIST):
        os.mkdir(WORK_DIR_PERSIST)


def save_image(image_array):
    cv2.imwrite('/'.join([WORK_DIR_PERSIST, uuid.uuid1().__str__()]) + '.jpg', image_array)
    cv2.imwrite('/'.join([WORK_DIR, uuid.uuid1().__str__()]) + '.jpg', image_array)


def save_detected_images(detected_images: list):
    if detected_images.__len__().__eq__(0):
        return False
    create_work_dirs()
    for image_array in detected_images:
        save_image(image_array)
    return True


def search_on_google_shopping():
    similar_products = {}
    images = glob.glob(WORK_DIR + '/*')
    for image in images:
        similar_products[image] = run(image)
    return similar_products


@app.route("/search")
def search_request():
    detected_objects = run_detection('test-images/chaise.jpg')
    if detected_objects is not None and detected_objects.__len__().__ge__(1):
        if save_detected_images(detected_objects):
            data = search_on_google_shopping()
            temp = render_template('template.html', data=data)
            return temp
    else:
        return []


if __name__ == '__main__':
    app.run()
