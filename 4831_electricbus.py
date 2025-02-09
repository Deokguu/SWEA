def check():

    for i in range(M+1): #간격 k보다 크면 리턴 0
        if charge_stop[i+1] - charge_stop[i] > K:
            return 0


    cnt = 0
    lastStop = 0

    for i in range(M+2):
        curS = charge_stop[i]
        if curS - lastStop > K:
            cnt += 1
            lastStop = charge_stop[i-1]
    return cnt

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = [0] + list(map(int, input().split())) + [N] #충전기 있는 정류장

    print(f'#{tc} {check()}')

















