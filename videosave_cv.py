import numpy as np
import cv2
import time

# Define the duration (in seconds) of the video capture here
capture_duration = 10

exit = 0

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# *'h264' -> H264 Format or *'hvc1' -> H265 Format
# libde265 and ffmpeg libraries have to be configured properly for H265

# fourcc = cv2.VideoWriter_fourcc(*'h264')
fourcc = cv2.VideoWriter_fourcc(*'hvc1')

while (exit == 0):

    # System time
    start_time = time.time()

    # local time for file naming
    start_time_local = time.localtime()


    str_time = time.strftime('%Y-%m-%d %H-%M-%S', start_time_local)
    str_time += ".mov"

    # print(str_time)

    out = cv2.VideoWriter(str_time, fourcc, 20.0, (640,480), True)


    while( int(time.time() - start_time) < capture_duration ):
        ret, frame = cap.read()
        if ret==True:
			# If the camera placed downside
            # frame = cv2.flip(frame,0)

            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exit = 1
                break
        else:
            break

    out.release()


# Release everything if job is finished
cap.release()

cv2.destroyAllWindows()
