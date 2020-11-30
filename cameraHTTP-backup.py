
import picamera
import logging
import socketserver
from threading import Condition
from http import server
import os

import time
import threading
import io
from io import BytesIO
from PIL import Image, ImageFile

import motionSensor as motion
import database as db
import kikiMailService as mail

###--- code for video stream ---###

PAGE="""\
<html>
<head>
<img src="stream.mjpg" width="640" height="480" />
</head>
</html>
"""
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


###--- code for motion detection ---###

def sense(cam):
    while True:

        #   if motion is detected two consecutive times, action is taken
        if(motion.motionDetected(cam)):
            if(motion.motionDetected(cam)):
                print(">>   \033[92m0% Motion Detected!\033[0m")
                
                
                #   signal to database that motion has been detected
                db.motion_detected()
                
                
                #   capture pic for mail    #
                cam.capture('system_notice.jpg',use_video_port=True)
                time.sleep(15*60)
                print(">>  \033[92m40% taken image for mail\033[0m")
                
                
                #   send main to relavent users with picture and date
                mail.sendNotification(db.getDataForMail())
                
                
                #   time should be 60*60    #
                print(">>  \033[92m80% cooldown for 30 minutes\033[0m")
                #time.sleep(30*60)
                
                
                #   reset database and start listen for new motion
                db.motion_detectedRESET()


def camera_check(cam):
    db.camera_online()
    while True:
        time.sleep(2)
        try:
            cam._check_camera_open()
        except:
            db.camera_disconnected()
            os._exit(1)


###--- start all ---###

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    t1 = threading.Thread(target=sense, args=[camera])
    t2 = threading.Thread(target=camera_check, args=[camera])
    #t1.start()
    #t2.start()
    
    
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    
    
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    
    finally:
        camera.stop_recording()
    


