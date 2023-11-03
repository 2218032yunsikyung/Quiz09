트리_높이 = int(input("크리스마스 트리의 높이를 입력하세요: "))

for i in range(트리_높이):
    공백 = 트리_높이 - i - 1
    별표 = 2 * i + 1

    for j in range(공백):
        print(' ', end='')

    for j in range(별표):
        print('*', end='')

    print()





