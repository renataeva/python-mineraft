from mcpi.minecraft import Minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import math
import time
mc = Minecraft.create()
mcdraw = MinecraftDrawing(mc)
def DistanceBetweenPoints(pos1, pos2):
    xd = pos2.x - pos1.x
    yd = pos2.y - pos1.y
    zd = pos2.z - pos1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

FAR_AWAY = 15
BlockMood = 'happy'
friend = mc.player.getTilePos()
friend.x = friend.x + 5
friend.y = mc.getHeight(friend.z, friend.z)
mc.setBlock(friend.z, friend.y, friend.z, block.DIAMOND_BLOCK.id)

while True:
    pos = mc.player.getTilePos()
    distance = DistanceBetweenPoints(pos, friend)
    if BlockMood == 'happy':
        if distance < FAR_AWAY:
            target = pos.clone()
        else:
            BlockMood = 'sad'
            mc.postToChat('<bot> Come back! I miss you')
    elif BlockMood == 'sad':
        if distance <= 5:
            BlockMood = 'happy'
            mc.postToChat('<bot> *im not goin to say anything cuz the tutorial was a tad cringe*')
    if friend != target:
        line = mcdraw.getLine(friend.x, friend.y, friend.z, target.x, target.y, target.z)
        for i in line[:-1]:
            mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
            friend = nextBlock.clone()
            friend.y = mc.getHeight(friend.x, friend.z)
            mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
            time.sleep(0.25)
        target = friend.clone()
    time.sleep(0.25)
