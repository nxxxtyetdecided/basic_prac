# 내가 정한 임의의 수 1 ~ 100
# 컴퓨터가 입력한 수 보다 크면   up
#                     작으면 down

com = [i for i in range(1, 101)]

while True:
    try:
        player = int(input("1 ~ 100 사이 숫자를 입력하세요 :"))
    except ValueError as e:
        print("조건에 맞는 값이 아닙니다.")

    start = 0
    end = 100
    mid = 0

    while player != com[mid]:
        mid = ((start + end) // 2) - 1

        if player < com[mid]:  # 중간값보다 작으면
            end = mid + 1
            result = input()
            if result != "다운":
                result = input("업 다운 다시 입력")
        elif player > com[mid]:  # 중간값보다 크면
            start = mid + 1
            result = input()
            if result != "업":
                result = input("업 다운 다시 입력")
    break
print("성공")

