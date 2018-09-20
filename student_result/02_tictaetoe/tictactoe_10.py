import random

comp_T='[computer]: '
Play_T='\n[Player]: '

#보드 그리기
def this_function_will_draw_the_board(a_long_thin_fl):
    print('')
    print('        ==========================    [Numbering]')
    print('                |        |            7 8 9')
    print('            ' + a_long_thin_fl[7] + '  ' + ' | ' + '   ' + a_long_thin_fl[8] + '  ' + ' | ' + '   ' + a_long_thin_fl[9] + '       4 5 6')
    print('                |        |            1 2 3')
    print('        --------------------------')
    print('                |        |        ')
    print('            ' + a_long_thin_fl[4] + '  ' + ' | ' + '   ' + a_long_thin_fl[5] + '  ' + ' | ' + '   ' + a_long_thin_fl[6] + '  ')
    print('                |        |        ')
    print('        --------------------------')
    print('                |        |        ')
    print('            ' + a_long_thin_fl[1] + '  ' + ' | ' + '   ' + a_long_thin_fl[2] + '  ' + ' | ' + '   ' + a_long_thin_fl[3] + '  ')
    print('                |        |        ')
    print('        ==========================')
    print('')

#어떤 문자를 선택할지
def this_function_ask_user_to_choose_between_dad_or_mom_nnnnn_X_or_O():
    letter = input(comp_T+'X랑 O중에서 골라봐'+Play_T).upper()
    wrong_cnt=0
    while not (letter =='X' or letter =='O'):
        wrong_cnt+=1
        if wrong_cnt>5:
            letter = input(comp_T+'응~ 어디 니 마음대로 쳐봐~'+Play_T).upper()
        else :
            message = random.choice(['아니 그거 말고... 하.. 다시 골라봐', '사람이세요? O랑 X중에 고르라고','O X 구별 못함????'])
            letter = input(comp_T+message+Play_T).upper()
    if letter =='X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
#누가 먼저 할 지
def Who_wanna_be_the_first_return_str_Computer_Player():
    if random.randint(0,1)==0:
        return 'Computer'
    else:
        return 'Player'

#다시 할 지
def this_function_ask_user_to_want_to_play_again_return_bool_true_or_false(state):
    #컴퓨터가 진경우
    if not state:
        input(comp_T+'틱택토 뭐같이 하네 ㄹㅇ 다시 해'+Play_T).startswith('n')
    #컴퓨터가 이긴경우
    else:
        return input(comp_T+'ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 한 판 더 ㄱ?'+Play_T).startswith('n')
    
#보드위에 두게 하자
def this_function_make_move_and_its_not_return_anything(a_long_thin_fl, letter, move):
    a_long_thin_fl[move] = letter


#어디 둘 지 입력받기
def this_function_will_ask_player_to_where_do_you_wanna_check_return_int_player_checked(a_long_thin_fl):
    move = input(comp_T+'니 턴 ㅇㅇ(1-9)'+Play_T)
    wrong_cnt=0
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not this_function_will_return_the_board_is_empty_return_bool(a_long_thin_fl, int(move)):
        wrong_cnt+=1
        #이상하게 입력한 횟수 5회 초과시
        if wrong_cnt>5:
            move = input(comp_T+'응~ 어디 니 마음대로 쳐봐~'+Play_T).upper()
        else :
            message = random.choice(['아니 숫자도 못읽냐 ㅉ', '손가락에 살찜?', '못 이길거 같으니깐 아무거나 막치죠?'])
            move = input(comp_T+message+Play_T)
    return int(move)

#이겼나?
def this_function_determin_the_letter_won_or_not_return_bool(a_long_thin_fl, letter):
    return (
        (a_long_thin_fl[7] == letter and a_long_thin_fl[8] == letter and a_long_thin_fl[9] == letter) or   #상단가로
        (a_long_thin_fl[4] == letter and a_long_thin_fl[5] == letter and a_long_thin_fl[6] == letter) or   #중앙가로
        (a_long_thin_fl[1] == letter and a_long_thin_fl[2] == letter and a_long_thin_fl[3] == letter) or   #하단가로
        (a_long_thin_fl[7] == letter and a_long_thin_fl[4] == letter and a_long_thin_fl[1] == letter) or   #좌측세로
        (a_long_thin_fl[8] == letter and a_long_thin_fl[5] == letter and a_long_thin_fl[2] == letter) or   #중앙세로
        (a_long_thin_fl[9] == letter and a_long_thin_fl[6] == letter and a_long_thin_fl[3] == letter) or   #우측세로
        (a_long_thin_fl[7] == letter and a_long_thin_fl[5] == letter and a_long_thin_fl[3] == letter) or   #우하향대각
        (a_long_thin_fl[9] == letter and a_long_thin_fl[5] == letter and a_long_thin_fl[1] == letter))     #우상향대각

#보드 복사
def this_function_copy_the_input_board_and_return_the_same_board(a_long_thin_fl):
    d_Board = []

    for _ in a_long_thin_fl:
        d_Board.append(_)
    return d_Board

#보드 그 위치가 비었나?
def this_function_will_return_the_board_is_empty_return_bool(a_long_thin_fl, move):
    return a_long_thin_fl[move] == ' '

#주어진 리스트에서 둘 수 있는 곳에 랜덤으로 두자
def this_function_will_pick_some_places_and_checking_that_can_be_placed_return_int(a_long_thin_fl, movesList):
    possibleMoves = []

    for _ in movesList:
        if this_function_will_return_the_board_is_empty_return_bool(a_long_thin_fl, _):
            possibleMoves.append(_)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#컴퓨터가 둘 곳
