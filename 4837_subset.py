T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))

    #000000: {}, 000001: {3}, 000011: {3, 6}, 111111: {3, 6, 7, 1, 5, 4}
    cnt_final = 0
    for i in range(1<<len(arr)): # 2**6, 1 << 6

        subset_list = []
        for j in range(len(arr)):
            if i & (1<<j):
                # print(arr[j], end = ',')
                subset_list.append(arr[j])
        if len(subset_list) == N and sum(subset_list) == K:
            cnt_final += 1

    print(f'#{tc} {cnt_final}')