def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2     # 2로 나눈 나머지
        binary_number = str(remain) + binary_number     #나머지가 앞으로 들어옴
        target = target // 2    # 2로 나눈다.
    print(binary_number)
def binary_to_dec(binary_str):
    # binary_str 문자열 뒤에서부터 진행
    # 각 자리에 맞는 수를 곱하면서, 결과에 더한다.
    decimal_number = 0
    pow = 0
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
            pow += 1
        else:
            pow += 1

    print(decimal_number)


def decimal_to_hexadecimal(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ''

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16
    print(hex_number)
target = 74
binary_to_dec("1001010")
decimal_to_hexadecimal((256))

def decto(value, bit): #10진수에서 다른 걸로 바꾸기
    result = ''
    while value:
        remain = value % bit
        value = value // bit
        if remain < 10:

        # print(value, remain)
            result = str(remain) + result
        else:
            mapp = {10:'A', 11:'B',12:'C', 13:'D', 14:'E', 15:'F'}
            result = str(remain) + result


def todec(s, bit): # 10진수로 바꾸기
    value = 0
    # 149 = ((1*10) + 4)
    for c in s:
        if c.isdigit():
            value = (value * bit) + int(c)
        else:
            mapp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
            value = (value * bit) + mapp[c]
            return value
#10진수를 거쳐 다른걸로 넘어가면 편함!

value = '149'
todec(value, 10)

#연습문제
for i in range(0, len(s), 7):
    sub = s[i:i+7]
    print(todec(s_sub, 2))