import RPi.GPIO as GPIO
import MFRC522
import signal
import mcpi.minecraft as minecraft
import time,os

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

#Replace skin file names here
skinFile=['ironman','default','batman','pig'] 
skinNames=['Iron Man', 'Herobrine', 'Batman']
idx=1;
winSizeX=1800 #set minecraft window size 
winSizeY=800

#create minecraft connection
mc = minecraft.Minecraft.create()

continue_reading = True
#Replace the card IDs here
UIDs=['160,41,83,122','144,24,1,118','176,221,21,124']

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
i=0;

print "Press Ctrl-C to stop."

# This loop keeps checking for cards. 
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID        
        print "Card UID: "+str(uid[0])+","+str(uid[1])+","+\
        str(uid[2])+","+str(uid[3])
        uid_str=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]);

        try:
            idx=UIDs.index(uid_str)
            os.system('cp skins/'+ skinFile[idx]
                      +'.png //home/pi/mcpi/data/images/mob/char.png')
            mc.postToChat('Skin changed to: '+skinNames[idx]+'!')
            i=i+1;
            os.system("xdotool search --name 'Minecraft - PI'  windowsize "
                      + str(winSizeX)+ ' ' +str(winSizeY+i%2))          
        except ValueError:
            print("Oops! Not in the list")
