import sys
sys.stdin = open("graph.txt", "r")

N, M = map(int, input().split()) # 정점 수, 간선 수
# 1. 그래프 저장하기
#   비어있는 그래프를 생성한다.
#   그래프 정보를 입력받아 넣는다.
# graph = [[0] * N for _ in range(N + 1)] # 1. 인접 행렬(N*N의 0배열) 또는 2. 인접리스트(N*N([]))
# for row in graph:
#     print(*row)

def dfs(node): # 재귀 호출로 구현 / 재귀호출인데도 종료조건이 없다.
    # 보통 그래프 문제들에서 여기서 가지치기가 들어감
    # ex) K개의 노드를 방문했다면 종료
    # ex) N개를 모두 방문했다면 경로 출력
    # return
    print(node, end = " ")
    # 현재 노드에서 인접한(내가 갈 수 있는 후보들)노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node] = 1
        dfs(next_node)

# 인접 리스트
graph = [[] for _ in range(N + 1)]
# for row in graph:
#     print(row)
for _ in range(M):
    s, e =map(int,input().split())
    graph[s].append(e)
    graph[e].append(s) #양방향이라면, 뒤집어서 저장해주어야 한다.

visited = [0] * (N + 1) #방문 여부 기록 / N+1인 이유는 0번을 버려서
visited[1] = 1 # 출발점 초기화
dfs(1)