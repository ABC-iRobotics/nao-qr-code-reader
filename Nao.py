# Import naoqi is for communication with nao API
from naoqi import ALProxy
import time

# Robot IP, change if your Nao IP different
ROBOT_IP = "192.168.1.105"

# NaoApi
barcode=ALProxy("ALBarcodeReader", ROBOT_IP, 9559)
memory=ALProxy("ALMemory", ROBOT_IP, 9559)

# Query last data from ALMemory hundred times
for i in range(100):
  data = memory.getData("BarcodeReader/BarcodeDetected")
  time.sleep(1)
  # If is for only use data if has same value
  if len(data) != 0:
    barcode = str(data[0])
    # Need to split otherwise the robot will say the cordinates too.
    robotsay = barcode.split(" [")
    output = robotsay[0]
    print(output)
    # Need to be string to the AltextToSpeech API could work
    output = str(output[2:len(output)])
    tss = ALProxy("ALTextToSpeech", ROBOT_IP, 9559)
    tss.say(output)

