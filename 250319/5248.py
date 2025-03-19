def find_set(x):
    # 자신 == 부모노드일 때 해당 집합의 대표자다
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x

def union(x, y):
    # 1. x, y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면? return
    if ref_x == ref_y:
        return
    parents[ref_y] = ref_x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]
    cnt = 0

    for i in range(len(arr)//2):
        s, e = arr[2*i], arr[2*i + 1]
        union(s, e)

    for i in range(len(parents)):
        if parents[i] == i:
            cnt += 1

    print(f'#{tc} {cnt-1}')


