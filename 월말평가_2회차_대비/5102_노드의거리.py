def bfs(V, s, g):
    queue = []
    visited = [0] * (V+1)
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)
        if t == g:
            return visited[g] - 1 
        for i in G[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)
    s, g = map(int, input().split())

    print(f'#{tc} {bfs(V, s, g)}')

    '''
    노드 간 방향성!!!!!!! 체크 !!!!!!!!!
    '''