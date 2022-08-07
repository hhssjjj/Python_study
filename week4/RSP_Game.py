#가위바위보 하기

# import random

# rsp = ['rock', 'sissor', 'paper']
# my_rsp = input('가위바위보 게임을 시작할까요? 가위:s, 바위:r, 보:p \n')
# ai_choice = random.choice(rsp)

# print(ai_choice)

#(1) 랜덤 기능, 딕셔너리 기능으로 컴퓨터와 가위바위보 하기
import random
# 가위바위보 1회만 가능
def RSPGame():
    rsp = ['rock', 'sissor', 'paper']
    my_rsp = input('가위바위보 게임을 시작할까요? 가위:s, 바위:r, 보:p \n')

    dict_rsp = {'r': 'rock', 's': 'sissor', 'p': 'paper'}  # 딕셔너리 기능
    ai_choice = random.choice(rsp) # 랜덤 기능
    my_choice = dict_rsp.get(my_rsp)

    print('AI:%s'%ai_choice)
    print('MY:%s'%my_choice)
    if my_choice == None:
        print('무효입니다.')
        game_result = 'Err'
    if my_choice == ai_choice:
        print('비겼습니다.')
        game_result = 0
    elif (my_choice == 'rock' and ai_choice == 'sissor') or \
        (my_choice == 'paper' and ai_choice == 'rock') or \
        (my_choice == 'sissor' and ai_choice == 'paper'):
        print('당신이 이겼습니다.')
        game_result = 1
    else:
        print('AI가 이겼습니다.')
        game_result = -1
    return game_result

#가위바위보 내가 원하는 만큼 정해서 사용자 함수정의할 수 있음 (다회성)
def getStartRSPGame(cnt):
    i = 0
    game_result_set = []
    while i < cnt:
        game_result = RSPGame()
        game_result_set.append(game_result)
        i += 1

    print(game_result_set)
    print("승:{} 패:{} 무승부:{}".format(game_result_set.count(1),\
                                    game_result_set.count(-1),\
                                    game_result_set.count(0)))




#넘무 어려워요~ ㅠㅠ






