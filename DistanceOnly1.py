import cv2
import time
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer
detector=HandDetector(detectionCon=0.5,maxHands=2)

cap=cv2.VideoCapture(0)
mixer.init()

b = []
count_x = 0
c = []
count_y = 0
finger_choice = 0
bbox_wanted = 600

# Arduino reading from the transmitter comes
# in the format of a 10 element pressure array where each element
# can be either 0, 1, 2, 3, or 4 where 0 means the finger is
# not pressed and 1-4 are the corresponding pressure values

def arduino_file():
    #file = open('test.txt', 'r')
    #x = file.read()
    #file.close() 
    #return x
    
    arduino_fingers = []

    with open('test1.txt', 'r') as file:
        for line in file:
            number = int(line.strip())
            arduino_fingers.append(number)
    print(f"arduino fingers: {arduino_fingers}")
    # return arduino fingers: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return arduino_fingers

def f2(dump, dump2):
    
    file = open('bbox_val1.txt', 'w')
    file.write(str(dump))
    file.write ("\n")
    file.write(str(dump2))
    file.close()
    #file.write(dump)
    #file.flush()


    
def obj_data_double(img):
    #print("double")
    bbox_x_1 = 0 
    bbox_x_2 = 0
    bbox_y_1 = 0 
    bbox_y_2 = 0
    bbox_1_have = False
    bbox_2_have = False
    
    hands,frame=detector.findHands(img)
    if hands:
        hands1=hands[0]
        bbox=hands1["bbox"]
        x,y,w,h=bbox
        bbox_x_1 = x
        bbox_y_1 = y
        bbox_1_have = True
        b.append([x,y])
        global count_x
        count_x = count_x + 1
        
        
    if len(hands)==2:
        hands2 = hands[1]
        bbox2=hands2["bbox"]
        x2,y2,w2,h2=bbox2
        bbox_x_2 = x2
        bbox_y_2 = y2
        bbox_2_have = True
        c.append([x2,y2])
        global count_y
        count_y = count_y + 1
       
    return bbox_x_1, bbox_x_2, bbox_y_1, bbox_y_2, bbox_1_have, bbox_2_have

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    finger_choice = arduino_file()
    

        
         
    bbox_x_1, bbox_x_2, bbox_y_1, bbox_y_2, bbox_1_have, bbox_2_have = obj_data_double(frame)
    if bbox_1_have:
        x1=b[count_x - 1][0]
        y1=b[count_x - 1][1]
        cv2.putText(frame, f"{bbox_x_1, bbox_y_1} ", (x1, y1),cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
         
    
    if bbox_2_have:
        x2=c[count_y - 1][0]
        y2=c[count_y - 1][1]
        cv2.putText(frame, f"{bbox_x_2, bbox_y_2} ", (x2, y2),cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    
   
    
    if (bbox_1_have and bbox_2_have):
        
    
        f2(bbox_x_1, bbox_x_2)
        
    else:
        
        f2(0,0)
    
    frame=cv2.imshow("FRAME",frame)
   
    if cv2.waitKey(1)&0xFF==27:
        break

cap.relase()
cv2.destroyAllWindows()