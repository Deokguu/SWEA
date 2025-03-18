'''
def recur(stop, remain, cnt):
    #현재 정류장에서의 동작을 기술
    
    #현재 정류장에서 충전안한경우 다음 정류장의 상태:
    recur(stop+1, remain-1, cnt)
    
    #현재 정류장에서 충전한 경우
    recur(stop+1, arr[stop]-1, cnt+1)
'''
def recur(depth, remain, cnt):
    global min_v
    if min_v < cnt:
        return

    if remain < 0:
        return

    if depth == N:
        if min_v > cnt:
            min_v = cnt
        return
    #현재 정류장에서 충전하지 않은 경우 다음 정류장
    recur(depth+1, remain - 1, cnt)

    #현재 정류장에서 충전한 경우
    recur(depth+1, arr[depth-1] - 1, cnt + 1)

T = int(input())

for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    # print(arr)
    min_v = 10e10
    recur(1,arr[0],0)
    print(f'#{tc} {min_v}')