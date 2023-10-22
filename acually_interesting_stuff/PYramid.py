from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def build_pyramid(base_len):
    x, y, z = mc.player.getTilePos()
    n = 0
    for i in range(base_len, 0, -2):
        xn = x-n
        zn = z+n
        mc.setBlocks(xn, y + n, zn,
                     xn - (i - 1), y + n, zn + (i - 1),
                     57)
        n += 1


side = int(input('Size of the base of the pyramid (in blocks, must be an odd number): '))

if side % 2 == 0:
    print('Odd number required')
    exit(1)
else:
    build_pyramid(side)
