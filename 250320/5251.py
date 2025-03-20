def dijkstra(start_node):
    pq = [(0, start_node)]
    distances = [INF] * (N+1)
    distances[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if distances[node] < dist: # 더 작은 경로로 온 적이 있으면 패스
            continue

        for next_info in graph[node]:
            next_dist = next_info[0] #다음 노드로 가기 위한 가중치
            next_node = next_info[1] #다음 노드 번호

            new_dist = dist + next_dist #누적거리에 가중치 더해줌

            if distances[next_node] <= new_dist:
                continue

            distances[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return distances[N]
import heapq
INF = int(21e8)

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split()) #마지막 정점번호 E간선 개수
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e]) #가중치, 도착지 노드번호

    result = dijkstra(0)
    print(f'#{tc} {result}')

