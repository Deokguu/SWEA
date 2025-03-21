'''
Prim 형식으로 풀거임

모든 섬(모든 정점)을 연결하는데,, 최소 간선수 or 최소비용(가중치 최소) -> MST
keyword : 환경부담금 최소로 지불, N개의 모든 섬 연결 => MST

(비용, 노드) 형태로 저장
방문 처리 해주고 이미 간 정점은 패스
최소비용 저장 리스트도 만들어야함

기존에 우선순위큐에 삽입된 거리를 저장하면서 진행
더 작은 비용으로 갈 수 있을 때만 heapq에 삽ㅇ비
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())