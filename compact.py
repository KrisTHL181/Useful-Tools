#将图片缩放至控制台大小
#coding: UTF-8
from rich import print
from PIL import Image
import sys,os,time
# 获取图片宽高
def compact(img,dst):
    image = Image.open(img)
    width, height = image.size
    # 字符画宽
    new_width = os.get_terminal_size().columns
    # 字符画高
    new_height = os.get_terminal_size().lines
    # 对原始图片进行比例压缩
    image = image.resize((new_width, int(new_height)))
    # 图片转为灰度图
    image = image.convert('L')
    image.save(dst)
srcdir=sys.argv[1]
dstdir=sys.argv[2]
total=len(os.listdir(srcdir))
filecount=0
lasttime=time.time()
starttime=time.time()
for file in os.listdir(srcdir):
    lasttime=time.time()
    compact(srcdir+file,dstdir+f"\\{file}")
    currenttime=time.time()
    print(f"[cyan]converted {file}[/cyan]:[yellow]{filecount}/{total}[/yellow]|[green]{round(currenttime-lasttime,2)}/{round((total-filecount)*(currenttime-lasttime),2)}[/green]    ",end="\r")
    filecount+=1
print(f"total time: {time.time()-starttime}")    
#format: converted 文件名:已转换/未转换|转换一次所需时长/预估总时长
