T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    max_num = 0

    #행부터 순회하며 탐색
    for i in range(N): # 행
        cnt = 0
        for j in range(M): # 열
            if arr[i][j] == '1': # 현재 위치가 1이면
                cnt += 1 # 카운트 증가
            else: # 아니면
                if max_num < cnt:
                    max_num = cnt
                cnt = 0
        if max_num < cnt:
            max_num = cnt


    for j in range(M): # 열
        cnt = 0
        for i in range(N):# 행 0 1 2
            if arr[i][j] == '1':
                cnt += 1
            else:
                if max_num < cnt:
                    max_num = cnt
                cnt = 0
        if max_num < cnt:
            max_num = cnt
    print(f'#{tc} {max_num}')







