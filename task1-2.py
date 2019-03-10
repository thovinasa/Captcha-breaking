from PIL import ImageFont, ImageDraw, Image
txt=raw_input("enter text: ")
     
image = Image.new('RGB', (500, 500), color = (73, 109, 137))
fontsize = 1  # starting font size

# portion of image width you want text width to be
img_fraction = 0.5

font = ImageFont.truetype('/home/kalifa/Desktop/Project2019/open-sans/OpenSans-Regular.ttf', fontsize)
while font.getsize(txt)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype('/home/kalifa/Desktop/Project2019/open-sans/OpenSans-Regular.ttf', fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
print fontsize
#font = ImageFont.truetype('/home/kalifa/Desktop/Project2019/open-sans/OpenSans-Regular.ttf',fontsize)
draw = ImageDraw.Draw(image)
draw.text((10,10), txt,font = ImageFont.truetype('/home/kalifa/Desktop/Project2019/open-sans/OpenSans-Regular.ttf',fontsize), fill=(255,255,0)) # put the text on the image
image.save('txt2.png')
