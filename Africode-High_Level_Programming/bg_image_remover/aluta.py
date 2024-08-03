from rembg import remove
from PIL import Image

img_path= r'/home/nash/Documents/Africode-High_Level_Programming/naomi.jpeg'
img=Image.open(img_path)


r=remove(img)

output_path= r'/home/nash/Documents/Africode-High_Level_Programming/naomi.png'
r.save(output_path)