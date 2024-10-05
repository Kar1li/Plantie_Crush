import random, time

numbers = (48, 49, 50, 51, 52, 53, 54, 55, 56, 57)
E = []
template = {'cost': 0, 'atk': 0, 'hp': 0, 'cd': 0, 'element': ' ', 'hikari': 0, 'straight': 0, 'tp': 0,
            'elementAttach': E.copy(), 'moved': 0, 'silent': 0}
gameData = [
    [
        template.copy() for j in range(10)
    ] for i in range(5)
]
remove = []
color = ('\033[42m', '\033[41m', '\033[45m', '\033[43m', '')

hole = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
valid = [0]
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
cost = [10]
Round = [0]
Victory = [0]
requirement = [0, 0, 0, 0]
gameData = [
    [
        template.copy() for j in range(10)
    ] for i in range(5)
]


def clearGlobal():
    global hole
    global valid
    global board
    global cost
    global Round
    global gameData
    global requirement
    global Victory
    hole = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    valid = [0]
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    cost = [10]
    Round = [0]
    Victory = [0]
    requirement = [0, 0, 0, 0]
    gameData = [
        [
            template.copy() for j in range(10)
        ] for i in range(5)
    ]



clearGlobal()


def print_board():
    print('\n' * 1145)
    print('Costs:', cost, 'Round', Round)
    board_element = []
    board_hp = []
    for i in range(len(board)):
        x = []
        y = []
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                if hole[i][j] == '+':
                    x.append('  + ')
                else:
                    x.append('    ')
                y.append('    ')
            elif board[i][j] in plants:
                dec = f'{color[elements.index(gameData[i][j]["element"])]}' + ' ' + '\033[0m'
                x.append(dec + f'{board[i][j]}' + dec)
                y.append(f' {i}{j} ')

            else:
                x.append(f'{color[elements.index(gameData[i][j]["element"])] + board[i][j]}' + '\033[0m' + '  ')
                y.append(f'{gameData[i][j]["hp"]:<2}' + '  ')
        board_element.append(x)
        board_hp.append(y)
    for i in range(len(board)):
        # print('  ', '   '.join(hole[i]))
        print(' ', '  '.join(board_hp[i]))
        print('|', '  '.join(board_element[i]))


# parameters
plants = ['\U0001F3F9', '\U0001F33B', "\U0001F954", '\U0001F330']
plantsData = [
    {'cost': 30, 'atk': 1, 'hp': 9, 'cd': 2, 'element': ' ', 'hikari': 0, 'straight': 0, 'tp': 0},
    {'cost': 15, 'hp': 9, 'atk': 5, 'cd': 2, 'element': ' ', 'hikari': 0, 'straight': 0, 'tp': 0},
    {'cost': 5, 'hp': 9, 'atk': 100, 'cd': 9, 'element': ' ', 'hikari': 0, 'straight': 0, 'tp': 0},
    {'cost': 15, 'hp': 50, 'cd': 9, 'element': ' ', 'hikari': 0, 'straight': 0, 'tp': 0}
]

zombies = ['\U0001F47B', '\U0001F480', '\U0001F9DF', '\U0001F9DB']
zomData = [
    {'atk': 1, 'hp': 6, 'element': ' ', 'elementAttach': E.copy(), 'moved': 0, 'silent': 0},
    {'atk': 2, 'hp': 8, 'element': ' ', 'elementAttach': E.copy(), 'moved': 0, 'silent': 0},
    {'atk': 2, 'hp': 11, 'element': ' ', 'elementAttach': E.copy(), 'moved': 0, 'silent': 0},
    {'atk': 3, 'hp': 15, 'element': ' ', 'elementAttach': E.copy(), 'moved': 0, 'silent': 0}
]

elements = ['~', '#', '!', '=', ' ']


def rotate(x, y):

    try:
        a = board[x][y]
        b = board[x][y + 1]
        c = board[x + 1][y + 1]
        d = board[x + 1][y]
        if a in plants and b in plants and c in plants and d in plants:
            board[x][y] = d
            board[x][y + 1] = a
            board[x + 1][y + 1] = b
            board[x + 1][y] = c
            a = gameData[x][y]
            b = gameData[x][y + 1]
            c = gameData[x + 1][y + 1]
            d = gameData[x + 1][y]
            gameData[x][y] = d
            gameData[x][y + 1] = a
            gameData[x + 1][y + 1] = b
            gameData[x + 1][y] = c
    except IndexError:
        pass


def irroate(x, y):
    try:
        a = board[x][y]
        b = board[x][y + 1]
        c = board[x + 1][y + 1]
        d = board[x + 1][y]
        if a in plants and b in plants and c in plants and d in plants:
            board[x][y] = b
            board[x][y + 1] = c
            board[x + 1][y + 1] = d
            board[x + 1][y] = a
            a = gameData[x][y]
            b = gameData[x][y + 1]
            c = gameData[x + 1][y + 1]
            d = gameData[x + 1][y]
            gameData[x][y] = b
            gameData[x][y + 1] = c
            gameData[x + 1][y + 1] = d
            gameData[x + 1][y] = a
    except IndexError:
        pass


def uppush(x, y):
    up = gameData[x - 1][y]
    self = gameData[x][y]
    if board[x - 1][y] in plants and board[x][y] in plants and x - 1 >= 0:
        gameData[x][y] = up
        gameData[x - 1][y] = self
        up = board[x - 1][y]
        self = board[x][y]
        board[x][y] = up
        board[x - 1][y] = self


def downpush(x, y):

    down = gameData[x + 1][y]
    self = gameData[x][y]
    if board[x + 1][y] in plants and board[x][y] in plants and x + 1 <= 4:
        gameData[x][y] = down
        gameData[x + 1][y] = self
        down = board[x + 1][y]
        self = board[x][y]
        board[x][y] = down
        board[x + 1][y] = self


def leftpush(x, y):

    self = gameData[x][y]
    left = gameData[x][y - 1]
    if board[x][y - 1] in plants and board[x][y] in plants and y - 1 >= 0:
        gameData[x][y] = left
        gameData[x][y - 1] = self
        left = board[x][y - 1]
        self = board[x][y]
        board[x][y] = left
        board[x][y - 1] = self


def rightpush(x, y):
    try:
        self = gameData[x][y]
        right = gameData[x][y + 1]
        if board[x][y + 1] in plants and board[x][y] in plants:
            gameData[x][y] = right
            gameData[x][y + 1] = self
            right = board[x][y + 1]
            self = board[x][y]
            board[x][y] = right
            board[x][y + 1] = self
    except IndexError:
        pass


def tp(a, b):
    x, y = a
    u, v = b
    p = board[x][y]
    q = board[u][v]
    r = gameData[x][y]
    s = gameData[u][v]
    if p in plants and q in plants and r['tp'] and s['tp']:
        board[x][y] = q
        board[u][v] = p
        gameData[x][y] = s
        gameData[u][v] = r
        requirement[1] += 1
    if not (r['tp'] and s['tp']):
        print(r'Please be reminded that you can only use teleport after at least one round of the sunflower attached with "!".')
        input('Press Enter to continue')


def Hikari_ni_Naru(x, y):
    # print('Hikari!')
    if board[x][y] in plants and gameData[x][y]['hikari']:
        board[x][y] = ' '
        gameData[x][y] = template.copy()
        requirement[0] += 1

def check():
    # print('check')
    global remove
    score = 0
    remove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j < 8:
                if board[i][j] == board[i][j + 1] == board[i][j + 2] and board[i][j] in plants:
                    remove.extend(((i, j), (i, j + 1), (i, j + 2)))
                    score += 2
                if i < 3:
                    if board[i][j] == board[i + 1][j] == board[i + 2][j] and board[i][j] in plants:
                        remove.extend(((i, j), (i + 1, j), (i + 2, j)))
                        score += 2
    cost[0] += score
    return score


def rmv():
    # print('rmv', remove)
    for i, j in remove:
        board[i][j] = ' '
        gameData[i][j] = template.copy()


