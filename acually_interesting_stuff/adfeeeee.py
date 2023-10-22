from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

mc.setBlock(pos.x + 1, pos.y, pos.z, 54, 2)
