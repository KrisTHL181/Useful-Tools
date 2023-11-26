#coding: UTF-8
from rich import print
import sys,cv2,os,time
import numpy as np
def threshold(src,dst):
    image=cv2.imread(src)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ##要二值化图像，必须先将图像转为灰度图
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(dst,binary)
srcdir=sys.argv[1]
dstdir=sys.argv[2]
total=len(os.listdir(srcdir))
filecount=0
lasttime=time.time()
starttime=time.time()
for file in os.listdir(srcdir):
    lasttime=time.time()
    threshold(srcdir+file,dstdir+f"\\{file}")
    currenttime=time.time()
    print(f"[cyan]converted {file}[/cyan]:[yellow]{filecount}/{total}[/yellow]|[green]{round(currenttime-lasttime,2)}/{round((total-filecount)*(currenttime-lasttime),2)}[/green]    ",end="\r")
    filecount+=1
print(f"\ntotal time: {time.time()-starttime}")
#format: converted 文件名:已转换/未转换|转换一次所需时长/预估总时长
