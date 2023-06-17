from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
p = mc.player.getTilePos()
blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
barBlock = 48
count = 0
while count <= len(blocks):
    blocks.insert(count, barBlock)
    mc.setBlock(p.x, p.y, p.z, blocks[0])
    mc.setBlock(p.x, p.y + 1, p.z, blocks[1])
    mc.setBlock(p.x, p.y + 2, p.z, blocks[2])
    mc.setBlock(p.x, p.y + 3, p.z, blocks[3])
    mc.setBlock(p.x, p.y + 4, p.z, blocks[4])
    mc.setBlock(p.x, p.y + 5, p.z, blocks[5])
    mc.setBlock(p.x, p.y + 6, p.z, blocks[6])
    mc.setBlock(p.x, p.y + 7, p.z, blocks[7])
    mc.setBlock(p.x, p.y + 8, p.z, blocks[8])
    mc.setBlock(p.x, p.y + 9, p.z, blocks[9])
    count += 1
    time.sleep(2)
