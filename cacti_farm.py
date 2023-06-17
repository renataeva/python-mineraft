from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# ⭐ Задание №3
# В x, y и z выбираем координаты местонахождения песка
x = -867
y = 62
z = 616
sand_id = 12
block = mc.getBlock(x, y, z)
if block == sand_id:
    if mc.getBlock(x, y+1, z) == 0:
        # mc.postToChat('yes, it is air')
        mc.setBlocks(x, y+1, z, x, y+3, z, 81)
    else:
        mc.postToChat("no,it's not air")
elif block == 2:
    mc.setBlock(x, y + 1, z, 38)
else:
    mc.postToChat('not sand')
