from rich import print as rich_print
import ctypes
#from line_profiler import LineProfiler
import os,sys,time,threading,sys,simpleaudio
#sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
print_as_rich=False
max_fps=1/90
class COORD(ctypes.Structure):
	 _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)] 
	 def __init__(self,x,y):
		 self.X = x
		 self.Y = y
def reset():
    STD_OUTPUT_HANDLE= -11
    hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    INIT_POS=COORD(0,0)
    ctypes.windll.kernel32.SetConsoleCursorPosition(hOut,INIT_POS)
files=os.listdir(sys.argv[1])
files.sort(key=lambda x:int(x.split('.')[0]))
counts=len(files)
def load(folder,files):
    caches=[]
    for temp in files:
        with open(folder+temp,"r") as f:
            caches.append(f.read())
    return caches
def play(frames,bgm):
    os.system("cls")
    count=0
    wave_obj = simpleaudio.WaveObject.from_wave_file(bgm)
    wave_obj.play()
    for frame in frames:
        lasttime=time.time()
        time.sleep(max_fps)
        if print_as_rich:rich_print("[white]"+frame+"[/white]\n",flush=True)
        else:print(frame,flush=True)
        sys.stdout.flush()
        if print_as_rich:
            rich_print(f"\n[cyan]{count} / {counts}[/cyan]|[yellow]{round(1/(time.time()-lasttime),2)} FPS[/yellow]",flush=True)
        else:
            print(f"\n{count} / {counts}|{round((time.time()-lasttime),2)} SPF",flush=True)
        sys.stdout.flush()
        count+=1
        reset()
cache=load(sys.argv[1],files)
play(cache,sys.argv[2])
rich_print("Finished!")