def fall():
    f = 0
    # print('fall')
    for i in range(len(board)):
        for j in range(len(board[i]) - 2):
            if gameData[i][j] == template.copy() and hole[i][j] != '+':
                f = 1
                # print('detect', (i, j))
                break
    if f:
        update = 0
        for i in range(len(board)):
            if update:
                print_board()
                update = 0
            time.sleep(0.07)
            newPlants = [plants[random.randint(0, 3)] for m in range(8)]  # size
            for j in range(len(board[i]) - 2):
                if hole[i][j] != '+' and board[i][j] == ' ':
                    if i == 0:
                        update = 1
                        board[i][j] = newPlants[j]
                        gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
                    else:
                        if board[i - 1][j] in plants:
                            board[i][j] = board[i - 1][j]
                            gameData[i][j] = gameData[i - 1][j]
                            board[i - 1][j] = ' '
                            gameData[i - 1][j] = template.copy()
                            update = 1
                        else:
                            board[i][j] = newPlants[j]
                            gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
                            update = 1

        fall()


def react():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in zombies:
                n = len(gameData[i][j]['elementAttach'])
                # print((i, j), gameData[i][j]['elementAttach'], n)
                if n >= 2:
                    excess_element = []
                    for k in range(int(n / 2)):
                        elm = gameData[i][j]['elementAttach'][2 * k:2 * k + 2]
                        # print(elm)
                        se = set(elm)
                        if len(se) == 1:
                            excess_element = excess_element + list(se)
                        elif se == {'#', '!'}:
                            print('burst')
                            gameData[i][j]['hp'] -= 2
                            requirement[3] += 1
                        elif se == {'#', '='}:
                            print('silent')
                            gameData[i][j]['silent'] = 1
                            requirement[3] += 1
                        elif se == {'!', '='}:
                            print('pierce')
                            requirement[3] += 1
                            for z in range(len(board[i][j + 1:])):
                                if board[i][j + z + 1] in zombies:
                                    gameData[i][j + z + 1]['hp'] -= 1

                                if i - z - 1 >= 0:
                                    if board[i - z - 1][j + z + 1] in zombies:
                                        gameData[i - z - 1][j + z + 1]['hp'] -= 1

                                if i + z + 1 <= 4:
                                    if board[i + z + 1][j + z + 1] in zombies:
                                        gameData[i + z + 1][j + z + 1]['hp'] -= 1
                        elif '~' in elm:

                            elm = list(se - {'~'})
                            requirement[3] += 1
                            print('spread', elm)
                            if i + 1 <= 4:
                                if board[i + 1][j] in zombies:  # down

                                    gameData[i + 1][j]['elementAttach'] = \
                                        gameData[i + 1][j]['elementAttach'] + elm

                            if i - 1 >= 0:
                                if board[i - 1][j] in zombies:  # up
                                    gameData[i - 1][j]['elementAttach'] = \
                                        gameData[i - 1][j]['elementAttach'] + elm

                            if i + 1 <= 4 and j - 1 >= 0:
                                if board[i + 1][j - 1] in zombies:  # down left
                                    gameData[i + 1][j - 1]['elementAttach'] = \
                                        gameData[i + 1][j - 1]['elementAttach'] + elm

                            if i + 1 <= 4 and j + 1 <= 9:
                                if board[i + 1][j + 1] in zombies:  # down right
                                    gameData[i + 1][j + 1]['elementAttach'] = \
                                        gameData[i + 1][j + 1]['elementAttach'] + elm

                            if i - 1 >= 0 and j - 1 >= 0:
                                if board[i - 1][j - 1] in zombies:  # up left
                                    gameData[i - 1][j - 1]['elementAttach'] = \
                                        gameData[i - 1][j - 1]['elementAttach'] + elm

                            if i - 1 >= 0 and j + 1 <= 9:
                                if board[i - 1][j + 1] in zombies:  # up right
                                    gameData[i - 1][j + 1]['elementAttach'] = \
                                        gameData[i - 1][j + 1]['elementAttach'] + elm

                            if j + 1 <= 9:
                                if board[i][j + 1] in zombies:  # right
                                    gameData[i][j + 1]['elementAttach'] = \
                                        gameData[i][j + 1]['elementAttach'] + elm

                            if j - 1 >= 0:
                                if board[i][j - 1] in zombies:  # left
                                    gameData[i][j - 1]['elementAttach'] = \
                                        gameData[i][j - 1]['elementAttach'] + elm
                    # print('exc', excess_element)
                    if n % 2 == 0:
                        gameData[i][j]['elementAttach'] = E.copy() + excess_element

                    else:
                        try:
                            gameData[i][j]['elementAttach'] = [gameData[i][j]['elementAttach'][-1]] + excess_element
                        except IndexError:
                            pass


def updateElement():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in zombies:
                try:
                    gameData[i][j]['element'] = gameData[i][j]['elementAttach'][0]
                except IndexError:
                    pass


def merge(i, j):
    # print('merge')
    if j - 1 >= 0:
        summ = zombies.index(board[i][j]) + zombies.index(board[i][j - 1]) + 2
        if summ - 1 >= 0:
            board[i][j - 1] = zombies[summ - 1]
            gameData[i][j - 1] = zomData[summ - 1].copy()
            board[i][j] = ' '
            gameData[i][j] = template.copy()


