from mcpi.minecraft import Minecraft, CmdPlayer
mc = Minecraft.create()
player: CmdPlayer = mc.player


class Location(object):
    # Class constructor.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def print_x(self):
    #     print(f'x: {self.x}')
    #
    # def print_y(self):
    #     print(f'y: {self.y}')
    #
    # def print_z(self):
    #     print(f'z: {self.z}')
    #
    # def print_all(self):
    #     self.print_x()
    #     self.print_y()
    #     self.print_z()


stairs = Location(-563, 88, 366)
house = Location(-561, 75, 325)
ravine = Location(-663, 78, 297)
river = Location(-648, 83, 233)
pyramid = Location(-566, 119, 263)


def move_to(location):
    player.setTilePos(location.x, location.y, location.z)


while True:
    a = input('''   Teleportation menu:
To go to the stairs, type 1;
To go to the house, type 2;
To go to the ravine, type 3;
To go to the floating river, type 4;
To go to the green pyramid, type 5;
To stop the program, type stop.
''')
    if a == '1':
        move_to(stairs)
    elif a == '2':
        move_to(house)
    elif a == '3':
        move_to(ravine)
    elif a == '4':
        move_to(river)
    elif a == '5':
        move_to(pyramid)
    elif a == 'stop':
        exit()
    else:
        print(f'Invalid input, please try again.\n')
        continue
