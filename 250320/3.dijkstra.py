def dijkstra(start_node):
    pq = [(0, start_node)] #누적거리, 노드번호
    dists = [INF] * V # 누적거리 저장할 리스트
    dists[start_node] = 0 # 시작 노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist : #이미 더 작은 경로로 온 적이 있다면 pass
            continue

        for next_info in graph[node]:
            next_dist = next_info[0] #다음 노드로 가기위한 가중치
            next_node = next_info[1] #다음 노드 번호

            #다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist
            #이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if new_dist >= dists[next_node]:
                continue
            dists[next_node] = new_dist #next_node까지 도착하는 데 비용은 new_dist
            heapq.heappush(pq, (new_dist, next_node))




import heapq
INF = int(21e8) #21억으로 무한대를 의미

V, E = map(int, input().split())
start_node = 0 #출발노드는 문제에 따라 다름
graph = [[] for _ in range(V)] #인접리스트로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v]) #왼쪽이 가중치 오른쪽이 도착노드번호


    #result_dists 0에서 출발해서, 다른 노드들까지의 최단 거리를 모두 구한다.
    result_dists = dijkstra(0)