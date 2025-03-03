def switch(arr, i, j, N):
    for t in range(1,j+1):
        if 0<=i-t<N and 0<=i+t<N:
            if arr[i-t] == arr[i+t]:
                if arr[i-t] == 1:
                    arr[i-t], arr[i+t] = 0, 0
                elif arr[i-t] == 0:
                    arr[i-t], arr[i+t] = 1, 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N돌의 수 M 뒤집기 횟수수
    arr = list(map(int, input().split())) #돌 초기상태
    for _ in range(M):
        i, j = map(int, input().split())
        i= i-1
        switch(arr, i, j, N)
    
    print(f'#{tc}', *arr)

'''
입력은 1-based지만, 리스트는 0-based이므로 변환.
'''