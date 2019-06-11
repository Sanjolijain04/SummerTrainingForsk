# image processing using PIL

#import Image module from PIL library
from PIL import Image

#operations in image processing

#imput name of image
name=(input("Enter the name of image: ")+".jpg")

#open image
img=Image.open(name)

#greyscale
img.convert(mode='L').save("imaeprocess.jpg")
bw_img=Image.open("imaeprocess.jpg")

#rotate image by 90 degree
img_rotate=bw_img.transpose(Image.ROTATE_90)
img_rotate.save("imaeprocess.jpg")

#crop image from center
crop_img=img_rotate.crop(box=(50,50,160,204))
crop_img.save("imaeprocess.jpg")

#generate thumbnails
'''
crop_img.thumbnail((75,75)).save("imaeprocess.jpg")
thumb_img=Image.open("imaeprocess.jpg")
thumb_img.show()
'''

#print name of image

