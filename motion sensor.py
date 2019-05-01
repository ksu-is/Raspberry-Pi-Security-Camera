from gpiozero import MotionSensor
from time import sleep 

pir = MotionSensor(4)


while True:
    
    pir.wait_for_motion()
    print ("Alert!") 
    print ("Alert!")
    print ("Motion Detected")
    print ("")
    print ("Sensor Restart")
    print ("")
    print ("Sensor Active")
    print ("------------------")
    sleep(7)



    