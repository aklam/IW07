import numpy as np
import math
import os
from PIL import Image
from skimage import data, exposure, img_as_float


def exposeImg(file):
    image = Image.open(file)
    fileExt  = file.split(".")[-1]
    fileName = file.split(".")[-2]


    expose  = Image.new("RGB",(image.width, image.height))
    expose2 = Image.new("RGB",(image.width, image.height))
    exposeLVL  = 1.6
    exposeLVL2 = 2

    for w in range(0, image.width):
        for h in range(0, image.height):
            r,g,b = image.getpixel((w,h))
            r2 = math.ceil(r * exposeLVL)
            g2 = math.ceil(g * exposeLVL)
            b2 = math.ceil(b * exposeLVL)
            expose.putpixel((w, h), (r2, g2, b2))

            r3 = math.ceil(r * exposeLVL2)
            g3 = math.ceil(g * exposeLVL2)
            b3 = math.ceil(b * exposeLVL2)
            expose2.putpixel((w, h), (r3, g3, b3))

    newName = fileName + "_explvl_" + str(exposeLVL) + "." + fileExt
    newName2 = fileName + "_explvl_" + str(exposeLVL2) + "." + fileExt

    os.chdir("../")
    wd = os.getcwd()
    expose.save(wd + "/exposelvl1/" + newName)
    expose2.save(wd + "/exposelvl2/" + newName2)

#def gammaCor():
#    obama = Image.open('Obama.jpg')
#    image = img_as_float(data.moon())
#    gamma_corrected = exposure.adjust_gamma(image, 1)
#    print (image.mean() > gamma_corrected.mean())

#exposeImg('Obama.jpg')
os.chdir(os.getcwd() + "/groundTruth")
currentDir = os.getcwd()
filelist=os.listdir(currentDir)
for fichier in filelist[:]:
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)

savewd = os.getcwd()
for f in filelist[:]:
    os.chdir(savewd)
    print("doing " + f)
    exposeImg(f)


