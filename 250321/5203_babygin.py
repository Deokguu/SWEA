# def run_test(arr):
#     arr = set(arr)
#     arr = list(arr)
#     for i in range(len(arr)-2):
#         if arr[i] == arr[i+1] - 1 == arr[i+2] - 2:
#             return True
#     return False
#
# def triplet_test(arr):
#     for i in range(len(arr)-2):
#         if arr[i] == arr[i+1] == arr[i+2]:
#             return True
#     return False
#
# T = int(input())
#
# for tc in range(1, T+1):
#     arr = list(map(int, input().split()))
#     player1 = []
#     player2 = []
#     result = 0
#
#     for i in range(0, len(arr), 2):
#         a, b = arr[i], arr[i+1]
#         player1.append(a)
#         player2.append(b)
#
#         player1.sort()
#         player2.sort()
#         # print(player1, player2)
#         if len(player1) >= 3:
#             if run_test(player1) or triplet_test(player1):
#                 result = 1
#                 break
#         if len(player2) >= 3:
#             if run_test(player2) or triplet_test(player2):
#                 result = 2
#                 break
#
#     print(f'#{tc} {result}')

def comb(ar, path=[]):
    if not ar:
        print(path)
        return

    for i in range(len(ar)):
        comb(ar[:i] + ar[i + 1:], path + [ar[i]])

ar = [1, 2, 3, 4]
comb(ar)