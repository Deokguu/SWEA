# def my_max(list1):
#     max_num = 0
#     idx = None
#     for i in list1:
#         if max_num < list1[i]:
#             max_num = list1[i]
#             idx = i
#     return idx, max_num


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input()))

    cnts = [0] * 10

    for number in numbers:
        cnts[number] += 1
    print(cnts)

    max_num = 0
    max_idx = 0

    for i in range(len(cnts)):
        if max_num <= cnts[i]:
            max_num = cnts[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_num}')


# for i in range(9):
#     cnts[i + 1] = cnts[i] + cnts[i + 1]
# print(cnts)
#
# temp = [-1] * N
# for number in numbers:
#     # pos = cnts[number] - 1
#     # temp[pos] = number
#     # cnts[number] -= 1
#
#     cnts[number] -= 1
#     temp[cnts[number]] = number
#
# print(temp)