T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N개의 카드
    arr = input().split()

    mid = N //2
    new_arr = []
    
    if N % 2 == 0:
        for i in range(mid):
            new_arr.append(arr[i])
            new_arr.append(arr[i+mid])
    else:
        for i in range(mid+1):
            new_arr.append(arr[i])
            if i+mid+1 < N:
                new_arr.append(arr[i+mid+1])
    print(f'#{tc}', *new_arr)



