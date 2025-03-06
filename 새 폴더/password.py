import sys
sys.stdin = open("input.txt", "r")


def find_end(arr, N, M):
    for row in range(N):
        for col in range(M - 1, -1, -1):  # 오른쪽에서 왼쪽으로 탐색
            if arr[row][col] == '1':
                return row, col



def decode_password(binary_str):
    code_dict = {
        (3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3,
        (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7,
        (1, 2, 1, 3): 8, (3, 1, 1, 2): 9
    }

    decoded_numbers = []
    for i in range(0, 56, 7):
        segment = binary_str[i:i + 7]
        decimal_value =
        decoded_numbers.append(decimal_value)

    return decoded_numbers


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]  # 입력받기

    ei, ej = find_end(arr, N, M)

    password = arr[ei][max(0, ej - 55):ej + 1]  # 최대 56자리 추출
    password_str = ''.join(password)  # 리스트 -> 문자열 변환

    decoded_numbers = decode_password(password_str)

    # print(f'#{tc} {decoded_numbers}')





















# def find_end(arr, N, M):
#     for row in range(N):
#         for col in range(M-1, -1, -1):
#             if arr[row][col] == '1':
#                 return row, col
# def test(arr):
#     code = [[3,2,1,1], [2,2,2,1], [2,1,2,2], [1,4,1,1], [1,1,3,2], [1,2,3,1], [1,1,1,4], [1,3,1,2], [1,2,1,3], [3,1,1,2]]
#     for i in range(8):
#         for k in range(7):
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     ei, ej = find_end(arr, N, M)
#     password = arr[ei][ej:ej - 56:-1][::-1]
#     password_bit = []
#     for i in range(0, 56, 7):
#         password_bit.append(password[i:i+7])
#     print(password_bit)
#
# import sys
#
# sys.stdin = open("input.txt", "r")

