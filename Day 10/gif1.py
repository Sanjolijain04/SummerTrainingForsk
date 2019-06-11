#gif of a moving ball

#create image with ball
#ball_x=x coordinate of ball
#ball_y= y coordinate of ball
def create_image_with_ball(width,height,ball_x,ball_y,ball_size):
    #create background
    bg_img=Image.new('RGBA',(width,height),(255,255,255))
    #initialioze background image as drawing object
    draw=ImageDraw.Draw(bg_img)
    
    # now we will draw ball on the background image
    #we will use ellipse() function for that
    #ellipse take four values in a tuple
    #ellipse((x0,y0,x1,y1), fill) where x0=initial x, y0=initial y, x1=x +size of ball, y1=y+size of ball
    draw.ellipse((ball_x, ball_y, ball_x+ball_size, ball_y+ball_size), fill='blue')
    
    return bg_img
    

from PIL import Image, ImageDraw
#make a list of frames
frames=[]
#make initial position of ball
x,y=0,0
#loop for frames i.e in this gif 10 frames will be there
for i in range(10):
    #generate a frame
    new_frame=create_image_with_ball(400,400,x,y,40)
    #append the new fraem into list
    frames.append(new_frame)
    #increment in x and y by 40 i.e size of ball
    x+=40
    y+=40
    

#save gif file such that it loops forever
frames[0].save('my_gif1.gif', format='GIF',append_images=frames[1:], save_all=True, duration=10, loop=0)



