def isYMD(numbers):
    thirtyone = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    twenty = [2]

    year = int(numbers[:4])
    month = int(numbers[4:6])
    day = int(numbers[6:])

    if month in thirtyone and 1<=day<=31:
        return f'{numbers[:4]}/{numbers[4:6]}/{numbers[6:]}'
    elif month in thirty and 1<=day<=30:
        return f'{numbers[:4]}/{numbers[4:6]}/{numbers[6:]}'
    elif month in twenty and 1<=day<=28:
        return f'{numbers[:4]}/{numbers[4:6]}/{numbers[6:]}'
    else:
        return -1

T = int(input())

for tc in range(1, T+1):
    numbers = input()

    print(f'#{tc} {isYMD(numbers)}')


'''
전역변수, 함수 내 변수 구분 잘하기
문자열로 받아와야 슬라이싱 가능
f스트링 써서 출력 자유롭게 하기
'''