V, E = map(int, input().split())

'''
크루스칼
모든 간선들을 보면서 가중치가 작은 간선부터 고르자 (정렬)
이때 사이클이 발생하면 pass
'''
def find_set(x): #대표자 찾기
    if x == parents[x]:
        return x
    return find_set(parents[x])

def union(x, y): #집합 합치기
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y: #사이클 방지
        return
    #일정한 규칙으로 연결하자
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    #간선에 대한 정보들을 저장함
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(V)] #make_set (정점 기준으로 만들어준다)

#작은 것부터 고르면서 나아가자
# N-1 개를 선택할 때까지
cnt = 0 #현재까지 선택한 간선의 수
result = 0 # MST 가중치 합

for u, v, w in edges:
    #u와 v가 연결이 안되어 있으면 선택, 즉 다른 집합이라면
    if find_set(u) != find_set(v):
        union(u,v)
        cnt += 1
        result += w

        if cnt == V - 1: # MST 구성이 끝났다.
            break
