def dfs(n, arr):
    stack = []
    visited = [0] * (N+1)
    stack.append(n)
    visited[n] = 1
    cnt = 1

    while stack:
        t = stack.pop()

        for i in range(len(arr[t])):
            if not visited[arr[t][i]]:
                stack.append(arr[t][i])
                visited[arr[t][i]] = 1
                cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    max_cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, N+1):
        result = dfs(i, graph)
        if max_cnt < result:
            max_cnt = result
    print(f'#{tc} {max_cnt}')








#스택으로 풀기
'''
분기마다(각 노드마다) visited 방문처리한 노드들을 따로 기록하면서 나아가야 함
'''


def dfs_stack(start, graph):
    global max_length
    stack = [(start, [start])]  # (현재 노드, 방문 경로 리스트)

    while stack:
        node, path = stack.pop()
        max_length = max(max_length, len(path))  # 현재까지 방문한 노드 개수 갱신

        for neighbor in graph[node]:
            if neighbor not in path:  # 이미 방문한 노드는 제외 (백트래킹)
                stack.append((neighbor, path + [neighbor]))  # 새로운 경로 추가


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)  # 무방향 그래프

    max_length = 0

    for i in range(1, N + 1):  # 모든 정점에서 시작하여 최장 경로 탐색
        dfs_stack(i, graph)

    print(f'#{tc} {max_length}')
