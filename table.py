from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

score = {}
answer = ''
while answer != 'stop':
    answer = input("What's your name? ")
    mc.postToChat('Go!')
    time.sleep(10)
    blocks = mc.events.pollBlockHits()
    blocks_length = len(blocks)
    score[answer] = 0
    name = answer
    if blocks_length > score[name]:
        score[name] = blocks_length
    mc.postToChat('Your score is ' + str(blocks_length))
print(score)
