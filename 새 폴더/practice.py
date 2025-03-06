# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
#
# Tree = [[] for _ in range(N+1)]
# lst = list(map(int, s.split()))
# for i in range(0, len(lst), 2):
#     p = lst[i]
#     c = lst[i+1]
#     Tree[p].append(c)
#
# print(Tree)
# root = 1
#
# def pre_order(T):
#     print(root)
#     if len(Tree[root]) > 0:
#         pre_order(Tree[root][0])
#     if len(Tree[root]) > 1:
#         pre_order(Tree[root][1])
#
# pre_order(1)

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

Tree = [[0,0] for _ in range(N+1)]
def post_order(T):
    post_order(Tree[T][0])
    