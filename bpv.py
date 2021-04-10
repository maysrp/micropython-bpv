import ujson as json
import ubinascii
import time
import framebuf
import gc

def showN(nu,display,x=86,y=64,sx=0,sy=0):
    data=bytearray(nu)
    fbuf = framebuf.FrameBuffer(data,x,y,framebuf.MONO_HLSB)
    display.blit(fbuf,sx,sy)
    display.show()
    gc.collect()


def pbm(files,oled,sx=0,sy=0,fills=True):
    if fills:
        oled.fill(0)
    with open(files,"rb") as f:
        f.readline()
        x,y=f.readline().decode("utf8").split()
        showN(f.read(),oled,int(x),int(y),sx,sy)
        
def play(files,display,sx=0,sy=0,qt=1):
    f=open(files,"rb")
    inf=f.readline()
    info=inf.decode()
    try:
        x,y,times,fps=json.loads(info)
    except Exception as e:
        print("Wrong File")
        return False
#     ce=time.ticks_ms()
    for i in range(times*fps):
        t=time.ticks_ms()
        c=f.readline()
        q=ubinascii.a2b_base64(c)
        showN(q,display,x,y,sx,sy)
        if i%10:
            time.sleep_ms(round(1000/fps)-time.ticks_ms()+t)
        else:
            time.sleep_ms(round(1000/fps)-time.ticks_ms()+t-qt)
#     print(time.ticks_ms()-ce)
    display.fill(0)
    display.show()
    return 'fin'

def plays(files,display,sx=0,sy=0,qt=0):
    f=open(files,"rb")
    inf=f.readline()
    info=inf.decode()
    try:
        x,y,times,fps=json.loads(info)
    except Exception as e:
        print("Wrong File")
        return False
    ce=time.ticks_ms()
    for i in range(times*fps):
        t=time.ticks_ms()
        c=f.readline()
        q=ubinascii.a2b_base64(c)
        showN(q,display,x,y,sx,sy)
        if i%10:
            time.sleep_ms(round(1000/fps)-time.ticks_ms()+t)
        else:
            time.sleep_ms(round(1000/fps)-time.ticks_ms()+t-qt)
    rec=time.ticks_ms()-ce
    print(rec)
    rex=(times*1000-rec)*10/(fps*times)
    print("QT:",rex)
    display.fill(0)
    display.show()
    return 'fin'
