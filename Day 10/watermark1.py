#add watermark to an image

from PIL import Image, ImageEnhance

#watermark function
def watermark(bg_img, mark_img, position, opacity):
    #check the value of opacity entered
    if(opacity<1):
        mark=reduce_opacity(mark_img, opacity)
    #check the mode of image 
    if(bg_img.mode != 'RGBA'):
        bg_img=bg_img.convert('RGBA')
    #create a transparent layer of size of bg image
    layer=Image.new('RGBA',bg_img.size, (0,0,0,0))
    
    # add watermark to that layer
    if(position=='tile'):
        
    
    
    

#open background image
bg_img=Image.open("anima.jpg")

#open watermark image
mark_img=Image.open("logo.png")

#call function to put watermark
watermark(bg_img, mark_img,tile, 0.3).show()


