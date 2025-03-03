def dfs(V, s, g):
    stack = []
    visited = [False] * (V+1)
    stack.append(s)
    visited[s] = True

    while stack:
        t = stack.pop()
        for i in G[t]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
    if visited[g] == True:
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
    s, g = map(int, input().split())        
    print(f'#{tc} {dfs(V, s, g)}')
