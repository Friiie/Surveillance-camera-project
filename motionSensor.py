import io
from io import BytesIO
from PIL import Image, ImageFile
import picamera
import time

threshhold = 10
sensitivity = 75

    
def getImData(cam):
    stream = io.BytesIO()
    cam.capture(stream, format='bmp', resize='100x75', use_video_port=True)
    stream.seek(0)
    pic = Image.open(stream)
    buffer = pic.load()
    return buffer


def motionDetected(cam):
    changedPixels = 0
    time.sleep(0.3)
    im1 = getImData(cam)
    time.sleep(0.3)
    im2 = getImData(cam)
    
    for x in range(100):
        for y in range(75):
            pixdiff = abs(im1[x,y][1] - im2[x,y][1])
            if (pixdiff > 10):
                changedPixels += 1
    
    if changedPixels > sensitivity:
        return True
    else:
        return False
