def todec(s, bit): # 10진수로 바꾸기
    value = 0
    for c in s:
        if c.isdigit():
            value = (value * bit) + int(c)
        else:
            mapp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
            value = (value * bit) + mapp[c]
    return value


def decto(value, bit, length):  # 10진수를 다른 진법으로 변환
    if value == 0:
        return "0".zfill(length)

    result = ""

    while value:
        remain = value % bit
        value //= bit
        result = str(remain) + result

    return result.zfill(length)

T = int(input())

for tc in range(1, T + 1):
    N, words = input().split()
    N = int(N)  # N은 문자열 길이
    decimal_value = todec(words, 16)  # 16진수를 10진수로 변환
    binary_length = N * 4  # 16진수 한 자리는 2진수 4자리
    binary_value = decto(decimal_value, 2, binary_length)  # 10진수를 2진수로 변환
    print(f'#{tc} {binary_value}')

