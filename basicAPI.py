import mcpi.minecraft as minecraft



import mcpi.block as block

import time

import os

skin=['default','batman','ironman','pig']
idx=1;

os.system('cp //home/pi/mcpi/data/images/mob/skins/'+ skin[idx]+'.png //home/pi/mcpi/data/images/mob/char.png')



mc = minecraft.Minecraft.create()


mc.postToChat("Hello Minecraft World")

#w   time.sleep(5)

#mc.camera.setFixed()
mc.camera.setNormal();
mc.camera.setPos(20,20,20);
mc.restoreCheckpoint()
#mc.camera.setFollow()
mc.setBlock(mc.player.getPos(),10)
            
        
