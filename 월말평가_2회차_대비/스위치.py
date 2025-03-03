def switch(arr1, arr2):
    cnt = 0
    for i in range(N):
        if arr1[i] == arr2[i]:
            continue
        else: #다르면
            cnt += 1
            for k in range(i, N):
                if arr1[k] == 0:
                    arr1[k] = 1
                elif arr1[k] == 1:
                    arr1[k] = 0
    return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #스위치 개수
    arr_before = list(map(int, input().split()))
    arr_after = list(map(int, input().split()))

    print(f'#{tc} {switch(arr_before, arr_after)}')

