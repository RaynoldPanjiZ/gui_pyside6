from PySide6.QtCore import QThread, QObject, Signal
from PySide6.QtGui import QPixmap, QIcon

import cv2
import numpy as np
import time
import os


## https://github.com/cundi/Python-PySide-PyQt-Tutorial/blob/master/Pyside_PyQt_%E7%BA%BF%E7%A8%8B/PySide%20Signals%20and%20Slots%20with%20QThread%20example.md
class MySignal(QObject):
    sig = Signal(np.ndarray, int)

class VideoStream(QThread):
    frame_update = MySignal()  
    
    def __init__(self, url, camera_id):
        super().__init__()
        self.url = url
        self.channel = camera_id
        self.started = True
        self.current_frame = None
        self.screen_available = True

        self.frames_to_count=24

    def run(self):
        # self.screen_available = screen_available
        vid = cv2.VideoCapture(self.url)
        fps=0
        cnt=0
        st = 0
        print('Loop :', vid.isOpened())
        if vid.isOpened():
            while self.started:
            
                # QtWidgets.QApplication.processEvents()	
                _, image = vid.read()

                if cnt == self.frames_to_count:
                    # print(self.frames_to_count/(time.time()-st),'FPS') 
                    fps = round(self.frames_to_count/(time.time()-st)) 
                    st = time.time()
                    cnt=0
                cnt+=1

                image = cv2.putText(image, f"{fps} fps", 
                    (50,100), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                self.frame_update.sig.emit(image, self.channel)

                # key = cv2.waitKey(1) & 0xFF
                if self.started==False:
                    print('Loop break')
                    break
        vid.release()

    def stop(self, camera_id):
        if self.channel == camera_id is not None:
            if self.isRunning():
                self.started = False
                time.sleep(1)
                self.terminate()
                print("camera", camera_id, "stopped")
            else:
                print("camera", camera_id, "already stoped!!")
        else:
            print("camera", camera_id, "not running!!")