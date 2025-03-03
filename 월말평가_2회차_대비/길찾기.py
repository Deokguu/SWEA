def dfs(V):
    stack = []
    visited = [False] * (V+1)
    stack.append(0)
    visited[0] = True

    while stack:
        t = stack.pop()

        for i in G[t]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
    if visited[99] == True:
        return 1
    else:
        return 0
    
T = 10

for tc in range(1, T+1):
    tc_number, E = map(int, input().split())
    G = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(2 * E):
        if i%2 == 0:
            v1, v2 = arr[i], arr[i+1]
            G[v1].append(v2)
    print(f'#{tc} {dfs(99)}')
    