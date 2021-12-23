# 컴퓨터가 정한 임의의 수 1 ~ 100
# 내가 입력한 수 보다 크면   up
#                  작으면 down

import random
com = random.randrange(1,101)

for i in range(5):
    try:
        player = int(input("1 ~ 100 사이 숫자를 입력하세요 :"))
    except ValueError as e:
        print("조건에 맞는 값이 아닙니다.")
    print(com, player)
    if (i == 4) and (com != player):
        print("실패")
        break
    elif com == player:
        print("성공")
        break
    elif com > player:
        print("업")
    elif com < player:
        print("다운")
