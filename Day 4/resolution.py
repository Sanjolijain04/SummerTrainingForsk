# resolution 

image_name="sample1.jpg"
def find_resolution(image_name):
    with open(image_name, mode='rb') as read_img:
        read_img.seek(163)
        a=read_img.read(2)
        height=(a[0]<<8)+a[1]
        a=read_img.read(2)
        width=(a[0]<<8)+a[1]
        print("Resolution of image is {} * {}".format(width, height))
        
find_resolution(image_name)