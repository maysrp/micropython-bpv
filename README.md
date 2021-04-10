# micropython-bpv
micropython oled play video or  show PBM picture


## 使用 

micropython 测试通过OK设备：
+ esp8266
+ esp32
+ raspberrypi pico

### 视频播放

上传转码好的bpv视频文件

```
from bpv import pbm,play,plays
i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
oled=SSD1306_I2C(128,64,i2c)

play("a.bpv",oled)


```

### 图片显示

上传你要显示的PBM图片

```
from bpv import pbm,play,plays
i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
oled=SSD1306_I2C(128,64,i2c)

pbm("f.pbm",oled)
pbm("f.pbm",oled,0,0)
#以上两个显示效果等价
#显示f.pbm在（0，0）坐标处开始显示，显示时默认清屏
pbm("f.pbm",oled,64,0,0)
#显示f.pbm在（64，0）坐标处开始显示，不清屏显示


```





## 创建BPV视频

PIP 安装pillow
```
pip install pillow
```

在PC上安装好ffmpeg 
使用sever文件夹中的main.py

```

#在文件最后添加 


convert("a.mp4",80,10,128,64)

#参数： 视频  时长 帧率  x轴  y轴 （分辨率128x64）
```



## 创建PBM文件

PIP 安装pillow
```
pip install pillow
```

原始代码
```
from PIL import Image

c=Image.open("a.jpg")
c=c.convert('1')
c=c.resize((128,64))
c.save("a.pbm")
```

使用sever文件夹中的main.py

```

#在文件最后添加

pbm("a.jpg",128,64)
```