def this_function_will_determin_where_computer_will_place_return_int_range_1_to_9(a_long_thin_fl, compLetter):
    if compLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'


    copy = this_function_copy_the_input_board_and_return_the_same_board(a_long_thin_fl)

    #이길거 같으면 끝내라
    if(this_function_will_return_the_board_is_empty_return_bool(copy,1)) and (compLetter==copy[2]==copy[3] or compLetter==copy[5]==copy[9] or compLetter==copy[4]==copy[7]):
        return 1
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,2)) and (compLetter==copy[1]==copy[3] or compLetter==copy[5]==copy[8]):
        return 2
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,3)) and (compLetter==copy[1]==copy[2] or compLetter==copy[6]==copy[9] or compLetter==copy[5]==copy[7]):
        return 3
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,4)) and (compLetter==copy[1]==copy[7] or compLetter==copy[5]==copy[6]):
        return 4
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,5)) and (compLetter==copy[1]==copy[9] or compLetter==copy[2]==copy[8] or compLetter==copy[3]==copy[7] or compLetter==copy[4]==copy[6]):
        return 5
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,6)) and (compLetter==copy[4]==copy[5] or compLetter==copy[3]==copy[9]):
        return 6
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,7)) and (compLetter==copy[1]==copy[4] or compLetter==copy[5]==copy[3] or compLetter==copy[8]==copy[9]):
        return 7
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,8)) and (compLetter==copy[7]==copy[9] or compLetter==copy[5]==copy[2]):
        return 8
    elif(this_function_will_return_the_board_is_empty_return_bool(copy,9)) and (compLetter==copy[1]==copy[5] or compLetter==copy[3]==copy[6] or compLetter==copy[7]==copy[8]):
        return 9
    #먼저 귀
    move = this_function_will_pick_some_places_and_checking_that_can_be_placed_return_int(a_long_thin_fl, [1, 3, 7, 9])
    if move != None:
        return move

    #다음 변
    move = this_function_will_pick_some_places_and_checking_that_can_be_placed_return_int(a_long_thin_fl, [2, 4, 6, 8])
    if move != None:
        return move

    #마지막 천원
    return 5

#보드가 가득 찼는지
def this_function_will_check_the_board_is_full_returb_bool(a_long_thin_fl):
    for _ in range(1,10):
        if this_function_will_return_the_board_is_empty_return_bool(a_long_thin_fl, _):
            return False
    return True

#메인입니다 ><
while True:
    #보드 리셋
    this_value_mean_the_plate_which_is_game_ = [' '] * 10
    playerLetter, compLetter = this_function_ask_user_to_choose_between_dad_or_mom_nnnnn_X_or_O()
    turn = Who_wanna_be_the_first_return_str_Computer_Player()
    #턴에 따른 출력 메세지
    if turn == 'Computer':
        message = random.choice(['나 선 ㅅㄱㅇ','나 먼저함 ㅇㅇ','먼저 놓는 사람이 유리함 ^오^'])
        print(comp_T+message)
    else :
        print(comp_T+'너 먼저해도 내가 이김 ㅅ')
    is_the_game_was_end_or_not_end_a_Ha_its_commencing_now = True

    #게임이 진행중이면
    while is_the_game_was_end_or_not_end_a_Ha_its_commencing_now:
        # 플레이어 턴
        if turn == 'Player':
            this_function_will_draw_the_board(this_value_mean_the_plate_which_is_game_)
            move = this_function_will_ask_player_to_where_do_you_wanna_check_return_int_player_checked(this_value_mean_the_plate_which_is_game_)
            this_function_make_move_and_its_not_return_anything(this_value_mean_the_plate_which_is_game_, playerLetter, move)

            #플레이어가 이겼다면
            if this_function_determin_the_letter_won_or_not_return_bool(this_value_mean_the_plate_which_is_game_, playerLetter):
                this_function_will_draw_the_board(this_value_mean_the_plate_which_is_game_)
                print(comp_T+'이기니깐 좋냐? ㅋㅋㅋㅋㅋㅋㅋ')
                is_the_game_was_end_or_not_end_a_Ha_its_commencing_now == False
                break
            #아니면 유감
            else:
                if this_function_will_check_the_board_is_full_returb_bool(this_value_mean_the_plate_which_is_game_):
                    this_function_will_draw_the_board(this_value_mean_the_plate_which_is_game_)
                    print(comp_T+'와 이걸 못이기네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                    break
                else:
                    turn = 'Computer'

        # 컴퓨터 턴
        else:
            move = this_function_will_determin_where_computer_will_place_return_int_range_1_to_9(this_value_mean_the_plate_which_is_game_, compLetter)
            this_function_make_move_and_its_not_return_anything(this_value_mean_the_plate_which_is_game_, compLetter, move)

            #컴퓨터가 이기면
            if this_function_determin_the_letter_won_or_not_return_bool(this_value_mean_the_plate_which_is_game_, compLetter):
                this_function_will_draw_the_board(this_value_mean_the_plate_which_is_game_)
                print(comp_T+'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이걸 지냐 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                is_the_game_was_end_or_not_end_a_Ha_its_commencing_now = False
                break
            else:
                if this_function_will_check_the_board_is_full_returb_bool(this_value_mean_the_plate_which_is_game_):
                    this_function_will_draw_the_board(this_value_mean_the_plate_which_is_game_)
                    print(comp_T+'와 이걸 못이기네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                    break
                else:
                    turn = 'Player'

    #계속할 지 물어봅니다
    if this_function_ask_user_to_want_to_play_again_return_bool_true_or_false(this_function_determin_the_letter_won_or_not_return_bool(this_value_mean_the_plate_which_is_game_, compLetter)):
        break