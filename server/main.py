import os
from PIL import Image
import json
import binascii
import base64

def qx(f):
    with open(f,"rb") as f:
        f.readline()
        f.readline()
        qxc=f.read()
    return base64.b64encode(qxc)

def image(f,x,y):
    name=f[0:-3]+".pbm"
    fx=Image.open(f)
    fb=fx.convert('1')
    fb=fb.resize((x,y))
    fb.save(name)   
    e=qx(name)
    os.remove(f)
    os.remove(name)
    return e

def convert(files,times=60,fps=10,x=128,y=64):
    bpv=files[0:files.rindex(".")]+".bpv"
    q=open(bpv,'wb')
    cx=json.dumps([x,y,times,fps])
    q.write(bytes(cx,encoding="utf8")+b'\n')
    for i in range(times*fps):
        ffmpeg="ffmpeg -ss %s  -i %s -f image2 -y %s" % (i/fps,files,str(i)+".jpg")
        os.system(ffmpeg)
        file_name=str(i)+".jpg"
        lk=image(file_name,x,y)
        q.write(lk+b"\n")
        print(i)
    q.close()

def pbm(files,x=128,y=64):
    pbmfile=files[0:files.rindex(".")]+".pbm"
    c=Image.open(files)
    l=c.convert('1')
    d=l.resize((x,y))
    d.save(pbmfile)
# convert("a.mp4",80,10,128,64)
#convert为视频转bpv pbm 为图片转pbm
pbm("a.jpg",86,64)
