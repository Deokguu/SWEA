'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
13
2 1 2 3 1 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])

V = int(input())
E = V-1
arr = list(map(int, input().split()))

left = [0] * (V+1)
right = [0] * (V+1)
parent = [0] * (V+1)

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    parent[c] = p

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

root = 1
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break
pre_order(root)