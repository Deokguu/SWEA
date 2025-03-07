print(7&5)
print(7|5)

#1. 이진수로 변환
#2. 각 자리를 and, or 연산한다.

# print(bin(7&5))
# print(hex(10))
#
# print(int('10111',2))
# print(int('b', 16))
#
# secret_code = 1004
# print(7070 ^ secret_code)
# print(6258 ^ secret_code)
#
# num = 1
# for _ in range(5):
#     print(num, bin(num))
#     num = num << 1

#1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4] # 16개
print(f'부분집합의 수 : {1<<len(arr)}')

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # (1<<idx) : ob1, 0b10, 0b100, 0b1000
        #i의 idx 번째 bit가 1인지 확인(부분 집합에 포함되어 있는지 확인)
        if i & (1<<idx):
            print(arr[idx], end = " ")
    print()

# arr = [1,2,3,4,5,6]
# for i in range(1 << len(arr)):
#     subset = []
#     total = 0
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             subset.append(arr[idx])
#             total += arr[idx]
#     if total == 10:
#         print(f'부분집합: {subset}')
# i = '10'
# j = int(i,2) # 2진수로 i를 해석하는 것

