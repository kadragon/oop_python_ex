# Tic tac toe

import random  # �������� ������ ���� �� ����ϱ� ���� random�Լ��� import�մϴ�.


def screenboard(screen):  # ������ ���� ȭ���� ����ϴ� �Լ��� def�մϴ�.
    print('   |   |')  # ĭ�� ������ ���� print�մϴ�.
    print(' ' + screen[1] + ' | ' + screen[2] + ' | ' + screen[
        3])  # �Ŀ� player �Ǵ� computer�� ���� ��ġ�� �Է¹޾� ����ϵ��� �����մϴ�.
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + screen[4] + ' | ' + screen[5] + ' | ' + screen[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + screen[7] + ' | ' + screen[8] + ' | ' + screen[9])
    print('   |   |')


def inputletter():  # player�� X�� ���� O�� ���� �Է¹޴� �Լ��� def�մϴ�.
    letter = ''  # letter�� �Է¹ޱ����� �� ������ �����մϴ�.
    while not (letter == 'X' or letter == 'O'):  # X�Ǵ� O�� �Էµ� �� ���� �ٽ� ����ϴ�.
        print('X�� O�� �ϳ��� ������.\n')  # ����ϴ�.
        letter = input().upper()  # ���ڸ� ��� �빮�ڷ� �޽��ϴ�.
    if letter == 'X':  # player�� X�� ������ ��� computer���� O�� �Ѱ��ݴϴ�.
        return ['X', 'O']
    else:  # �� ���� ��� computer���� X�� �Ѱ��ݴϴ�.
        return ['O', 'X']


def choose():  # ������ �������� ���ϴ� �Լ��� def�մϴ�.
    if random.randint(0, 1) == 0:  # �������� 0 �Ǵ� 1�� ���ڸ� ������ ������ ���մϴ�.
        return 'computer'  # �Ŀ� print��ü�� ���� ���� �����ϴ��� �˸��� ���� ���ڷ� �����մϴ�.
    else:
        return 'player'


def retry():  # ������ ���� �� �ٽ� �÷����� ������ ����� �Լ��� def�մϴ�.
    print('���� �ٽ� �÷��� �Ͻðڽ��ϱ�? (���� �Ǵ� ��¥)')  # ����ϴ�.
    return input().startswith('����')  # ���ɺ��̸� �޾��ݴϴ�.


def save(screen, letter, move):  # �÷��̾ �����̰ڴٰ� �� ĭ�� �Է¹޴� �Լ��� def�մϴ�.
    screen[move] = letter


def win(sc, le):  # �̱�� ��츦 �̸� �������ִ� �Լ��� def�մϴ�.
    return ((sc[1] == sc[2] == sc[3] == le) or (sc[4] == sc[5] == sc[6] == le) or (sc[7] == sc[8] == sc[9] == le) or (
                sc[1] == sc[4] == sc[7] == le) or (sc[2] == sc[5] == sc[8] == le) or (
                        sc[3] == sc[6] == sc[9] == le) or (sc[1] == sc[5] == sc[9] == le) or (
                        sc[3] == sc[5] == sc[7] == le))


def copyscreen(screen):  # �����̴� ĭ�� ���� �̿��ϱ� ���� �����صδ� �Լ��� def�մϴ�.
    dupescreen = []

    for i in screen:
        dupescreen.append(i)

    return dupescreen


def space(screen, move):  # �ش� ������ ������� �˷��ִ� �Լ��� def�մϴ�.
    return screen[move] == ' '


def movemove(screen):  # �����̴� �Լ��� def�մϴ�.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space(screen, int(
            move)):  # ���ڸ� �Է��� �� ����, ������ �� ĭ�� �Է��� �� ���� �ٽ� ����ϴ�.
        print('��� ���� �νǰǰ���? (1-9)\n')  # ����ϴ�.
        move = input()  # �����̰��� �ϴ� ĭ�� �Է¹޽��ϴ�.
    return int(move)


