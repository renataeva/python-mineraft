from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
# pos = mc.player.getTilePos()
# x, y, z, = pos.x, pos.y, pos.z
while True:
    pos = mc.player.getTilePos()
    x, y, z, = pos.x, pos.y, pos.z
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)
    mc.player.setPos(x, y, z)
    time.sleep(0.01)
