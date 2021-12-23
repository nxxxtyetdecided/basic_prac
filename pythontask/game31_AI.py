import random as r

sum = 0

def com_num(sum):
    c_num = 0

    if sum % 4 == 0:
        c_num = 2
    elif sum % 4 == 1:
        c_num = 1
    elif sum % 4 == 3:
        c_num = 3

    for _ in range(c_num):
        sum += 1
        print(f"컴퓨터 : {sum}")
        if sum == 31:
            break
    return sum

def player_num(sum):
    while True:
        p_num = int(input('숫자를 입력하세요 : '))
        if p_num > 3: # 3 이상의 숫자가 입력되면
            print("다시 입력해주세요")
        else: # 잘 입력 됐으면 while문 빠져나오기
            break

    for _ in range(p_num):
        sum += 1
        print(f"플레이어 : {sum}")
        if sum == 31:
            break
    return sum


turn = r.randrange(2)
print(f'순서 : {turn}')

while sum < 31:
    if turn == 0:
        sum = com_num(sum)
        turn += 1 # 플레이어 순서로 넘기기
    elif turn == 1:
        sum = player_num(sum)
        turn -= 1 # 컴퓨터 순서로 넘기기


if turn == 0:
    print("컴퓨터 승리")
else:
    print("사용자 승리")