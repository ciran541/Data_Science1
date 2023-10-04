import os
import cv2
import time

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

webcam_index = 0
cap = cv2.VideoCapture(webcam_index)

for class_num in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(class_num))):
        os.makedirs(os.path.join(DATA_DIR, str(class_num)))

    print(f'Collecting data for class {class_num}')

    input('Press Enter when you are ready to start capturing images.')

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(class_num), f'{counter}.jpg'), frame)

        counter += 1

    print(f'Class {class_num} data collection complete.')

    time.sleep(5)

cap.release()
cv2.destroyAllWindows()

