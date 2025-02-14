def dfs(v, E): # v출발, N 마지막 정점
    visited = [False] * (N+1) #방문표시
    stack = [] # 스택
    stack.append(v)

    while stack:
        now = stack.pop()
        if now == E:
            return 1

        visited[now] = True
        for node in adj_list[now]:
            if not visited[node]:
                stack.append(node)
    return 0





T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        graph.extend(list(map(int, input().split())))
    S, G = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        v, w = graph[i*2], graph[i*2+1]
        adj_list[v].append(w)

    print(f'#{tc} {dfs(S, G)}')