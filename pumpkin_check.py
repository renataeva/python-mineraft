# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# ppos = mc.getBlock(int(input()))
# elif ppos == 86 :
#     mc.postToChat('True')
# else :
#     mc.postToChat('False')
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# def check_block():
#     ppos = mc.getBlock(int(input('cords:')))
#     if ppos == 86:
#         mc.postToChat('True')
#     else:
#         mc.postToChat('False')
# check_block()
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# ⭐ Задание №1
# В x, y и z выбираем координаты местонахождения тыквы
x = -290
y = 66
z = 362
pumpkin_id = 86
block = mc.getBlock(x, y, z)
mc.postToChat(block == pumpkin_id)# Здесь будет True или False
