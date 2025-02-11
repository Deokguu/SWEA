T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = input().split('0')

    # print(arr)
    max_v = 0
    for idx in range(len(arr)):
        if len(arr[idx]) > max_v:
            max_v = len(arr[idx])
    
    print(f'#{tc} {max_v}')

