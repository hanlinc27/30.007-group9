import serial

arduino_reading = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
finger_choice = ['0']*10
parsed=['0','0','0','0','0','0','0','0','0','0']

def write_to_file(dump):
   # file = open('test.txt', 'w')
   # file.write(str(dump))
   # print("hi")
   # file.close()
   
   # writes it to the file with a new line
   # for each of the fingers
    with open('test1.txt', 'w') as file:
        for line in dump:
            file.write(f"{line}\n")

    #file.write(dump)
    #file.flush()
    
while (1):

    test_reading = arduino_reading.readline()
    
    if len(test_reading) > 10:
        test_reading = test_reading.decode('utf-8', errors='replace')
        parsed=test_reading.split(",")
        parsed = [x.rstrip() for x in parsed]
        
        # write all the values to the file since
        # we might have multiple fingers
        print(f"parsed: {parsed}")
        write_to_file(parsed)
        finger_choice = parsed

def reading_arduino():
    return finger_choice


