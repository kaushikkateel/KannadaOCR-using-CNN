import segmentation
import predictor
import sequencer
import os
import shutil



directory = "./seg_img/"

def removeFiles():

	for filename in os.listdir(directory):
	    file_path = os.path.join(directory, filename)
	    try:
	        if os.path.isfile(file_path) or os.path.islink(file_path):
	            os.unlink(file_path)
	        elif os.path.isdir(file_path):
	            shutil.rmtree(file_path)
	    except Exception as e:
	        print('Failed to delete %s. Reason: %s' % (file_path, e))

resDict = dict()

def processor(file):

	removeFiles()

	segmentation.segment(file)

	for filename in os.listdir(directory):
 
		 imagepath = os.path.join(directory, filename)

		 # print(imagepath)

		 res, imageName = predictor.predict(imagepath)

		 resDict[imageName] = res

	char = sequencer.sequence(resDict)


	return char
		 # file = open("text.txt","a")
		 # file.write(res)
		 # file.close()





    