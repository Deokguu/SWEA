'''
위상정렬
진입과 진출이란 개념을 알아야함
진입차수를 기준으로 보는 문제
백준 1766 큐 대신 우선순위 큐(힙큐)
'''
def solve():
    result = []
    q = []
    for i in range(1, V+1):
        if IN[i] == 0:
          q.append(i)
    while q:
        v = q.pop(0)
        result.append(v)

        for i in range(V+1):
            if G[v][i]:
                IN[i] -= 1
                if IN[i] == 0: #처리가 끝나면
                    q.append(i)
    print(result)


T = 1

for tc in range(1, T+1):
    V, E= map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[0] * (V+1) for _ in range(V+1)] #인접 행렬
    IN = [0] * (V+1)

    for i in range(0, len(arr), 2):
        s, e =arr[i], arr[i+1]
        G[s][e] = 1
        IN[e] += 1 #진입 개수 세기