def action(i, j, _=1):
    refresh = 0
    try:
        if gameData[i][j]['hp'] <= 0:
            if board[i][j] in plants:
                hole[i][j] = '+'
            else:
                gameData[i][j] = template.copy()
            board[i][j] = ' '
        else:
            if board[i][j] == '\U0001F33B':
                if gameData[i][j]['element'] == '#':  # max hp

                    if board[i - 1][j] in plants and gameData[i - 1][j]['hp'] < \
                            plantsData[plants.index(board[i - 1][j])]['hp'] and i > 0:
                        gameData[i - 1][j]['hp'] = gameData[i - 1][j]['hp'] + 1
                    if i < 4:
                        if board[i + 1][j] in plants and gameData[i + 1][j]['hp'] < \
                                plantsData[plants.index(board[i + 1][j])]['hp']:
                            gameData[i + 1][j]['hp'] = gameData[i + 1][j]['hp'] + 1
                    if board[i][j - 1] in plants and gameData[i][j - 1]['hp'] < \
                            plantsData[plants.index(board[i][j - 1])]['hp'] and j > 0:
                        gameData[i][j - 1]['hp'] = gameData[i][j - 1]['hp'] + 1
                    if j < 7:
                        if board[i][j + 1] in plants and gameData[i][j + 1]['hp'] < \
                                plantsData[plants.index(board[i][j + 1])]['hp']:
                            gameData[i][j + 1]['hp'] = gameData[i][j + 1]['hp'] + 1

                if gameData[i][j]['element'] == '!':

                    if board[i - 1][j] in plants and i > 0:
                        gameData[i - 1][j]['tp'] = 1
                    if i < 4:
                        if board[i + 1][j] in plants:
                            gameData[i + 1][j]['tp'] = 1
                    if board[i][j - 1] in plants:
                        gameData[i][j - 1]['tp'] = 1
                    if j < 7:
                        if board[i][j + 1] in plants:
                            gameData[i][j + 1]['tp'] = 1

                if gameData[i][j]['element'] == '=':  # max hp
                    if board[i - 1][j] in plants and i > 0:
                        gameData[i - 1][j]['hikari'] = 1
                    if i < 4:
                        if board[i + 1][j] in plants:
                            gameData[i + 1][j]['hikari'] = 1
                    if board[i][j - 1] in plants and j - 1 >= 0:
                        gameData[i][j - 1]['hikari'] = 1
                    if j < 7:
                        if board[i][j + 1] in plants:
                            gameData[i][j + 1]['hikari'] = 1

            if board[i][j] == '\U0001F3F9':
                for k in board[i][j:]:
                    if k in zombies:
                        gameData[i][board[i].index(k)]['hp'] = \
                            gameData[i][board[i].index(k)]['hp'] \
                            - plantsData[plants.index('\U0001F3F9')]['atk']
                        if gameData[i][j]['element'] != ' ':
                            gameData[i][board[i].index(k)]['elementAttach'] = \
                                gameData[i][board[i].index(k)]['elementAttach'] + [gameData[i][j]['element']]
                        break
            if board[i][j] == "\U0001F954":
                if gameData[i][j]['element'] == '~':
                    boom = 0
                    for u in range(len(board)):
                        for v in range(len(board[i])):
                            if board[u][v] in zombies:
                                gameData[u][v]['elementAttach'] = gameData[u][v]['elementAttach'] + ['~']
                                boom = 1
                    if boom: requirement[2] += 1
                    board[i][j] = ' '
                    gameData[i][j] = template.copy()
                    refresh = 1

                if gameData[i][j]['element'] == '=':
                    hole0 = []
                    for u in range(len(hole)):
                        for v in range(len(hole[u])):
                            if hole[u][v] == '+':
                                hole0.append((u, v))
                    # print('hole', hole0)
                    try:
                        k, l = random.choice(hole0)
                    except IndexError:
                        pass
                    # print('choice', (k, l))
                    try:  # dangerous
                        hole[k][l] = ' '
                        requirement[0] += 1
                    except UnboundLocalError:
                        pass
                    board[i][j] = ' '
                    gameData[i][j] = template.copy()
                    refresh = 1
                if gameData[i][j]['element'] == '!':
                    pass
                if gameData[i][j]['element'] == '#':
                    for u in range(len(board)):
                        for v in range(len(board[i])):
                            if board[u][v] in zombies:
                                gameData[u][v]['hp'] -= 2
                    board[i][j] = ' '
                    gameData[i][j] = template.copy()
                    refresh = 1

            if board[i][j] == '\U0001F330':
                if gameData[i][j]['element'] == '~':
                    try:
                        if board[i][j + 1] in ('\U0001F47B', '\U0001F480') and board[i][j + 2] == ' ':
                            # print('push')
                            board[i][j + 2] = board[i][j + 1]
                            board[i][j + 1] = ' '
                            gameData[i][j + 2] = gameData[i][j + 1]
                            gameData[i][j + 1] = template.copy()
                            requirement[2] += 1
                    except IndexError:
                        pass

                if gameData[i][j]['element'] == '!':
                    if j + 1 <= 9:
                        if board[i][j + 1] in zombies:
                            gameData[i][j + 1]['hp'] = gameData[i][j + 1]['hp'] - \
                                                       zomData[zombies.index(board[i][j + 1])][
                                                           'atk']

            if board[i][j] in ('\U0001F43A', '\U0001F43A'):
                # print('MN', (i, j))
                if j + 1 <= 9:
                    # print('M acts')

                    if board[i][j + 1] == ' ' and not gameData[i][j]['moved']:
                        # print('M moves')

                        board[i][j + 1] = board[i][j]
                        board[i][j] = ' '
                        gameData[i][j + 1] = gameData[i][j]
                        gameData[i][j + 1]['moved'] = 1
                        # print(gameData[i][j + 1]['moved'])
                        gameData[i][j] = template.copy()

                        # if board[i][j + 1] == '\U0001F43A' and _: action(i, j + 1, 0)

                    elif board[i][j + 1] in zombies:
                        # print('M hits')
                        damage = gameData[i][j]['atk']
                        gameData[i][j + 1]['hp'] -= damage
                        # if board[i][j] == '\U0001F43A' and _: action(i, j, 0)
                else:
                    if not gameData[i][j]['moved']:
                        # print('M dis')
                        board[i][j] = ' '
                        gameData[i][j] = template.copy()

            if board[i][j] in zombies:

                if j == 0:
                    # print('fail')
                    return 'fail'

                if board[i][j - 1] == "\U0001F954" and j - 1 >= 0:
                    if gameData[i][j - 1]['element'] != '!':
                        board[i][j] = ' '
                        gameData[i][j] = template.copy()
                        hole[i][j - 1] = '+'
                    else:
                        board[i][j] = '\U0001F43A'
                        if board[i][j - 1] in ('\U0001F9DF', '\U0001F9DB'):
                            board[i][j] = '\U0001F43A'
                        requirement[1] += 1
                    board[i][j - 1] = ' '
                    gameData[i][j - 1] = template.copy()

                if board[i][j - 1] in zombies \
                        and zombies.index(board[i][j]) + zombies.index(board[i][j - 1]) <= 2 \
                        and not gameData[i][j - 1]['silent'] and j - 1 >= 0:
                    merge(i, j)

                if board[i][j - 1] == ' ' and not \
                        (board[i][j - 2] == '\U0001F330' \
                         and gameData[i][j - 2]['element'] == '~' \
                         and j - 2 >= 0 \
                         and board[i][j] not in ('\U0001F9DF', '\U0001F9DB')) and j - 1 >= 0:
                    board[i][j - 1] = board[i][j]
                    board[i][j] = ' '
                    gameData[i][j - 1] = gameData[i][j]
                    gameData[i][j] = template.copy()
                    if board[i][j - 1] in ('\U0001F9DF', '\U0001F9DB') and _: action(i, j - 1, 0)

                if board[i][j - 1] in plants + ['\U0001F43A', '\U0001F43A'] and j - 1 >= 0:
                    # print('zom hits')
                    damage = gameData[i][j]['atk']
                    if board[i][j - 1] == '\U0001F330' and gameData[i][j - 1]['element'] == '#': damage *= 0.7
                    gameData[i][j - 1]['hp'] = gameData[i][j - 1]['hp'] - damage
                    # print('damage', damage, gameData[i][j - 1])
                    if board[i][j] in ('\U0001F9DF', '\U0001F9DB') and _: action(i, j, 0)
                    if board[i][j - 1] == '\U0001F330' and gameData[i][j - 1]['element'] == '=':
                        # print('change row')
                        if i <= 3:
                            for k in range(len(board[i + 1])):
                                if board[i + 1][k] == ' ':
                                    board[i + 1][k] = board[i][j]
                                    board[i][j] = ' '
                                    gameData[i + 1][k] = gameData[i][j]
                                    gameData[i][j] = template.copy()
                                    requirement[0] += 1
                                    break
                        elif i == 4:
                            for k in range(len(board[i - 1])):
                                if board[i - 1][k] == ' ':
                                    board[i - 1][k] = board[i][j]
                                    board[i][j] = ' '
                                    gameData[i - 1][k] = gameData[i][j]
                                    gameData[i][j] = template.copy()
                                    requirement[0] += 1
                                    break
    except TypeError:
        pass
    return refresh


def nextFrame():
    # print('nextFrame')
    Re = 0
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            a = action(i, j)
            # print(a)
            if a == 'fail':
                # print('defeat')
                return 'defeat'
            elif a == 1:
                Re = 1

    # print('action ends')
    react()
    # print('reaction ends')
    updateElement()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in ('\U0001F43A', '\U0001F43A'):
                if gameData[i][j]['moved']:
                    gameData[i][j]['moved'] = 0
            if board[i][j] in zombies:
                count += 1
    Round[0] += 1
    if count <= 4:
        Victory[0] += 1
    else:
        Victory[0] = 0
    return Re


def genZb():
    # print('genz')
    x = random.randint(0, 4)
    z = random.choice(zombies[:2])

    if board[x][9] == ' ':
        board[x][9] = z
        gameData[x][9] = zomData[zombies.index(z)].copy()


def genZb1():
    x = random.randint(0, 4)
    z = random.choice(zombies[2:])

    if board[x][9] == ' ':
        board[x][9] = z
        gameData[x][9] = zomData[zombies.index(z)].copy()


def genZb3():
    # print('genz')
    z = zombies[3]
    for _ in range(2):
        x = random.randint(0, 4)
        if board[x][9] == ' ':
            board[x][9] = z
            gameData[x][9] = zomData[zombies.index(z)].copy()


def update():
    fall()
    while check() != 0:
        rmv()
        fall()


# for i in range(5):
#     for j in range(3):
#         hole[i][j] = '+'


def teach1():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '\U0001F3F9', '\U0001F3F9', ' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you how to make use of fire-electricity reaction!')
    print('Type   e21#   to attach fire to the first shooter')

    command = input()
    if command == 'e21#':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach fire element to the first shooter!')
        print('Then type   e22!   to attach electricity to the second shooter')
        command = input()
        if command == 'e22!':
            x, y = tuple(map(int, (command[1], command[2])))
            ele = command[3]
            gameData[x][y]['element'] = ele
            print_board()
            print('You have successfully attach electricity element to the second shooter!')
            print('Type space to see what will happen')
            command = input()
            if command == ' ':
                nextFrame()
                print_board()
                print('Burst reaction! Zombie HP  decrease by 2!')
                clearGlobal()
                return
    print('You type something wrong, try again!')
    teach1()


