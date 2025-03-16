import sys
sys.stdin = open("input.txt", "r")

def find_end(arr, N, M):
    for row in range(N):
        for col in range(M-1, -1, -1):
            if arr[row][col] == '1':
                return row, col
def test(arr):
    real_password = []
    code = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    for i in range(8):
        if arr[i] in code:
            real_password.append(code[arr[i]])
    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += real_password[i]
        else:
            even += real_password[i]
    if (odd * 3 + even) % 10 == 0:
        return sum(real_password)
    else:
        return 0
    
    
    # return real_password
        


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ei, ej = find_end(arr, N, M)
    password = arr[ei][ej:ej-56:-1][::-1]
    password_bit = []
    for i in range(0, 56, 7):
        password_bit.append(''.join(password[i:i+7]))
    
    print(f'#{tc} {test(password_bit)}')

















# def find_end(arr, N, M):
#     for row in range(N):
#         for col in range(M - 1, -1, -1):  # 오른쪽에서 왼쪽으로 탐색
#             if arr[row][col] == '1':
#                 return row, col



# def decode_password(binary_str):
#     code_dict = {
#         (3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3,
#         (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7,
#         (1, 2, 1, 3): 8, (3, 1, 1, 2): 9
#     }

#     decoded_numbers = []
#     for i in range(0, 56, 7):
#         segment = binary_str[i:i + 7]
#         decimal_value =
#         decoded_numbers.append(decimal_value)

#     return decoded_numbers


# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(input().strip()) for _ in range(N)]  # 입력받기

#     ei, ej = find_end(arr, N, M)

#     password = arr[ei][max(0, ej - 55):ej + 1]  # 최대 56자리 추출
#     password_str = ''.join(password)  # 리스트 -> 문자열 변환

#     decoded_numbers = decode_password(password_str)

#     # print(f'#{tc} {decoded_numbers}')









