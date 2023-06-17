import string

passive_mobs = ['pig',
                'sheep',
                'villager',
                'cow',
                'chicken',
                'rabbit']
tameable_mobs = ['wolf',
                 'horse',
                 'donkey']
agressive_mobs = ['creeper',
                  'zombie',
                  'skeleton',
                  'spider']


def sanitise(word: str) -> str:
    ws = []
    chars_skip = string.punctuation + string.whitespace
    for c in word:
        if c not in chars_skip:
            ws.append(c)
    return ''.join(ws)


words = input('What do you see? ').split()

for n in words:
    ns = sanitise(n)
    if ns in passive_mobs:
        print('Everything is safe.')
        exit()
    elif ns in tameable_mobs:
        print('Quick, tame it!')
        exit()
    elif ns in agressive_mobs:
        print('Watch out!')
        exit()

print('Nothing to worry about.')
