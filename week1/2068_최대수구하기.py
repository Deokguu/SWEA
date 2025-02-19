T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    max_v = 0

    for v in arr:
        if max_v < v:
            max_v = v
    print(f'#{tc} {max_v}')