from mcpi.minecraft import Minecraft
mc = Minecraft.create()
places = {
    'ravine' : (-662, 106, 296),
    'alliums' : (-707, 76, 236),
    'beacon' : (-624, 108, 433)
}

answer = ''

while answer != 'stop':
    answer = input('Where do you want to go? Write "stop" stop the program ')
    if answer in places:
        location = places[answer]
        x, y, z, = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
    elif answer != 'stop':
        print('ValueNotFound')
