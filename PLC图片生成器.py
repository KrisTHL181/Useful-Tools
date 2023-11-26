from PIL import Image as image
from PIL import ImageDraw, ImageFont
from sys import argv
'''name=input("姓名:")
gender=input("性别(男/女):")
birth=input("出生日期(yyyy年mm月dd日):")
id_number=input("身份证号码(18位):")
address=input("户口地址:")
photo=input("大头照路径:")'''
#print("参数:\n1:名字\n2:性别\n3:生日\n4:身份证号\n5:地址\n6:照片")
name=argv[1]
gender=argv[2]
birth=argv[3]
id_number=argv[4]
address=argv[5]
photo=argv[6]
def generate(name,gender,birth,id_number,address,photo):
    #START-写入头部
    img = image.new('RGB', (1280, 980), 'white')
    plc_head = image.open("PLC头部.jpg")
    img.paste(plc_head.copy(), (0,0)) #粘贴头部
    #END-写入
    #START-写入大头照
    head=image.open(photo)
    img.paste(head.copy().resize((388,438),image.LANCZOS),(25,450))
    #END-写入大头照
    #START-写入信息
    font=ImageFont.truetype(font="方正黑体.ttf",size=50)
    draw=ImageDraw.Draw(img)
    draw.text((500,350),"姓名",fill=(0,51,102),font=font)
    draw.text((500,420),"性别",fill=(0,51,102),font=font)
    draw.text((500,490),"出生日期",fill=(0,51,102),font=font)
    draw.text((500,560),"身份证号码",fill=(0,51,102),font=font)
    draw.text((500,700),"户口地址",fill=(0,51,102),font=font)
    draw.text((610,350),name,fill=(0,0,0),font=font)
    draw.text((610,420),gender,fill=(0,0,0),font=font)
    draw.text((720,490),birth,fill=(0,0,0),font=font)
    draw.text((500,630),id_number,fill=(0,0,0),font=font)
    draw.text((500,770),address,fill=(0,0,0),font=font)
    #END-写入信息
    img.save(f"{name}.png")

generate(name,gender,birth,id_number,address,photo)
