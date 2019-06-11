import requests

url="http://forsk.in/images/Forsk_logo_bw.png"
source=requests.get(url)
source.content
f = open("new_img.png","wb")
f.write(source.content)
f.close()

#nethod 2
from PIL import Image
from io import BytesIO

img = Image.open(BytesIO(source.content))
img.save("my_new_img.png")

