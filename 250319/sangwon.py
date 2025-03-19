def bfs(node):
    queue = []
    queue.append(node)
    visited[node] = 1
    cnt = 0
    through_cnt = 0

    while queue:
        if through_cnt == 1+ len(graph[1]):
            break
        t = queue.pop(0)

        for k in graph[t]:
            if not visited[k]:
                queue.append(k)
                visited[k] = 1
                cnt += 1

        through_cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    visited = [0] * (N+1)
    print(f'#{tc} {bfs(1)}')