def teach2():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '\U0001F3F9', '\U0001F3F9', ' ', ' ', ' ', '\U0001F330', '\U0001F480', ' ', '\U0001F480'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    gameData[2][7]['hp'] = 99
    print_board()
    print('Now we will teach you how to make use of fire-light reaction!')
    print('Type   e21#   to attach fire to the first shooter')
    command = input()
    if command == 'e21#':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach fire element to the first shooter!')
        print('Then type   e22=   to attach light to the second shooter')
        command = input()
        if command == 'e22=':
            x, y = tuple(map(int, (command[1], command[2])))
            ele = command[3]
            gameData[x][y]['element'] = ele
            print_board()
            print('You have successfully attach light element to the second shooter!')
            print('Type space to see what will happen')
            command = input()
            if command == ' ':
                nextFrame()
                print_board()
                print('Type space to see what will happen')
                command = input()
                if command == ' ':
                    nextFrame()
                    print_board()
                    print('Frozen reaction! Zombie cannot fuse!')
                    clearGlobal()
                    return
    print('You type something wrong, try again!')
    teach2()


def teach3():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' '],
        [' ', '\U0001F3F9', '\U0001F3F9', ' ', ' ', '\U0001F480', '\U0001F480', '\U0001F480', '\U0001F480',
         '\U0001F480'],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you how to make use of electricity-light reaction!')
    print('Type   e21!  to attach electricity to the first shooter')
    command = input()
    if command == 'e21!':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach electricity element to the first shooter!')
        print('Then type   e22=   to attach light to the second shooter')
        command = input()
        if command == 'e22=':
            x, y = tuple(map(int, (command[1], command[2])))
            ele = command[3]
            gameData[x][y]['element'] = ele
            print_board()
            print('You have successfully attach light element to the second shooter!')
            print('Type space to see what will happen')
            command = input()
            if command == ' ':
                nextFrame()
                print_board()
                print('Photoelectric reaction! Attack all zombies in horizontal, vertical and diagonal path!')
                clearGlobal()
                return
    print('You type something wrong, try again!')
    teach3()


def teach4():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', '\U0001F480', '\U0001F480', ' '],
        [' ', '\U0001F3F9', '\U0001F3F9', ' ', ' ', ' ', ' ', '\U0001F480', '\U0001F480', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', '\U0001F480', '\U0001F480', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you how to make use of reaction consist of wind!')
    print('Type   e21~   to attach wind to the first shooter')
    command = input()
    if command == 'e21~':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach wind element to the first shooter!')
        print('Then attach fire electricity or light elements to the second shooter(except wind)')
        command = input()
        if command[0] == 'e' \
                and len(command) == 4 \
                and ord(command[2]) in numbers \
                and ord(command[1]) in numbers \
                and command[3] != '~':
            x, y = tuple(map(int, (command[1], command[2])))
            ele = command[3]
            if ele in elements and x < 5 and y < 8:
                gameData[x][y]['element'] = ele
                print_board()
                print(f'You have successfully attach {command[3]} element to the second shooter!')
                print('Type space to see what will happen')
                command = input()
                if command == ' ':
                    nextFrame()
                    print_board()
                    print('Spread reaction! The element will be spread out!')
                    clearGlobal()
                    return
    input('You type something wrong, try again! (Press Enter)')
    teach4()


def teach5():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '\U0001F3F9', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the element power of the shooter!')
    print('Type   e21~   to attach wind to the shooter(In fact you can attach any elements later in the game)')
    command = input()
    if command == 'e21~':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach wind element to the shooter!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Zombie is also attach with wind element!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach5()


def teach6():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F330', '\U0001F480', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the wind power of the walnut!')
    print('Type   e26~   to attach wind to the walnut')
    command = input()
    if command == 'e26~':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach wind element to the walnut!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Zombie(only \U0001F47B or \U0001F480) is push to right by one!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach6()


def teach7():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F330', '\U0001F480', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the light power of the walnut!')
    print('Type   e26=   to attach light to the walnut')
    command = input()
    if command == 'e26=':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach light element to the walnut!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Zombie will go to another line!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach7()


def teach9():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', "\U0001F954", '+', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the light power of the bomb!')
    print('Type   e26=   to attach light to the bomb')
    command = input()
    if command == 'e26=':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach light element to the bomb!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Hole is gone!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach9()


def teach10():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', '\U0001F480', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', "\U0001F954", ' ', '\U0001F480', '\U0001F480'],
        [' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', '\U0001F480', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the wind power of the bomb!')
    print('Type   e26~   to attach wind to the bomb')
    command = input()
    if command == 'e26~':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach wind element to the bomb!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('All zombie are attached with wind!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach10()


def teach11():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', '\U0001F480', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', "\U0001F954", ' ', '\U0001F480', '\U0001F480'],
        [' ', ' ', ' ', ' ', '\U0001F480', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F480', ' ', '\U0001F480', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the fire power of the bomb!')
    print('Type   e26#   to attach fire to the bomb')
    command = input()
    if command == 'e26#':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach fire element to the bomb!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('All zombie will be attacked!')
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach11()


def teach12():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', "\U0001F954", '\U0001F9DB', ' ', ' ', '\U0001F480', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the electricity power of the bomb!')
    print('Type   e23!   to attach fire to the bomb')
    command = input()
    if command == 'e23!':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach electricity element to the bomb!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('You turn a zombie into your ally!')
            print('Keep typing space to see how it will help you')
            while input() == ' ' and '\U0001F480' in board[2]:
                nextFrame()
                print_board()
            clearGlobal()
            return
    print('You type something wrong, try again!')
    teach12()


def teach13():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F3F9', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '\U0001F3F9', '\U0001F33B', '\U0001F330', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', "\U0001F954", ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the electricity power of the sunflower!')
    print('Type   e26!  to attach electricity to the sunflower')
    command = input()
    if command == 'e26!':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach electricity element to the sunflower!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Type   t1627   to see what will happen')
            command = input()
            if command[0] == 't':
                a = tuple(map(int, (command[1], command[2])))
                b = tuple(map(int, (command[3], command[4])))
                tp(a, b)
                print('tp')
                print_board()
                print('You can teleportation between two plants adjacent to sunflower!')

                clearGlobal()
                return
    print('You type something wrong, try again!')
    teach13()


def teach14():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '\U0001F3F9', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '\U0001F3F9', '\U0001F33B', '\U0001F330', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', "\U0001F954", ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the light power of the sunflower!')
    print('Type   e26=   to attach light to the sunflower')
    command = input()
    if command == 'e26=':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach light element to the sunflower!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Type h27 to see what will happen!')
            command = input()
            if command[0] == 'h':
                x, y = tuple(map(int, (command[1], command[2])))
                Hikari_ni_Naru(x, y)
                print_board()
                print('You can eliminate a plant adjacent to sunflower!')
                clearGlobal()
                return
    print('You type something wrong, try again!')
    teach14()


def teach15():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', '\U0001F330', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '\U0001F3F9', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '\U0001F330', '\U0001F3F9', '\U0001F33B', '\U0001F3F9', '\U0001F330', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '\U0001F3F9', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '\U0001F330', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will teach you the wind power of the sunflower!')
    print('Type   e24~   to attach wind to the sunflower')
    command = input()
    if command == 'e24~':
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        gameData[x][y]['element'] = ele
        print_board()
        print('You have successfully attach wind element to the sunflower!')
        print('Type space to see what will happen')
        command = input()
        if command == ' ':
            nextFrame()
            print_board()
            print('Type p connect with a coordinate to see what will happen!')
            command = input()
            if command[0] == 'p':
                x, y = tuple(map(int, (command[1], command[2])))
                if gameData[x - 1][y]['element'] == '~' and board[x - 1][y] == '\U0001F33B' and x - 1 >= 0:
                    downpush(x, y)

                elif gameData[x][y - 1]['element'] == '~' and board[x][y - 1] == '\U0001F33B' and y - 1 >= 0:
                    rightpush(x, y)

                elif gameData[x + 1][y]['element'] == '~' and board[x + 1][y] == '\U0001F33B' and x + 1 <= 4:
                    uppush(x, y)

                elif gameData[x][y + 1]['element'] == '~' and board[x][y + 1] == '\U0001F33B' and y + 1 <= 9:
                    leftpush(x, y)

                print_board()
                print('You push a plant adjacent to sunflower!')
                clearGlobal()
                return
    print('You type something wrong, try again!')
    teach15()


