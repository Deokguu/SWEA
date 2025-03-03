T = int(input())

for tc in range(1, T+1):
    N = int(input()) 
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_cnt = 0
    
    for row in range(N):
        for col in range(N):     
            cur_r, cur_c = row, col #초기화 작업
            min_r, min_c = row, col
            cnt = 1
            while True:    
                min_v = 10e10
                
                for d in range(4):
                    newR, newC = cur_r + dr[d], cur_c + dc[d]

                    if 0<=newR<N and 0<=newC<N and arr[cur_r][cur_c] > arr[newR][newC]:
                        if min_v > arr[newR][newC]:
                            min_v = arr[newR][newC]
                            min_r, min_c = newR, newC
                if min_v < arr[cur_r][cur_c]:
                    cur_r, cur_c = min_r, min_c
                    cnt += 1
                else:
                    break
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')
            
    
            