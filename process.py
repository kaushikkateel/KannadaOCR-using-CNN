import segmentation
import predictor
import sequencer
import os

directory = "./seg_img/"

resDict = dict()

def processor(file):

	segmentation.segment(file)

	for filename in os.listdir(directory):
 
		 imagepath = os.path.join(directory, filename)

		 # print(imagepath)

		 res, imageName = predictor.predict(imagepath)

		 resDict[imageName] = res

		 sequencer.sequence(resDict)



		 # file = open("text.txt","a")
		 # file.write(res)
		 # file.close()







    