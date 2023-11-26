# coding=utf-8
# 典孝急乐蚌批赢麻 勾勒刻板印象~
import sqlite3 as sql
import keyboard
import random
import pyperclip
db=sql.connect("神秘骂人库.db")
cursor=db.cursor()
curse_small=[]
curse_big=[]
RemoveOnCopied=False
if RemoveOnCopied: print("已开启单文本只复制一次功能!")
try:
    cursor.execute('select * from main')
    curses=cursor.fetchall()
    for curse in curses:
        if curse[2] == "min":
            curse_small.append(curse[1])
        else:
            curse_big.append(curse[1])
except Exception as f:
    print("Error:{}".format(f))
finally:
    cursor.close()
    db.close()
cursed=0
def getCurseBig():
    global cursed
    stc=random.choice(curse_big)
    if RemoveOnCopied: curse_big.remove(stc)
    pyperclip.copy(stc)
    cursed+=1
    print(f"高级: {stc}\n你骂了{cursed}句!\n")
def getCurseSmall():
   global cursed
   stc=random.choice(curse_small)
   if RemoveOnCopied: curse_small.remove(stc)
   pyperclip.copy(stc)
   cursed+=1
   print(f"普通: {stc}\n\r你骂了{cursed}句!\n\r")
print("骂人宝典,启动!")
while True:
    keyboard.add_hotkey("ctrl+o",getCurseBig,suppress=False)
    keyboard.add_hotkey("ctrl+p",getCurseSmall,suppress=False)
    keyboard.wait()
