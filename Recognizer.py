import cv2
import keras

from utils import *


class Recognizer:
    def __init__(self, model_path, feature_path=None, size=28):
        # size: length of one side of images to recognize
        self.model = keras.models.load_model(model_path)
        self.size = size
        self.features = np.load(feature_path, allow_pickle=True)

    def recognize_matrix(self, matrix):
        # matrix: (size, size, 1) matrix representing image to recognize
        matrix.astype('uint8')
        if len(matrix.shape) == 4:
            pass
        elif len(matrix.shape) == 3:
            matrix = np.expand_dims(matrix, axis=0)
        elif len(matrix.shape) == 2:
            matrix = np.expand_dims(matrix, axis=0)
            matrix = np.expand_dims(matrix, axis=3)
        elif len(matrix.shape) == 1:
            matrix = matrix.reshape(-1, self.size, self.size, 1)
        else:
            raise Exception("Wrong shape")
        pre_vector = self.model.predict(matrix)[0]
        prediction = self.decode_one_hot(pre_vector)

        return prediction


    def recognize_image(self, image_path):
        # image: array returned by cv2.imread gray scale.
        image = resize_crop_img(image_path)
        prediction = self.recognize_matrix(image)
        # character = self.decode_one_hot(prediction)
        return prediction

    def decode_one_hot(self, pre_vector):
        character = decode_onehot(pre_vector, self.features)
        return character