'''
간선 위주 알고리즘
    1. 간선들을 정렬하고 2. 최소 간선들을 뽑고 3. 사이클 검사


'''
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y: # 노드 번호가 더 큰 쪽으로 병합
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())
    parents = [i for i in range(N)]
    sum_weight = 0

    edges = []
    for i in range(N):
        for j in range(i+1, N):
            cost = ((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2) * tax
            edges.append((cost, i, j)) # (weight, 노드1, 노드2)

    edges.sort()

    cnt = 0 #최소신장트리의 간선 개수

    for weight, node1, node2 in edges:
        if find_set(node1) != find_set(node2):
            union(node1, node2)
            sum_weight += weight
            cnt += 1

            if cnt == N-1:
                break
    print(f'#{tc} {sum_weight:.0f}')


