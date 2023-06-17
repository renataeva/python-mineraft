from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
import  random
x = -276
y = 66
z = 334
# defining the height
height = random.randint(4, 100)
# erasing before building
mc.setBlocks(x-2, y, z-2, x+2, y+100, z+2, block.AIR.id)
# building
mc.postToChat(height)
mc.setBlocks(x, y, z, x, y+height, z, block.GOLD_BLOCK.id)
mc.setBlocks(x-1, y, z-1, x+1, y+height/2, z+1, block.GOLD_BLOCK.id)
mc.setBlocks(x-2, y, z-2, x+2, y+height/4, z+2, block.GOLD_BLOCK.id)
