from mcpi.minecraft import Minecraft
import mcpi.block as block
"""
This is a multi-line
comment of my code.
"""
mc = Minecraft.create()

# Materials
M_AIR = (block.AIR.id, 0)
M_PLANKS_OAK = (block.WOOD_PLANKS.id, 0)
M_LOG_OAK = (block.WOOD.id, 0)
M_LOG_OAK_NS = (block.WOOD.id, 8)
M_LOG_OAK_WE = (block.WOOD.id, 4)
M_ANDESIDE_SMOOTH = (block.STONE.id, 6)
M_TORCH = (block.TORCH.id, 1)
M_GLASS = (block.GLASS.id, 0)

# Coordinates
wall_height = 3

Y_BASE = 75
Y_WALL_TOP = Y_BASE + wall_height - 1
Y_ROOF = Y_WALL_TOP + 1


def clear_box(x_from, z_from, y_from, x_to, z_to, y_to):
    mc.setBlocks(x_from, y_from, z_from, x_to, y_to, z_to, *M_AIR)


def build_house(x, y, z):
    x_from = -564
    z_from = 322

    x_to = -571
    z_to = 329

    # clear
    clear_box(x_from, z_from, Y_BASE, x_to, z_to, Y_ROOF)

    # north wall
    mc.setBlocks(-564, Y_BASE, 322, -571, Y_WALL_TOP, 322, *M_PLANKS_OAK)
    # north-west pillar
    mc.setBlocks(-571, Y_BASE, 322, -571, Y_ROOF, 322, *M_LOG_OAK)
    # north-east pillar
    mc.setBlocks(-564, Y_BASE, 322, -564, Y_ROOF, 322, *M_LOG_OAK)
    # south wall
    mc.setBlocks(-564, Y_BASE, 329, -571, Y_WALL_TOP, 329, *M_PLANKS_OAK)
    # south-west pillar
    mc.setBlocks(-571, Y_BASE, 329, -571, Y_ROOF, 329, *M_LOG_OAK)
    # south-east pillar
    mc.setBlocks(-564, Y_BASE, 329, -564, Y_ROOF, 329, *M_LOG_OAK)
    # east wall
    mc.setBlocks(-564, Y_BASE, 328, -564, Y_WALL_TOP, 323, *M_PLANKS_OAK)
    # west wall
    mc.setBlocks(-571, Y_BASE, 328, -571, Y_WALL_TOP, 323, *M_PLANKS_OAK)
    # floor
    mc.setBlocks(-564, 74, 328, -570, 74, 323, *M_ANDESIDE_SMOOTH)
    # door frame
    mc.setBlocks(-564, Y_BASE, 326, -564, 76, 325, *M_AIR)
    # roof
    mc.setBlocks(-570, Y_ROOF, 323, -565, Y_ROOF, 328, *M_PLANKS_OAK)
    # west pilon
    mc.setBlocks(-571, Y_ROOF, 323, -571, Y_ROOF, 328, *M_LOG_OAK_NS)
    # east pilon
    mc.setBlocks(-564, Y_ROOF, 323, -564, Y_ROOF, 328, *M_LOG_OAK_NS)
    # south pilon
    mc.setBlocks(-570, Y_ROOF, 329, -565, Y_ROOF, 329, *M_LOG_OAK_WE)
    # north pilon
    mc.setBlocks(-570, Y_ROOF, 322, -565, Y_ROOF, 322, *M_LOG_OAK_WE)
    # placing torches
    mc.setBlock(-570, Y_WALL_TOP, 323, *M_TORCH)
    mc.setBlock(-570, Y_WALL_TOP, 328, *M_TORCH)
    # placing north window
    mc.setBlocks(-566, 76, 322, -569, 76, 322, *M_GLASS)
    # placing south window
    mc.setBlocks(-566, 76, 329, -569, 76, 329, *M_GLASS)



#
# # clear
# mc.setBlocks(-564, Y_BASE, 322, -571, Y_ROOF, 329, *M_AIR)
#
# # north wall
# mc.setBlocks(-564, Y_BASE, 322, -571, Y_WALL_TOP, 322, *M_PLANKS_OAK)
# # north-west pillar
# mc.setBlocks(-571, Y_BASE, 322, -571, Y_ROOF, 322, *M_LOG_OAK)
# # north-east pillar
# mc.setBlocks(-564, Y_BASE, 322, -564, Y_ROOF, 322, *M_LOG_OAK)
# # south wall
# mc.setBlocks(-564, Y_BASE, 329, -571, Y_WALL_TOP, 329, *M_PLANKS_OAK)
# # south-west pillar
# mc.setBlocks(-571, Y_BASE, 329, -571, Y_ROOF, 329, *M_LOG_OAK)
# # south-east pillar
# mc.setBlocks(-564, Y_BASE, 329, -564, Y_ROOF, 329, *M_LOG_OAK)
# # east wall
# mc.setBlocks(-564, Y_BASE, 328, -564, Y_WALL_TOP, 323, *M_PLANKS_OAK)
# # west wall
# mc.setBlocks(-571, Y_BASE, 328, -571, Y_WALL_TOP, 323, *M_PLANKS_OAK)
# # floor
# mc.setBlocks(-564, 74, 328, -570, 74, 323, *M_ANDESIDE_SMOOTH)
# # door frame
# mc.setBlocks(-564, Y_BASE, 326, -564, 76, 325, *M_AIR)
# # roof
# mc.setBlocks(-570, Y_ROOF, 323, -565, Y_ROOF, 328, *M_PLANKS_OAK)
# # west pilon
# mc.setBlocks(-571, Y_ROOF, 323, -571, Y_ROOF, 328, *M_LOG_OAK_NS)
# # east pilon
# mc.setBlocks(-564, Y_ROOF, 323, -564, Y_ROOF, 328, *M_LOG_OAK_NS)
# # south pilon
# mc.setBlocks(-570, Y_ROOF, 329, -565, Y_ROOF, 329, *M_LOG_OAK_WE)
# # north pilon
# mc.setBlocks(-570, Y_ROOF, 322, -565, Y_ROOF, 322, *M_LOG_OAK_WE)
# # placing torches
# mc.setBlock(-570, Y_WALL_TOP, 323, *M_TORCH)
# mc.setBlock(-570, Y_WALL_TOP, 328, *M_TORCH)
# # placing north window
# mc.setBlocks(-566, 76, 322, -569, 76, 322, *M_GLASS)
# # placing south window
# mc.setBlocks(-566, 76, 329, -569, 76, 329, *M_GLASS)
