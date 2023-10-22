from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def start(playerName, winAttempt):
    mc.postToChat(f"""Let's start the game! GLHF, {playerName}. You have {winAttempt} attempts to win.""")


# playerName = mc.entity.getName(3197)

start('atanerave', 7)
