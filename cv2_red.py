import cv2
import urllib.request
import numpy as np
 
def nothing(x):
    pass
 
url='http://192.168.1.55/cam-lo.jpg'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
 
l_h, l_s, l_v = 0, 0, 0
u_h, u_s, u_v = 15, 255, 255
 
while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv, l_b, u_b)
 
    cnts, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 
    for c in cnts:
        area=cv2.contourArea(c)
        if area>2000:
            cv2.drawContours(frame,[c],-1,(255,0,0),3)
            M=cv2.moments(c)
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
 
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,"red",(cx-20, cy-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
        
    res = cv2.bitwise_and(frame, frame, mask=mask)
 
    cv2.imshow("live transmission", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
    
 
cv2.destroyAllWindows()
