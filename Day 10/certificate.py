#import useful libraries
#Image= to create image object
#ImageDraw= creates a drawing context
#ImageFont= font of the text
from PIL import Image, ImageDraw, ImageFont

#create white background
img=Image.new('RGBA',(800,600), color='white')

#adding border in Image
layer=Image.new('RGBA',(img.width+20, img.height+20), (214,142,0))

#set background
layer.paste(img,(10,10))

#save background image
layer.save("mybg.png")

#open background image
bg_img=Image.open('mybg.png')

#initialize the drawing content with background image
draw=ImageDraw.Draw(bg_img)
#writing haeading i.e Cetificate of PArticipation

'''
Content of certificate
'''

#color
 #rgb values of color required
color='rgb(0,0,0)'


# select font
font=ImageFont.truetype('Chewy-Regular.ttf', size=60)
#starting position of the message
(x,y)= (70,30)
#message
message="Certification of Participation"
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)


# select font
font=ImageFont.truetype('Roboto-Regular.ttf', size=30)
#starting position of the message
(x,y)= (160,240)
message="This certificate is proudly presented to" 
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)


# select font
font=ImageFont.truetype('Roboto-Bold.ttf', size=50)
#starting position of the message
(x,y)= (250,280)
message= input("Enter your name: ") 
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)
(x,y)= (230,290)
message="_________________" 
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)

# select font
font=ImageFont.truetype('Roboto-Regular.ttf', size=30)
#starting position of the message
(x,y)= (50,3005)
#message
message="For attending a bootcamp on" 
#color
color='rgb(0,0,0)' #rgb values of color required
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)


# select font
font=ImageFont.truetype('Roboto-Bold.ttf', size=40)
#starting position of the message
(x,y)= (700,100)
#message
message=input("Enter the topic of Bootcamp attended: ")
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)


"""
add logo to certificate
"""
logo_img=Image.open('logo.png')
logo=logo_img.resize((220,140))
bg_img.paste(logo,(300,100), logo)

"""
add stamp to certificate
"""
stamp_img=Image.open('stamp.png')
stamp=stamp_img.resize((100,100))
bg_img.paste(stamp,(870,450), stamp)


# select font
font=ImageFont.truetype('Roboto-Regular.ttf', size=25)
#starting position of the message
(x,y)= (60,540)
#message
message="Signature:_____________" 
#color
color='rgb(0,0,0)' #rgb values of color required
#draw message on bg image
draw.text((x,y), message, fill=color, font=font)


"""
add sign to certificate
"""
sign_img=Image.open('sign.png')
sign=sign_img.resize((120,70))
bg_img.paste(sign,(170,480), sign)


bg_img.save('s.png')
