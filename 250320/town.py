def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x


def union(x, y):
    # 1. x, y 의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면 ?
    # -> 끝!
    if ref_x == ref_y:
        return

    # rank 가 큰 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # rank 가 같으면 한 쪽으로 병합하고, 대표자의 rank 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    ranks = [0] * (N+1)
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for i in range(len(parents)):
        if parents[i] == i:
            cnt += 1
    print(f'#{tc} {cnt-1}')


