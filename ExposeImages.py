import numpy as np
import math
import os
import sys
import random
from PIL import Image
#from skimage import data, exposure, img_as_float


def exposeImg(file):
    image = Image.open(file)
    fileExt  = file.split(".")[-1]
    fileName = file.split(".")[-2]


    expose  = Image.new("RGB",(image.width, image.height))
    expose2 = Image.new("RGB",(image.width, image.height))
    exposeLVL  = round(random.uniform(1.2,2),2)
    exposeLVL2 = round(random.uniform(1.2,2),2)


    #try to recover image by just multiplying
    rec = Image.new("RGB",(image.width, image.height))

    for w in range(0, image.width):
        for h in range(0, image.height):
            r,g,b = image.getpixel((w,h))

            r2 = math.ceil(r * exposeLVL)
            g2 = math.ceil(g * exposeLVL)
            b2 = math.ceil(b * exposeLVL)

            if r2 > 255:
                r2 = 255
            if g2 > 255:
                g2 = 255
            if b2 > 255:
                b2 = 255
            expose.putpixel((w, h), (r2, g2, b2))

            r3 = math.ceil(r * exposeLVL2)
            g3 = math.ceil(g * exposeLVL2)
            b3 = math.ceil(b * exposeLVL2)
            if r3 > 255: 
                r3 = 255
            if g3 > 255:
                g3 = 255
            if b3 > 255:
                b3 = 255
            expose2.putpixel((w, h), (r3, g3, b3))


    newName = fileName + "_explvl." + str(exposeLVL) + "." + fileExt
    newName2 = fileName + "_explvl." + str(exposeLVL2) + "." + fileExt

    os.chdir("../")
    wd = os.getcwd()
    expose.save(wd + "/OverExpose/" + newName)
    expose2.save(wd + "/OverExpose/" + newName2)

    
def allPics(dirName):
    if not os.path.exists("OverExpose"):
        os.makedirs("OverExpose")
    # if not os.path.exists("exposelvl2"):
    #     os.makedirs("exposelvl2")

    os.chdir(os.getcwd() + "/" + dirName)
    currentDir = os.getcwd()
    filelist=os.listdir(currentDir)
    for fichier in filelist[:]:
        if not(fichier.endswith(".png") or fichier.endswith(".jpg") or fichier.endswith(".jpeg")):
            filelist.remove(fichier)
    
    savewd = os.getcwd()
    for f in filelist[:]:
        os.chdir(savewd)
        print("doing " + f)
        exposeImg(f)

currentDir = os.getcwd()
allCont = os.listdir(currentDir)
allDir = []
for f in allCont:
    if os.path.isdir(f):
        allDir.append(f)

if sys.argv[1] not in allCont:
    print("Not valid directory")
else: 
    allPics(sys.argv[1])
