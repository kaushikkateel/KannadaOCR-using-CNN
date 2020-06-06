import tensorflow as tf
from tensorflow import keras
import os
import cv2
import numpy as np
import keras
from tensorflow.keras.models import load_model


def predict(img):

	image = img
	model = load_model("./cnn/final_proj_05-06-2020(try1).h5")

	test = cv2.imread(img)

	# img = cv2.resize(test,(150,150))

	# img = np.reshape(img,[1,150,150,3])
	img = cv2.resize(test,(128,128))

	img = np.reshape(img,[1,128,128,3])

	a = np.argmax(model.predict(img))

	class_names = np.array(['ಅ','ಆ','ಇ','ಈ','ಉ','ಊ','ಋ','ಎ','ಏ','ಐ','ಒ','ಓ','ಔ','ಕ','ಖ','ಗ','ಘ','ಙ','ಚ','ಛ','ಜ','ಝ','ಞ'])

	result = str(class_names[a])
	res = result.encode("utf-8")

	basefilename = os.path.basename(image)
	imageName = os.path.splitext(basefilename)[0]


	return result , imageName

# res,i = predict("./seg_img/01-02-01-0.png")
# #print(res.decode('utf-8'))
# file = open("text.txt","wb")
# result = res.encode("utf-8")
# # print(result.type())
# file.write(result)
# file.close()
# print(i)