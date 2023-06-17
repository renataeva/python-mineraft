from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
y = random.randint(80, 180)
mc.player.setPos(-554, y, 326)
