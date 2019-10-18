import numpy as np 
import cv2,os 

x = os.path.dirname(os.path.abspath(__file__)) + r'\GestureSamples\Sample1.webm'
cap = cv2.VideoCapture(x) 
fgbg = cv2.createBackgroundSubtractorMOG2() 
  
while(1):
    try:
        ret, frame = cap.read() 
  
        fgmask = fgbg.apply(frame)

        bluR = cv2.blur(fgmask,(5,5))

        edges = cv2.Canny(bluR,10,10)
   
        cv2.imshow('fgmask', frame) 
        cv2.imshow('frame', fgmask)
        cv2.imshow('blur',bluR)
        cv2.imshow('boundary',edges)
      
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            break
        
    except Exception:
        cap.release() 
        cv2.destroyAllWindows() 
        break
      
  
cap.release() 
cv2.destroyAllWindows() 
