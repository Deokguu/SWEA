def multiply(arr1, arr2, N, M):
    max_v = -10e10
    
    for i in range(M-N+1):
        total = 0
        for m in range(N):
            total += arr1[m] * arr2[i+m]
        if max_v < total:
            max_v = total
    return max_v
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    if N > M:
        arr1, arr2 = arr2, arr1
        N, M = M, N
    print(f'#{tc} {multiply(arr1, arr2, N, M)}')

'''
max_v
최솟값이 얼마인지 잘 생각해보고 초기값 설정

arr1, arr2 배열을 바꿔주려면 배열의 크기변수인 N, M도 같이 바꿔줘라
'''