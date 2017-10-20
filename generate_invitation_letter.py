"""Author Yichen Gong"""
"""2016 TCFA Name Card"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=3850x2975 at 0x101382EF0>
imageIdx = [[(365,220) , (1220,870)] , 
            [(365 + 3850/2, 220) , (1220 + 3850/2, 870)] , 
            [(365, 220 + 2975/2) , (1220, 870 + 2975/2)], 
            [(365 + 3850/2, 220 + 2975/2), (1220 + 3850/2, 870 + 2975/2+1)]]
img = Image.open("2016Dinnerinvitation.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Apple Chancery.ttf", 50)
color = (39,6,116)
f = open("dinner_list_2.txt",'r')
count = 0
line = f.readline().rstrip()

while(line):
    name = " ".join(line.split())
    draw.text(imageIdx[count%4][0],name,color,font=font)
    line = f.readline().rstrip()
    count += 1
    if(count%4==0 and count!=0):
        img.save("invitation_letters/dinner" + str(count) + "_2.png")
        img.close()
        img = Image.open("2016Dinnerinvitation.png")
        draw = ImageDraw.Draw(img)

    
    # draw.text(imageIdx[i%4][1], "6", color, font=font)
if(count%4!=0):
    img.save("invitation_letters/dinner" + str(count) + "_2.png")
    img.close()