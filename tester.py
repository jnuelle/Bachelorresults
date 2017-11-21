from scipy import misc
import glob
import random
import numpy as np



mask = misc.imread('/home/green/Bachelorthesis/Results/fullmask.png')

for direc in [1000, 2000, 4000, 11999]:
	
	globalPath = "/home/green/Bachelorthesis/Results/run%d_day/test_images/test*.png" % (direc)

	meanRaw = 0
	meanRel = 0
	maxRaw = 0
	maxRel = 0
	minRaw = 1
	minRel = 1
	arrayRaw = "rawArray = [ "
	arrayRel = "relArray = [ "

	for image_path in glob.glob(globalPath):
	
		counter = 0
		matchRaw = 0
		matchRel = 0
		image = misc.imread(image_path)		
	
		for x, y in np.nditer([image, mask]):
		
			if y > 0:
				counter += 1
				if x > 10:
					matchRaw += 1
					matchRel += 1
			elif x > 10:
				matchRel -= 1


		resultRaw = matchRaw/counter
		resultRel = matchRel/counter

		if resultRaw > maxRaw:
			maxRaw = resultRaw

		if resultRaw < minRaw:
			minRaw = resultRaw

		if resultRel > maxRel:
			maxRel = resultRel

		if resultRel < minRel:
			minRel = resultRel

		meanRaw += resultRaw
		meanRel += resultRel
		arrayRaw = "%s, %2.4f" % (arrayRaw, resultRaw)		
		arrayRel = "%s, %2.4f" % (arrayRel, resultRel)


	meanRaw = meanRaw/20
	meanRel = meanRel/20

	start = "run%d : \n" % direc
	arrayRaw = "%s]\n" % arrayRaw		
	arrayRel = "%s]\n" % arrayRel
	line1 = "mean: %2.4f	%2.4f\n" % (meanRaw, meanRel)
	line2 = "max: %2.4f 	%2.4f \n" % (maxRaw, maxRel)
	line3 = "min: %2.4f 	%2.4f \n" % (minRaw, minRel)
	with open("day.txt", "a") as myfile:
		myfile.write(start)
		myfile.write(arrayRaw)
		myfile.write(arrayRel)
		myfile.write(line1)
		myfile.write(line2)
		myfile.write(line3)
		myfile.write("\n")
