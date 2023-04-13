from pygame import mixer
import time

mixer.init()
# set ten channels for each finger's sound
# https://stackoverflow.com/questions/38028970/how-to-assign-sounds-to-channels-in-pygame
mixer.set_num_channels(10)
bbox_wanted = 605

def bbox_val():
    count = 0
    a = 0
    b = 0
    file = open('bbox_val1.txt', 'r')
    x = file.readlines()
    
    for line in x:
        if count == 0:
            a = line
        else:
            b = line
        count = count + 1
        
    file.close()
    return a,b
    #file.write(dump)
    #file.flush()


def arduino_file():
    finger = -1
    with open('test1.txt', 'r') as file:
        for index,line in enumerate(file):
            line = int(line)
            if (line > 0):
                finger = index
                break
    return finger
    #file.write(dump)
    #file.flush()

while(1):
    bbox_x_1, bbox_x_2 = bbox_val()
    bbox_x_1 = int(bbox_x_1)
    bbox_x_2 = int(bbox_x_2)
    finger_choice = arduino_file()
    print(finger_choice)
    
    if (bbox_x_1 != 0 and bbox_x_2 != 0 ):
        if finger_choice == 0:
            bbox_wanted = bbox_x_2 - 40
        elif finger_choice == 1:
            bbox_wanted = bbox_x_2 - 20
        elif finger_choice == 2:
            bbox_wanted = bbox_x_2
        elif finger_choice == 3:
            bbox_wanted = bbox_x_2 + 20
        elif finger_choice == 4:
            bbox_wanted = bbox_x_2 + 40
        elif finger_choice == 5:
            bbox_wanted = bbox_x_1 - 40
        elif finger_choice == 6:
            bbox_wanted = bbox_x_1 - 20
        elif finger_choice == 7:
            bbox_wanted = bbox_x_1 
        elif finger_choice == 8:
            bbox_wanted = bbox_x_1 + 20
        elif finger_choice == 9:
            bbox_wanted = bbox_x_1 + 40
        elif finger_choice == -1:
            bbox_wanted = 605
        
        print(bbox_wanted)
    
    if (bbox_wanted < 600):
        if (bbox_wanted >= 50 and bbox_wanted < 70):
            mixer.music.load('./piano-mp3/C1.mp3')
            print("play C1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 70 and bbox_wanted < 90):
            mixer.music.load('./piano-mp3/D1.mp3')
            print("play D1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 90 and bbox_wanted < 110):
            mixer.music.load('./piano-mp3/E1.mp3')
            print("play E1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 110 and bbox_wanted < 130):
            mixer.music.load('./piano-mp3/F1.mp3')
            print("play F1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 130 and bbox_wanted < 150):
            mixer.music.load('./piano-mp3/G1.mp3')
            print("play G1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 150 and bbox_wanted < 170):
            mixer.music.load('./piano-mp3/A1.mp3')
            print("play A1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 170 and bbox_wanted < 190):
            mixer.music.load('./piano-mp3/B1.mp3')
            print("play B1")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 190 and bbox_wanted < 210):
            mixer.music.load('./piano-mp3/C2.mp3')
            print("play C2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 210 and bbox_wanted < 230):
            mixer.music.load('./piano-mp3/D2.mp3')
            print("play D2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 230 and bbox_wanted < 250):
            mixer.music.load('./piano-mp3/E2.mp3')
            print("play E2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 250 and bbox_wanted < 270):
            mixer.music.load('./piano-mp3/F2.mp3')
            print("play F2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 270 and bbox_wanted < 290):
            mixer.music.load('./piano-mp3/G2.mp3')
            print("play G2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 290 and bbox_wanted < 310):
            mixer.music.load('./piano-mp3/A2.mp3')
            print("play A2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 310 and bbox_wanted < 330):
            mixer.music.load('./piano-mp3/B2.mp3')
            print("play B2")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 330 and bbox_wanted < 350):
            mixer.music.load('./piano-mp3/C3.mp3')
            print("play C3")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 350 and bbox_wanted < 370):
            mixer.music.load('./piano-mp3/D3.mp3')
            print("play D3")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 370 and bbox_wanted < 390):
            mixer.music.load('./piano-mp3/E3.mp3')
            print("play E3")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 390 and bbox_wanted < 410):
            mixer.music.load('./piano-mp3/F3.mp3')
            print("play F3")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 410 and bbox_wanted < 430):
            mixer.music.load('./piano-mp3/G3.mp3')
            print("play G3")
            mixer.music.play()
            time.sleep(1)
        elif (bbox_wanted >= 430 and bbox_wanted < 450):
            mixer.music.load('./piano-mp3/A3.mp3')
            print("play A3")
            mixer.music.play()
            time.sleep(1)
    else:
        print("music stop")
        mixer.music.stop()
    
    

