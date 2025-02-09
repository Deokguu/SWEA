T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) #건물 높이 모음

    for _ in range(N):
        max_num = 0
        min_num = 101
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if max_num < arr[i]:
                max_num = arr[i]
                max_idx = i

            if min_num > arr[i]:
                min_num = arr[i]
                min_idx = i

        arr[max_idx] -= 1
        arr[min_idx] += 1
    answer = max(arr) - min(arr)
    print(f'#{tc} {answer}')


