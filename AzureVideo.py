#%%html
from IPython.core.display import HTML
print('<h2>Hello ss</h1>')
#%%
#import requests
#from IPython import display
vid_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/Intro.mp4'

#response = requests.get(vid_url)
##%%
#display.Video(vid_url, autoplay=True)
##display.HTML("<video width='320' height='240' controls><source src='" +
##vid_url + "' type='video/mp4'></video>")
##display.Audio('https://github.com/sayadrameez/AI-Introduction/raw/master/files/RainSpain.wav',
##autoplay=True)
#!curl
#https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/RainSpain.wav
#-o RainSpain.wav
import requests
#display.Audio('RainSpain.wav', autoplay=True)
import numpy as np
import cv2
print(np.__path__)
# Open a sample video available in sample-videos
vcap = cv2.VideoCapture(vid_url)
#if not vcap.isOpened():
#    print "File Cannot be Opened"
while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")

#import curl
#import av
from PIL import Image,ImageDraw
import requests
#container = av.open()
#with open("/Users/rameezahmed.sayad/Desktop/sample.mp4", 'wb') as f:
response = requests.get(vid_url)
if response.status_code == 200:
    with open("sample.mp4", 'wb') as f:
        f.write(response.content)

import av
container = av.open("sample.mp4")

from matplotlib import pyplot

for frame in container.decode(video=0):
    if(frame.index == 25):
        img = frame.to_image()
        pyplot.imshow(img)
        pyplot.show()
  
frameCount = frame.index - 1

print(str(frameCount) + " frames")

