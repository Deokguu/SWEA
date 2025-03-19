def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x

def union(x, y):
    # 1. x, y 의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)

