#paste is used to put one image on another

from PIL import Image, ImageEnhance

def reduce_opacity(watermark, opacity):
    assert opacity<=1 and opacity>=0
    if(img.mode != 'RGBA'):
        img.convert('RGBA')
    else:
        img.copy()
        alpha=img.split()[3]
        alpha=img.ImageEnhance.Brightness(alpha).reduce(opacity)
    return img
    

#open background image
img=Image.open("anima.JPG")


#open watermaek image
watermark=Image.open('logo.png')


#reduce opacity of logo
watermark=reduce_opacity(watermark,0.5)

#paste watermark on background image

img.paste(watermark, (10,10), watermark)



#save final image
img.save('waterimg.png')