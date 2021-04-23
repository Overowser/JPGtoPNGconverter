from sys import argv
import os
from PIL import Image

#grabbing the directory where we have the images to convert and where to put the converted images
to_convert = argv[1]
converted = argv[2]

#create the new directory where to put the converted images if it does not exist
if not os.path.exists(converted):
    os.mkdir(converted)

#looping through the images with the .jpg format in the pokedex file
for filename in os.listdir(to_convert):
    if filename.endswith(".jpg"):
        ima = Image.open(to_convert+"/"+filename)
        #this one works only in the case of jpg but it should be enough for this project
        filename = filename[:-4]+".png"
        #filename = os.path.splitext(filename)[0]
        ima.save(converted + "/" + filename, "png")
