import pandas as pd
from Recognizer import Recognizer


data = pd.read_csv('./input/chinese/train.csv')
y = data['character']
X = data.drop('character', axis=1)
X_3d = X.values.reshape(-1, 28, 28)
# cv2.imwrite(f'./image/{y[index]}.jpg', X_3d[index])


recognizer = Recognizer('./model/chinese-45.keras', './model/chinese-features-45.npy')

import random

index = random.randint(0, len(X_3d) - 1)

from matplotlib import pyplot as plt

plt.imshow(X_3d[index], cmap='gray')
print(recognizer.recognize_matrix(X_3d[index]), '\n')

print(recognizer.recognize_image('./image/万.jpg'))