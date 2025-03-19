from collections import deque

def bfs(node):
    queue = deque([node])
    queue.append(node)
    visited[node] = 1
    cnt = 0

    while queue:
        t = queue.popleft()
        if t == M:
            return visited[t] - 1

        for new_v in [t+1, t-1, t*2, t-10]:
            if 0<=new_v<=1000000 and not visited[new_v]:
                queue.append(new_v)
                visited[new_v] = visited[t] + 1

    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (1000001)
    print(f'#{tc} {bfs(N)}')