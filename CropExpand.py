import numpy as np
import math
import os
import sys
import random
from PIL import Image

os.chdir("test123")
currentDir = os.getcwd()
allPics = os.listdir(currentDir)
for i in allPics:
	if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"):
		img = Image.open(i)
		imgw = img.width
		imgh = img.height
		img2 = img.crop((0,0,900,1188))
		img3 = img.crop((100,132,1000,1320))
		img2 = img2.resize((178,218))
		img3 = img3.resize((178,218))
		img2.save("cropBR_" + i)
		img3.save("cropTL_" + i)