def randommove(screen, movelist):  # computer�� �������� �����̴� �Լ��� def�մϴ�.
    possiblemove = []
    for i in movelist:
        if space(screen, i):  # �� �������� Ȯ���� ��
            possiblemove.append(i)  # ������ �������� Ȯ���ϱ� ���� �־�Ӵϴ�.

    if len(possiblemove) != 0:  # �Է°����� ������ ���� �� ���� computer�� ���� �Ӵϴ�.
        return random.choice(possiblemove)
    else:  # ���ĭ�� ä������ ��� None�� �����մϴ�.
        return None


def commove(screen, comletter):  # computer�� �����̴� �������� ��쿡 ���� �Լ��� def�մϴ�.
    if comletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

    for i in range(1, 10):
        copy = copyscreen(screen)  # �����ص� ĭ�� �̿��Ͽ� �� �������� Ȯ���մϴ�.
        if space(copy, i):
            save(copy, comletter, i)
            if win(copy, comletter):  # computer�� �̱� �� �ִ� ���̸� �װ��� ���� �Ӵϴ�.
                return i

    for i in range(1, 10):
        copy = copyscreen(screen)  # �����ص� ĭ�� �̿��Ͽ� �� �������� Ȯ���մϴ�.
        if space(copy, i):
            save(copy, playerletter, i)
            if win(copy, playerletter):  # player�� ���� �ξ��� �� �̱� �� �ִ� ĭ�� �����ϴ�.
                return i

    move = randommove(screen, [1, 3, 7, 9])  # �������� �� �����ϰ�� ���� �Ӵϴ�.
    if move != None:
        return move

    if space(screen, 5):  # ��� ĭ�� ����� ��� ���� �Ӵϴ�.
        return 5

    return randommove(screen, [2, 4, 6, 8])  # ������ ĭ�� ����� ��� ���� �Ӵϴ�.


def full(screen):  # �ش��ϴ� ĭ�� ä�����ִ��� Ȯ���ϴ� �Լ��� def�մϴ�.
    for i in range(1, 10):
        if space(screen, i):
            return False
    return True


print(' ')
print('=' * 29)
print(' ')
print('Tic Tac Toe ������ �����մϴ�\n')  # ������ ������ �� ������ ���� print�մϴ�.
print('=' * 29)
print(' ')

while True:
    thescreen = [' '] * 10
    playerletter, comletter = inputletter()  # �Լ��� �ҷ��ͼ� X, O�� ������ ������ ������ �Է� �޽��ϴ�.
    turn = choose()  # �Լ��� �ҷ��ͼ� ������ ���մϴ�.
    print(turn + ' �� ���� �����մϴ�.\n')  # ������ ���� �� ���� ���� �����ϴ��� �˷��ݴϴ�.
    playing = True

    while playing:
        if turn == 'player':  # player ������ �� �����Դϴ�.
            screenboard(thescreen)
            move = movemove(thescreen)
            save(thescreen, playerletter, move)

            if win(thescreen, playerletter):  # �̱��� �̰�ٰ� �˷��ݴϴ�.
                screenboard(thescreen)
                print('�̰���ϴ�!')
                playing = False
            else:  # ���º� �ϰ�� ���ºζ�� �˷��ݴϴ�.
                if full(thescreen):
                    screenboard(thescreen)
                    print('���º�!')
                    break
                else:
                    turn = 'computer'  # �ƹ� ��Ȳ�� �ƴ� ��� computer���� ������ �Ѱ��ݴϴ�.
        else:
            move = commove(thescreen, comletter)
            save(thescreen, comletter, move)

            if win(thescreen, comletter):  # computer�� �̱��� ���ٰ� �˷��ݴϴ�.
                screenboard(thescreen)
                print('������!')
                playing = False
            else:
                if full(thescreen):  # ���º��ϰ�� ���ºζ�� �˷��ݴϴ�.
                    screenboard(thescreen)
                    print('���º�!')
                    break
                else:
                    turn = 'player'  # �ƹ��͵� �ƴҰ�� player���� ������ �Ѱ��ݴϴ�.

    if not retry():  # �ٽ����� ������� ��ü�� ����ϴ�.
        break
