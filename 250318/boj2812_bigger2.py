def comb(depth, start, new_lst, max_v):
    if depth == N-K:
        if max_v < int(''.join(new_lst)):
            max_v = int(''.join(new_lst))
        return max_v
    
    for i in range(start, len(arr)):
        new_lst.append(arr[i])
        comb(depth + 1, i + 1, new_lst, max_v)
        new_lst.pop()
    return max_v

N, K = map(int, input().split())
arr = list(input())


print(comb(0, 0, [], 0))


