#图片转字符画
#coding: UTF-8
#IJWTP: I Just Want To Play 'some video'
from rich import print
import sys,cv2,os,time
import numpy as np
def convert_bgr(img,dst):
        img=cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
        xy = np.where(img[:, :, 0] < 128, "1", "0") #1为黑，0为白
        with open(dst+".txt","w") as f:
                f.write("\n".join(["".join(row) for row in xy]))

srcdir=sys.argv[1]
dstdir=sys.argv[2]
total=len(os.listdir(srcdir))
filecount=0
lasttime=time.time()
starttime=time.time()
for file in os.listdir(srcdir):
    lasttime=time.time()
    convert_bgr(srcdir+file,dstdir+f"\\{file}")
    currenttime=time.time()
    print(f"[cyan]converted {file}[/cyan]:[yellow]{filecount}/{total}[/yellow]|[green]{round(currenttime-lasttime,2)}/{round((total-filecount)*(currenttime-lasttime),2)}[/green]    ",end="\r")
    filecount+=1
print(f"total time: {time.time()-starttime}")    

