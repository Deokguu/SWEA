def selection_sort(a, N):

    for i in range(N-1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i+1, N):
                if a[j] > a[max_idx]:
                    max_idx = j
            a[i], a[max_idx] = a[max_idx], a[i]
            # print(a)
        elif i % 2 != 0:
            min_idx = i
            for j in range(i+1, N):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
            # print(a)


        #i가 짝수일때:
        #범위 i부터 N까지 중 제일 큰 값의 위치를 찾아서
        #i 번째와 교환
        # i가 홀수일때
        #범위 i부터 N까지 중 제일 작은 값의 위치를 찾아서
        #i번째와 교환
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection_sort(arr, N)

    print(f'#{tc}', end=' ')
    print(*arr[:10])