def teachRotate():
    global board
    print('\n' * 1000)
    print('In this game, unlike candy crush, the elements rotate as a two by two square clockwise')
    print('Look carefully at the example')
    print()
    print('                   1 2\n                   3 4')
    print('\n')
    print('After you input the coordinate, the 2*2 square will rotate clockwise.')
    time.sleep(5)
    print('\n' * 3)
    print('                   3 1\n                   4 2')
    print('\n')
    print('As you can see, each element has rotated clockwise by one')
    time.sleep(5)
    input('Press any key to coutinue')
    board = [
        ['\U0001F3F9', '\U0001F330', '\U0001F3F9', '\U0001F330', '\U0001F330', '\U0001F33B', '\U0001F330', "\U0001F954",
         ' ', ' '],
        ['\U0001F330', "\U0001F954", '\U0001F33B', '\U0001F3F9', '\U0001F330', '\U0001F3F9', "\U0001F954", '\U0001F330',
         ' ', ' '],
        ["\U0001F954", '\U0001F330', "\U0001F954", '\U0001F3F9', '\U0001F33B', '\U0001F330', '\U0001F3F9', '\U0001F3F9',
         ' ', ' '],
        ['\U0001F330', '\U0001F33B', "\U0001F954", "\U0001F954", '\U0001F330', '\U0001F33B', '\U0001F33B', "\U0001F954",
         ' ', ' '],
        ["\U0001F954", '\U0001F3F9', '\U0001F3F9', '\U0001F330', '\U0001F33B', '\U0001F330', "\U0001F954", '\U0001F3F9',
         ' ', ' ']
    ]
    print_board()
    print('Now apply the skill to rotate plants!')
    print('Your input number should be the top left of the two by two square you want to rotate!')
    print('For example, if you want to rotate 00, 01, 10 and 11, type in "00"')
    print('Make sure you make three in a row after the rotation! ')
    command = input()
    if len(command) == 2 and ord(command[0]) in numbers and ord(command[1]) in numbers:
        x, y = tuple(map(int, (command[0], command[1])))
        rotate(x, y)
        if check() == 0:
            irroate(x, y)
            print_board()
            print('This is an invalid rotation!')
            print('No plants were eliminated after rotating!')
            print('Try again!')
            time.sleep(3)
            teachRotate()
        else:
            print_board()
            print('Congratulations! This is a valid rotation!')
            clearGlobal()
            return
    else:
        print('invalid input')
        teachRotate()


