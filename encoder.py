from PIL import Image
import json

max_line_length = 0
input_txt = ""
line_amount = 0
current_x = 0
current_y = 0

def color_correct(color:str):
    return "0x"+color.replace("0x","")[::-1]

with open("./translations.json","r") as translator:
    guide = dict(json.loads(translator.read()))
with open("./input.txt","r") as inputfile:
    input_txt = inputfile.read().upper()
with open("./input.txt","r") as inputfile:
    line_amount = len(inputfile.readlines())
with open("./input.txt","r") as inputfile:
    for line in inputfile.readlines():
        currentlen = len(line.replace("\n",""))
        if currentlen > max_line_length:
            max_line_length = currentlen

img = Image.new("RGB",(max_line_length*2,(line_amount*7)-2))

for char in input_txt:
    if char in guide.keys():
        for i in range(5):
            img.putpixel((current_x, current_y + i), int(color_correct(guide[char][i]), base=16))
    else:
        if char == " ":
            current_x = current_x + 1
            continue
        elif char == "\n":
            current_y = current_y + 7
            current_x = 0
            continue
        else:
            for i in range(5):
                img.putpixel((current_x, current_y + i), int("0xFFFFFF", base=16))
    current_x = current_x + 2

img.save("./output.png")
img.close()

input("Done! Saved as output.png\nPress enter to exit.")
