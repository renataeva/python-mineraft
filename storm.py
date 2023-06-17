from mcpi.minecraft import Minecraft
import mcpi.block as block

affirmative = ['o', 'yes', 'Yes', 'ofc', 'Yes!', 'why not', 'Why not?']
mc = Minecraft.create()

# a = input('''There is a storm coming.
# Do you want to hide somewhere? ''')
p = mc.player.getPos()
print(type(p))
x = int(p.x)
y = int(p.y)
z = int(p.z)


def build_house():
    mc.setBlocks(x, y-1, z, x+4, y+2, z+4, 49)
    mc.setBlocks(x+1, y, z+1, x+3, y+1, z+3, 0)
    # mc.setBlocks(x, y-1, z, x+4, y+2, z+4, 49)
    # mc.setBlocks(x+1, y, z+1, x+3, y+1, z+3, 0)
    # dx = 2
    # dy = 2
    # dz = 2
    # print(x, y, z)
    # mc.setBlocks(x+dx, y, z-dz, x-dx, y, z+dz, 95)
    # mc.setBlocks(x + dx-1, y, z - dz, x - dx, y, z + dz, 1)
def build_tree():
    print(x, y, z)
    mc.setBlocks(x-1, y+2, z, x-3, y+3, z+2, 18)
    mc.setBlocks(x-2, y+4, z, x-2, y+4, z+2, 18)
    mc.setBlocks(x-1, y+4, z+1, x-3, y+4, z+1, 18)
    mc.setBlock(x-2, y+5, z+1, 18)
    mc.setBlocks(x-2, y+3, z+1, x-2, y, z+1, 17)


build_house()

# if a in affirmative:
#     print('building house')
#     build_house()
# else:
#     print('planting tree')
#     build_tree()
