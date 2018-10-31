'''
 This program code saves captured video 
 with H265 codec. 
'''
# https://stackoverflow.com/questions/38686359/opencv-videowriter-control-bitrate

# import packages
from PIL import Image

from subprocess import Popen, PIPE

import imutils
from imutils.video import VideoStream
from imutils.object_detection import non_max_suppression
from imutils import paths

import cv2
import numpy as np


# ffmpeg setup
p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'libx265', '-qscale', '5', '-r', '24', 'video.mov'], stdin=PIPE)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if ret:
                    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        im = Image.fromarray(frame)
        
        # Send JPEG formatted image through PIPE to encoder
        im.save(p.stdin, 'JPEG')
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit = 1
            break       
    else:
        break

p.stdin.close()
p.wait()
video.release()
cv2.destroyAllWindows()
