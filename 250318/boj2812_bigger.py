def comb(depth, start):
    global max_v

    if depth == N-K:
        if max_v < int(''.join(new_lst)):
            max_v = int(''.join(new_lst))
        return
    
    for i in range(start, len(arr)):
        new_lst.append(arr[i])
        comb(depth + 1, i + 1)
        new_lst.pop()

N, K = map(int, input().split())
arr = list(input())
new_lst = []

max_v = 0
comb(0, 0)
print(max_v)


