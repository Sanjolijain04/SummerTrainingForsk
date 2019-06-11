# generate id card for the students of Forsk summer developer program 2019

from PIL import Image, ImageDraw, ImageFont

def create_background():
    bg_img=Image.new('RGBA',(380,450), (255,255,255))
#    profile=Image.open('profile.jpg')
#    profile.resize((50,50))
#    bg_img.paste(profile,(10,10))
    return bg_img
    
    
create_background()
bg_img.show()

