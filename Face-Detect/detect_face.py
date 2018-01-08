from random import randint
import cv2
import glob
import os

CASCADE = "Face_cascade.xml"
FACE_CASCADE = cv2.CascadeClassifier(CASCADE)


def detect_faces(image_path):
    image = cv2.imread(image_path)
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(image_grey, scaleFactor=1.14, minNeighbors=5, minSize=(25, 25), flags=0)

    for x, y, w, h in faces:
        sub_img = image[y - 10:y + h + 10, x - 10:x + w + 10]
        os.chdir("Extracted")
        cv2.imwrite(str(randint(0, 10000)) + ".jpg", sub_img)
        os.chdir("../")
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 600, 600)
        cv2.imshow('image',image)
    if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
        cv2.destroyAllWindows()


all_images = glob.glob("./images/*.jpg")

for image in all_images:
    detect_faces(image)