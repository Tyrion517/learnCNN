import cv2
import numpy as np
import json5


def resize_crop_img(image_path: str, size: int = 28) -> np.ndarray:

    # size: the length of side of resized image
    # return (size, size, 1) np 3d array
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).astype('uint8')
    _, image = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    min_x_left_contour = min(contours, key=lambda x: cv2.boundingRect(x)[0])
    max_x_right_contour = max(contours, key=lambda x: cv2.boundingRect(x)[0] + cv2.boundingRect(x)[2])
    min_y_up_contour = min(contours, key=lambda x: cv2.boundingRect(x)[1])
    max_y_down_contour = max(contours, key=lambda x: cv2.boundingRect(x)[1] + cv2.boundingRect(x)[3])

    x_left = cv2.boundingRect(min_x_left_contour)[0]
    y_up = cv2.boundingRect(min_y_up_contour)[1]
    x_right = sum(cv2.boundingRect(max_x_right_contour)[::2])
    y_down = sum(cv2.boundingRect(max_y_down_contour)[1::2])

    cropped_image = image[y_up:y_down, x_left:x_right]

    resized_image = cv2.resize(cropped_image, (size, size)).reshape((size,size,1))

    return resized_image

def show_details(array):
    print(f'type(array): {type(array)}\nshape: {array.shape}\ndtype: {array.dtype}\n')

def decode_onehot(encoded_vector, feature_names):
    index_ = np.argmax(encoded_vector)
    return feature_names[index_]

