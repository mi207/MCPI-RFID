#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

skin=['ironman','default','batman','pig']
skinNames=['Iron Man', 'Herobrine', 'Batman']
idx=1;
winSizeX=1800
winSizeY=800

mc = minecraft.Minecraft.create()

continue_reading = True

UIDs=['160,41,83,122','144,24,1,118','176,221,21,124']
#UIDs=['0,20,197,128','0,13,25,131','44,23,219,171']

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
i=0;
# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
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
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        uid_str=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]);

        try:
            idx=UIDs.index(uid_str)
            os.system('cp //home/pi/mcpi/data/images/mob/skins/'+ skin[idx]+'.png //home/pi/mcpi/data/images/mob/char.png')
            mc.postToChat('Skin changed to: '+skinNames[idx]+'!')
            i=i+1;
            os.system("xdotool search --name 'Minecraft - PI'  windowsize " + str(winSizeX)+ ' ' +str(winSizeY+i%2))
            #os.system("xdotool search --name 'Minecraft - PI'  windowsize " + str(winSizeX)+ ' ' +str(winSizeY))

            
            #break
        except ValueError:
            print("Oops! Not in the list")
        
    
##        # This is the default key for authentication
##        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
##        
##        # Select the scanned tag
##        MIFAREReader.MFRC522_SelectTag(uid)
##
##        # Authenticate
##        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
##
##        # Check if authenticated
##        if status == MIFAREReader.MI_OK:
##            MIFAREReader.MFRC522_Read(8)
##            MIFAREReader.MFRC522_StopCrypto1()
##        else:
##            print "Authentication error"

        #print "finished"