def showZombieAttack():
    global board
    global gameData
    global hole
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', "\U0001F954", '\U0001F33B', ' ', '\U0001F480', ' ', '\U0001F480', ' ', ' '],
        [' ', ' ', "\U0001F954", '\U0001F33B', '\U0001F480', ' ', ' ', '\U0001F480', ' ', ' '],
        [' ', ' ', "\U0001F954", '\U0001F33B', ' ', ' ', '\U0001F480', ' ', '\U0001F480', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    for i in range(5):
        for j in range(10):
            if board[i][j] in plants:
                gameData[i][j] = plantsData[plants.index(board[i][j])].copy()
            elif board[i][j] in zombies:
                gameData[i][j] = zomData[zombies.index(board[i][j])].copy()
            elif board[i][j] == ' ':
                gameData[i][j] = template.copy()
    print_board()
    print('Now we will show you how zombies attack plants!')
    print('Type space to see what will happen')
    command = input()
    while command == ' ':
        nextFrame()
        print_board()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if '+' in hole[i][j]:
                    print('After a bomb kills a zombie, it will leave a hole (+)')
                    clearGlobal()
                    return
        print('Type space to see what will happen')
        command = input()

    print('You type something wrong, try again!')
    showZombieAttack()


def noHole():
    no_hole = 1
    for i in range(5):
        for j in range(10):
            if hole[i][j] == '+':
                no_hole = 0
                break
    # print('noh', no_hole)
    return no_hole


def clearZombies():
    for i in range(5):
        for j in range(10):
            if board[i][j] in zombies:
                board[i][j] = ' '
                gameData[i][j] = template.copy()


def Main():
    global board
    global gameData
    global hole
    global Round
    global Victory
    print('\U0001F9DF' + ": This part is easy. If you can't pass this, you are just bad!")
    time.sleep(3)
    print('''
╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔═╗╔╗╔╔═╗
╚═╗ ║ ╠═╣║ ╦║╣   ║ ║║║║║╣ 
╚═╝ ╩ ╩ ╩╚═╝╚═╝  ╚═╝╝╚╝╚═╝
''')  # picture
    time.sleep(3)
    print('''
████████▄     ▄████████    ▄████████    ▄████████ ███▄▄▄▄      ▄████████    ▄████████ 
███   ▀███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ 
███    ███   ███    █▀    ███    █▀    ███    █▀  ███   ███   ███    █▀    ███    █▀  
███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄     ███   ███   ███         ▄███▄▄▄     
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ▀███████████ ▀▀███▀▀▀     
███    ███   ███    █▄    ███          ███    █▄  ███   ███          ███   ███    █▄  
███   ▄███   ███    ███   ███          ███    ███ ███   ███    ▄█    ███   ███    ███ 
████████▀    ██████████   ███          ██████████  ▀█   █▀   ▄████████▀    ██████████ 

''')
    print('----------------------------------Survive 20 rounds------------------------------------')
    input('Press any key to continue')
    while Round[0] < 20:
        print_board()
        if main(1) == 'Wasted':
            print(Wasted)
            return 1
    clearZombies()
    print('\U0001F9DF' + ": A worthwhile oppononet indeed. Come on, let's see what you got!")
    time.sleep(3)
    print('''
╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╦ ╦╔═╗
╚═╗ ║ ╠═╣║ ╦║╣    ║ ║║║║ ║
╚═╝ ╩ ╩ ╩╚═╝╚═╝   ╩ ╚╩╝╚═╝
''')

    time.sleep(3)
    print('''
   ▄████████     ███        ▄████████  ▄█          ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄       ███     
  ███    ███ ▀█████████▄   ███    ███ ███         ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ▀█████████▄ 
  ███    █▀     ▀███▀▀██   ███    ███ ███         ███    █▀  ███   ███   ███   ███    █▀  ███   ███    ▀███▀▀██ 
  ███            ███   ▀   ███    ███ ███        ▄███▄▄▄     ███   ███   ███  ▄███▄▄▄     ███   ███     ███   ▀ 
▀███████████     ███     ▀███████████ ███       ▀▀███▀▀▀     ███   ███   ███ ▀▀███▀▀▀     ███   ███     ███     
         ███     ███       ███    ███ ███         ███    █▄  ███   ███   ███   ███    █▄  ███   ███     ███     
   ▄█    ███     ███       ███    ███ ███▌    ▄   ███    ███ ███   ███   ███   ███    ███ ███   ███     ███     
 ▄████████▀     ▄████▀     ███    █▀  █████▄▄██   ██████████  ▀█   ███   █▀    ██████████  ▀█   █▀     ▄████▀   
                                      ▀                                                                                                                                                                                         
''')
    print('----------------------------------------Gain 100 costs------------------------------------------')
    input('Press any key to continue')
    while cost[0] < 200:
        print_board()
        if main(2) == 'Wasted':
            print(Wasted)
            return 1
    clearZombies()
    print('\U0001F9DF' + ": Welcome to the final round. This is all I've got, do you have enough to finish me?")
    time.sleep(3)
    print('''
╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╦ ╦╦═╗╔═╗╔═╗
╚═╗ ║ ╠═╣║ ╦║╣    ║ ╠═╣╠╦╝║╣ ║╣ 
╚═╝ ╩ ╩ ╩╚═╝╚═╝   ╩ ╩ ╩╩╚═╚═╝╚═╝
''')
    time.sleep(3)
    print('''
           ▄████████  ▄██████▄  ███    █▄  ███▄▄▄▄       ███        ▄████████    ▄████████            
          ███    ███ ███    ███ ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███            
          ███    █▀  ███    ███ ███    ███ ███   ███    ▀███▀▀██   ███    █▀    ███    ███            
          ███        ███    ███ ███    ███ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀            
          ███        ███    ███ ███    ███ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀              
          ███    █▄  ███    ███ ███    ███ ███   ███     ███       ███    █▄  ▀███████████            
          ███    ███ ███    ███ ███    ███ ███   ███     ███       ███    ███   ███    ███            
          ████████▀   ▀██████▀  ████████▀   ▀█   █▀     ▄████▀     ██████████   ███    ███            
                                                                                ███    ███            
 ▄██████▄     ▄████████    ▄████████    ▄████████ ███▄▄▄▄      ▄████████  ▄█   ▄█    █▄     ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ ███  ███    ███   ███    ███ 
███    ███   ███    █▀    ███    █▀    ███    █▀  ███   ███   ███    █▀  ███▌ ███    ███   ███    █▀  
███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄     ███   ███   ███        ███▌ ███    ███  ▄███▄▄▄     
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ▀███████████ ███▌ ███    ███ ▀▀███▀▀▀     
███    ███   ███          ███          ███    █▄  ███   ███          ███ ███  ███    ███   ███    █▄  
███    ███   ███          ███          ███    ███ ███   ███    ▄█    ███ ███  ███    ███   ███    ███ 
 ▀██████▀    ███          ███          ██████████  ▀█   █▀   ▄████████▀  █▀    ▀██████▀    ██████████ 

''')
    print('-------------------------------Clear all holes and struggle to survive---------------------------------')
    input('Press any key to continue')
    Victory[0] = 0
    while (not noHole()) or Victory[0] < 7:
        print_board()
        print(Victory)
        if main(3) == 'Wasted':
            print(Wasted)
            return 1

    print(Vic)
    return 0


def main(stage=None):
    if stage == None: stage = 2
    V = 1
    update()
    command = input()
    if len(command) == 0:
        print_board()
        print('Invalid')
        V = 0
        main()
    elif command == 'nl':
        w = nextFrame()
        # print('~', w)
        if w == 'defeat':
            return 'Wasted'
        if stage == 1:
            genZb1()
        elif stage == 2:
            genZb()
        elif stage == 3:
            genZb3()
    # elif command[0] == '?' and ord(command[2]) in numbers and ord(command[1]) in numbers:  # small guys
    #     print(id(gameData[int(command[1])][int(command[2])]), gameData[int(command[1])][int(command[2])])
    #     main()
    elif command[0] == 'e' \
            and cost[0] >= 5 and len(command) == 4 \
            and ord(command[2]) in numbers \
            and ord(command[1]) in numbers:
        x, y = tuple(map(int, (command[1], command[2])))
        ele = command[3]
        if ele not in elements or x >= 5 or y >= 8:
            print_board()
            print('invalid attach')
            V = 0
            main()
        else:
            gameData[x][y]['element'] = ele
            cost[0] -= 5
    else:
        if command[0] == 'p' and len(command) == 3 and ord(command[2]) in numbers and ord(command[1]) in numbers:
            x, y = tuple(map(int, (command[1], command[2])))

            if x >= 1 and x <= 3:
                if gameData[x - 1][y]['element'] == '~' and board[x - 1][y] == '\U0001F33B':
                    downpush(x, y)
                    if check() == 0:
                        uppush(x + 1, y)
                        print_board()
                        print('invalid uppush')
                        V = 0
                        main()
                    else:
                        requirement[2] += 1
 

            if y >= 1 and y <= 6:
                if gameData[x][y - 1]['element'] == '~' and board[x][y - 1] == '\U0001F33B':
                    rightpush(x, y)
                    if check() == 0:
                        leftpush(x, y + 1)
                        print_board()
                        print('invalid')
                        V = 0
                        main()
                    else:
                        requirement[2] += 1

            if x <= 3 and x >= 1:
                if gameData[x + 1][y]['element'] == '~' and board[x + 1][y] == '\U0001F33B' and x > 0:
                    uppush(x, y)
                    if check() == 0:
                        downpush(x - 1, y)
                        print_board()
                        print('invalid')
                        V = 0
                        main()
                    else:
                        requirement[2] += 1

            if y <= 6 and y >= 1:
                if gameData[x][y + 1]['element'] == '~' and board[x][y + 1] == '\U0001F33B' and y > 0:
                    leftpush(x, y)
                    if check() == 0:
                        rightpush(x, y - 1)
                        print_board()
                        print('invalid')
                        V = 0
                        main()
                    else:
                        requirement[2] += 1

            else:
                print_board()
                print('invalid')
                V = 0
                main()


        elif command[0] == 't' \
                and len(command) == 5 \
                and ord(command[1]) in numbers \
                and ord(command[2]) in numbers \
                and ord(command[3]) in numbers \
                and ord(command[4]) in numbers:
            a = tuple(map(int, (command[1], command[2])))
            b = tuple(map(int, (command[3], command[4])))
            tp(a, b)

            if check() == 0:
                tp(a, b)
                print_board()
                print('invalid')
                
                V = 0
                main()

        elif command[0] == 'h' and len(command) == 3 and ord(command[2]) in numbers and ord(command[1]) in numbers:
            x, y = tuple(map(int, (command[1], command[2])))
            if gameData[x][y]['hikari']:
                Hikari_ni_Naru(x, y)

            else:
                print_board()
                print('invalid')
                input('Please be reminded that it takes a round to be activated after attachment\nPress Enter to continue')
                V = 0

            fall()

        elif len(command) == 2 and ord(command[0]) in numbers and ord(command[1]) in numbers:
            x, y = tuple(map(int, (command[0], command[1])))
            rotate(x, y)
            if check() == 0:
                irroate(x, y)
                print_board()
                print('invalid')
                V = 0
                main()
            else:
                valid[0] += 1
        else:
            print_board()
            print('invalid input')
            V = 0
            main()
        while check() != 0:
            rmv()
            fall()
        if V:
            w = nextFrame()
            # print('~', w)
            if w == 'defeat':
                # print('Wasted')
                return 'Wasted'
            elif w == 1:
                update()
            if stage == 1:
                genZb1()
            elif stage == 2:
                genZb()
            elif stage == 3:
                genZb3()


# Main()


def one():
    print('One day, Kit was getting ready to sleep...')
    time.sleep(2)
    print('When suddenly......')
    time.sleep(2)
    print('\U0001F9DF')
    time.sleep(2)
    print('My name is Dirk! Your python codes turned me, a plant, into a zombie!!!')
    time.sleep(2)
    print('I must seek revenge and kill you!')
    time.sleep(2)
    print()
    print('Your task as the savior of the world is to help Kit kill Dirk and his zombie friends!')
    time.sleep(2)
    print(
        "You will need to combine plants together on a board. Don't be scared, we will guide you throughout the process")
    input('Press any key to continue')
    teachRotate()
    input('Press any key to continue')
    print("Now, let's see some action!")
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    print('Stage 1: Trigger valid rotation 7 times')
    time.sleep(3)
    input('Press any key to continue')
    while valid[0] < 7:
        print_board()
        if main() == 'Wasted':
            print(Wasted)
            return 1
        clearZombies()
    print(ma)
    print('Well done! You have learnt the skills to gain coins!')
    return 0


def two():
    print('\U0001F9DF : ROARRRRRR!!!!')
    time.sleep(2)
    print("\U0001F9DF : You're not going to kill me!")
    input('Press any key to continue')
    showZombieAttack()
    print('Now, your turn to kill some zombies!')
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    print('Survive 10 rounds to advance to next stage.')
    time.sleep(3)
    input('Press any key to continue')
    while Round[0] < 10:
        print_board()
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print("\U0001F9DF: This is not going to work. I'm calling backup!")
    return 0


def check3():
    count = 0
    for i in range(5):
        for j in range(10):
            if gameData[i][j]['element'] == '#':
                count += 1
    if count == 7:
        return 0
    else:
        return 1


def three():  # fire

    print('\U0001F9DF: Haha, what are you going to do, burn me alive?')
    input('Press any key to continue')
    teach11()
    input('Press any key to continue')
    #  description of fire wall and fire flower
    print('\U0001F9DF: What???? You learnt what???????')
    time.sleep(5)
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    print('To advance to next level, Attach Fire element 7 times')
    time.sleep(3)
    input('Press any key to continue')
    while check3():
        print_board()
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print("\U0001F9DF : I'm getting a little bit scared. ")
    return 0


def four():  # light
    print('\U0001F9DF : Dirk never gives up. You changed me, you broke me. I will finish you!')
    input('Press any key to continue')
    teach14()
    input('Press any key to continue')
    teach9()
    input('Press any key to continue')
    teach7()
    input('Press any key to continue')
    print('\U0001F9DF : My backup has arrived. You will see your downfall!')
    global board
    global gameData
    global hole
    global Round
    global Victory
    global requirement
    print('Trigger element effects of light 5 times')
    requirement[0] = 0
    time.sleep(3)
    input('Press any key to continue')
    while requirement[0] < 5:
        print_board()
        # print('req', requirement)
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print('\U0001F9DF : This is harder than I thought. ')
    return 0


def five():  # electricity  ban other elements
    input('Press any key to continue')
    print('\U0001F9DF' + ": You will see me like never before!")
    input('Press any key to continue')
    teach12()
    input('Press any key to continue')
    teach13()
    input('Press any key to continue')
    print('\U0001F9DF' + ": Electricity? Shocking me? Do you guys have any sort of human decency?")
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    global requirement
    requirement[1] = 0
    print('Trigger element effects of electricity 5 times')
    time.sleep(3)
    input('Press any key to continue')
    while requirement[1] < 5:
        print_board()
        # print('req', requirement)
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print('\U0001F9DF' + ": OKOK, please don't go so hard on me! Please please, you don't have to get rid of me!")
    return 0


def six():  # wind and attach  wind wall not tested
    print('\U0001F9DF' + ": Have you not heard my pleas? Stop learning new ways to kill me! Let's be friends!!!")
    input('Press any key to continue')
    teach6()
    input('Press any key to continue')
    teach15()
    input('Press any key to continue')

    teach10()
    input('Press any key to continue')
    print('\U0001F9DF' + ": Please!!! I beg you! Stop! What do you want me to do?")
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    global requirement
    requirement[2] = 0
    print('Trigger element effects of wind 5 times')
    time.sleep(3)
    input('Press any key to continue')
    while requirement[2] < 5:
        print_board()
        # print('req', requirement)
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print(
        '\U0001F9DF' + ": OKOK, I'll say it! You're amazing at python, you'll get an A for ENGG1330. Please, stop trying to kill me!")
    return 0


def seven():  # reaction
    print('\U0001F9DF' + ": I beg you one last time! I will go! Stop trying to kill me!")
    input('Press any key to continue')
    teach5()
    print('Remember that a bomb with wind element can attach ')
    input('Press any key to continue')
    teach1()
    input('Press any key to continue')
    teach2()
    input('Press any key to continue')
    teach3()
    input('Press any key to continue')
    teach4()
    input('Press any key to continue')
    print('\U0001F9DF' + ": What??? You've even turned my friends on me??")
    input('Press any key to continue')
    global board
    global gameData
    global hole
    global Round
    global Victory
    global requirement
    requirement[3] = 0
    print('Trigger element reaction 5 times')
    time.sleep(3)
    input('Press any key to continue')
    while requirement[3] < 5:
        print_board()
        # print('req', requirement)
        if main() == 'Wasted':
            print(Wasted)
            return 1
    print(ma)
    print(
        '\U0001F9DF' + ": OK, if you're that good, how about you fight me in the main round! I swear you will end up dead. ")
    time.sleep(3)
    print('\U0001F9DF' + ": Try me, there will only be one way to see who is the best at python!")
    return 0


print(r'''
                    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗             
                    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝             
                    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗               
                    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝               
                    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗             
                     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝             

                                         ████████╗ ██████╗                              
                                         ╚══██╔══╝██╔═══██╗                             
                                            ██║   ██║   ██║                             
                                            ██║   ██║   ██║                             
                                            ██║   ╚██████╔╝                             
                                            ╚═╝    ╚═════╝                              

██████╗ ██╗      █████╗ ███╗   ██╗████████╗██╗███████╗         ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗████╗  ██║╚══██╔══╝██║██╔════╝        ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║
██████╔╝██║     ███████║██╔██╗ ██║   ██║   ██║█████╗          ██║     ██████╔╝██║   ██║███████╗███████║
██╔═══╝ ██║     ██╔══██║██║╚██╗██║   ██║   ██║██╔══╝          ██║     ██╔══██╗██║   ██║╚════██║██╔══██║
██║     ███████╗██║  ██║██║ ╚████║   ██║   ██║███████╗        ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚══════╝         ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                (Genshin Impact version)

--------------------------------Press the number to choose what to play--------------------------------

------------------------------------------- 1. Story --------------------------------------------------
------------------------------------------- 2. Chapter ------------------------------------------------
------------------------------------------- 3. Infinite -----------------------------------------------

-------------------------------------------------------------------------------------------------------
''')

ma = r'''
                   __  ___ ____ _____ _____  ____ ____   _   __                      
                  /  |/  //  _// ___// ___/ /  _// __ \ / | / /                      
                 / /|_/ / / /  \__ \ \__ \  / / / / / //  |/ /                       
                / /  / /_/ /  ___/ /___/ /_/ / / /_/ // /|  /                        
               /_/  /_//___/ /____//____//___/ \____//_/ |_/                         
    ___    ______ ______ ____   __  ___ ____   __     ____ _____  __  __ ______ ____ 
   /   |  / ____// ____// __ \ /  |/  // __ \ / /    /  _// ___/ / / / // ____// __ \
  / /| | / /    / /    / / / // /|_/ // /_/ // /     / /  \__ \ / /_/ // __/  / / / /
 / ___ |/ /___ / /___ / /_/ // /  / // ____// /___ _/ /  ___/ // __  // /___ / /_/ / 
/_/  |_|\____/ \____/ \____//_/  /_//_/    /_____//___/ /____//_/ /_//_____//_____/  

'''
Wasted = r'''
▓██   ██▓ ▒█████   █    ██      █████▒▄▄▄       ██▓ ██▓    ▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██   ▒▒████▄    ▓██▒▓██▒    ▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒████ ░▒██  ▀█▄  ▒██▒▒██░    ▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▒  ░░██▄▄▄▄██ ░██░▒██░    ▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒█░    ▓█   ▓██▒░██░░██████▒░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒ ░    ▒▒   ▓▒█░░▓  ░ ▒░▓  ░░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░       ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░     ░   ▒    ▒ ░  ░ ░      ░    ░ ░  ░ 
 ░ ░         ░ ░     ░                     ░  ░ ░      ░  ░   ░  ░   ░    
 ░ ░                                                               ░      
 ██▓ ███▄    █     ██▓███ ▓██   ██▓▄▄▄█████▓ ██░ ██  ▒█████   ███▄    █   
▓██▒ ██ ▀█   █    ▓██░  ██▒▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █   
▒██▒▓██  ▀█ ██▒   ▓██░ ██▓▒ ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒  
░██░▓██▒  ▐▌██▒   ▒██▄█▓▒ ▒ ░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒  
░██░▒██░   ▓██░   ▒██▒ ░  ░ ░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓░ ████▓▒░▒██░   ▓██░  
░▓  ░ ▒░   ▒ ▒    ▒▓▒░ ░  ░  ██▒▒▒   ▒ ░░    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒   
 ▒ ░░ ░░   ░ ▒░   ░▒ ░     ▓██ ░▒░     ░     ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  
 ▒ ░   ░   ░ ░    ░░       ▒ ▒ ░░    ░       ░  ░░ ░░ ░ ░ ▒     ░   ░ ░   
 ░           ░             ░ ░               ░  ░  ░    ░ ░           ░   
                           ░ ░                                            
                         ▐██▌  ▐██▌  ▐██▌                                 
                         ▐██▌  ▐██▌  ▐██▌                                 
                         ▐██▌  ▐██▌  ▐██▌                                 
                         ▓██▒  ▓██▒  ▓██▒                                 
                         ▒▄▄   ▒▄▄   ▒▄▄                                  
                         ░▀▀▒  ░▀▀▒  ░▀▀▒                                 
                         ░  ░  ░  ░  ░  ░                                 
                            ░     ░     ░                                 
                         ░     ░     ░                                                                                                              
'''
Vic = r'''
      ___                     ___       ___          ___          ___       ___     
     /\__\         ___       /\  \     /\  \        /\  \        /\  \     |\__\    
    /:/  /        /\  \     /::\  \    \:\  \      /::\  \      /::\  \    |:|  |   
   /:/  /         \:\  \   /:/\:\  \    \:\  \    /:/\:\  \    /:/\:\  \   |:|  |   
  /:/__/  ___     /::\__\ /:/  \:\  \   /::\  \  /:/  \:\  \  /::\~\:\  \  |:|__|__ 
  |:|  | /\__\ __/:/\/__//:/__/ \:\__\ /:/\:\__\/:/__/ \:\__\/:/\:\ \:\__\ /::::\__\
  |:|  |/:/  //\/:/  /   \:\  \  \/__//:/  \/__/\:\  \ /:/  /\/_|::\/:/  //:/~~/~   
  |:|__/:/  / \::/__/     \:\  \     /:/  /      \:\  /:/  /    |:|::/  //:/  /     
   \::::/__/   \:\__\      \:\  \    \/__/        \:\/:/  /     |:|\/__/ \/__/      
    ~~~~        \/__/       \:\__\                 \::/  /      |:|  |              
                             \/__/                  \/__/        \|__|              
'''
c1 = r'''
   _____  ____   _    _  _____    _____  ______      ____   _   _  ______ 
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|    / __ \ | \ | ||  ____|
 | |    | |  | || |  | || |__) || (___  | |__      | |  | ||  \| || |__   
 | |    | |  | || |  | ||  _  /  \___ \ |  __|     | |  | || . ` ||  __|  
 | |____| |__| || |__| || | \ \  ____) || |____    | |__| || |\  || |____ 
  \_____|\____/  \____/ |_|  \_\|_____/ |______|    \____/ |_| \_||______|

'''
c2 = r'''
   _____  ____   _    _  _____    _____  ______     _______ __          __ ____  
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|   |__   __|\ \        / // __ \ 
 | |    | |  | || |  | || |__) || (___  | |__         | |    \ \  /\  / /| |  | |
 | |    | |  | || |  | ||  _  /  \___ \ |  __|        | |     \ \/  \/ / | |  | |
 | |____| |__| || |__| || | \ \  ____) || |____       | |      \  /\  /  | |__| |
  \_____|\____/  \____/ |_|  \_\|_____/ |______|      |_|       \/  \/    \____/ 


'''
c3 = r'''
   _____  ____   _    _  _____    _____  ______    _______  _    _  _____   ______  ______ 
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|  |__   __|| |  | ||  __ \ |  ____||  ____|
 | |    | |  | || |  | || |__) || (___  | |__        | |   | |__| || |__) || |__   | |__   
 | |    | |  | || |  | ||  _  /  \___ \ |  __|       | |   |  __  ||  _  / |  __|  |  __|  
 | |____| |__| || |__| || | \ \  ____) || |____      | |   | |  | || | \ \ | |____ | |____ 
  \_____|\____/  \____/ |_|  \_\|_____/ |______|     |_|   |_|  |_||_|  \_\|______||______|

'''
c4 = r'''
   _____  ____   _    _  _____    _____  ______    ______  ____   _    _  _____  
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|  |  ____|/ __ \ | |  | ||  __ \ 
 | |    | |  | || |  | || |__) || (___  | |__     | |__  | |  | || |  | || |__) |
 | |    | |  | || |  | ||  _  /  \___ \ |  __|    |  __| | |  | || |  | ||  _  / 
 | |____| |__| || |__| || | \ \  ____) || |____   | |    | |__| || |__| || | \ \ 
  \_____|\____/  \____/ |_|  \_\|_____/ |______|  |_|     \____/  \____/ |_|  \_\


'''
c5 = r'''
   _____  ____   _    _  _____    _____  ______    ______  _____ __      __ ______ 
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|  |  ____||_   _|\ \    / /|  ____|
 | |    | |  | || |  | || |__) || (___  | |__     | |__     | |   \ \  / / | |__   
 | |    | |  | || |  | ||  _  /  \___ \ |  __|    |  __|    | |    \ \/ /  |  __|  
 | |____| |__| || |__| || | \ \  ____) || |____   | |      _| |_    \  /   | |____ 
  \_____|\____/  \____/ |_|  \_\|_____/ |______|  |_|     |_____|    \/    |______|

'''
c6 = r'''
   _____  ____   _    _  _____    _____  ______     _____  _____ __   __
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|   / ____||_   _|\ \ / /
 | |    | |  | || |  | || |__) || (___  | |__     | (___    | |   \ V / 
 | |    | |  | || |  | ||  _  /  \___ \ |  __|     \___ \   | |    > <  
 | |____| |__| || |__| || | \ \  ____) || |____    ____) | _| |_  / . \ 
  \_____|\____/  \____/ |_|  \_\|_____/ |______|  |_____/ |_____|/_/ \_\


'''
c7 = r'''
   _____  ____   _    _  _____    _____  ______     _____  ______ __      __ ______  _   _ 
  / ____|/ __ \ | |  | ||  __ \  / ____||  ____|   / ____||  ____|\ \    / /|  ____|| \ | |
 | |    | |  | || |  | || |__) || (___  | |__     | (___  | |__    \ \  / / | |__   |  \| |
 | |    | |  | || |  | ||  _  /  \___ \ |  __|     \___ \ |  __|    \ \/ /  |  __|  | . ` |
 | |____| |__| || |__| || | \ \  ____) || |____    ____) || |____    \  /   | |____ | |\  |
  \_____|\____/  \____/ |_|  \_\|_____/ |______|  |_____/ |______|    \/    |______||_| \_|


'''
ff = r'''
  ______  _____  _   _            _         ______  _____  _____  _    _  _______ 
 |  ____||_   _|| \ | |    /\    | |       |  ____||_   _|/ ____|| |  | ||__   __|
 | |__     | |  |  \| |   /  \   | |       | |__     | | | |  __ | |__| |   | |   
 |  __|    | |  | . ` |  / /\ \  | |       |  __|    | | | | |_ ||  __  |   | |   
 | |      _| |_ | |\  | / ____ \ | |____   | |      _| |_| |__| || |  | |   | |   
 |_|     |_____||_| \_|/_/    \_\|______|  |_|     |_____|\_____||_|  |_|   |_|   

'''
inp = input()
if inp == '1':
    while 1:
        print(c1)
        time.sleep(3)
        if one(): break
        input('Press any key to continue')
        clearGlobal()
        print(c2)
        time.sleep(3)
        if two(): break
        input('Press any key to continue')
        clearGlobal()
        print(c3)
        time.sleep(3)
        if three(): break
        input('Press any key to continue')
        clearGlobal()
        print(c4)
        time.sleep(3)
        if four(): break
        input('Press any key to continue')
        clearGlobal()
        print(c5)
        time.sleep(3)
        if five(): break
        input('Press any key to continue')
        clearGlobal()
        print(c6)
        time.sleep(3)
        if six(): break
        input('Press any key to continue')
        clearGlobal()
        print(c7)
        time.sleep(3)
        if seven(): break
        input('Press any key to continue')
        print(ff)
        clearGlobal()
        time.sleep(3)
        if Main(): break
        break
elif inp == '2':
    chapter = input('Choose a chapter (1 - 7 or 0) ')
    if chapter in ('0', '1', '2', '3', '4', '5', '6', '7'):
        if chapter == '1': one()
        if chapter == '2': two()
        if chapter == '3': three()
        if chapter == '4': four()
        if chapter == '5': five()
        if chapter == '6': six()
        if chapter == '7': seven()
        if chapter == '0': Main()
elif inp == '3':
    while 1:
        if main() == 'Wasted':
            print(Wasted)
            break
        print_board()

