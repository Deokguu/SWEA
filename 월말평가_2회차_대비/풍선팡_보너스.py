def balloon(arr, N):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_total = 0
    min_total = 10e10
    for row in range(N):
        for col in range(N):
            total = arr[row][col]
            
            for d in range(4):
                newR, newC = row+dr[d], col+dc[d]

                while 0<=newR<N  and 0<=newC<N:
                    total += arr[newR][newC]
                    newR, newC = newR+dr[d], newC+dc[d]   
            if max_total < total:
                max_total = total
            if min_total > total:
                min_total = total

    return max_total - min_total     
            # for d in range(4):
            #     for far in range(1, N):
            #         newR = row + dr[d] * far
            #         newC = col + dc[d] * far
                    
    #                 if 0<=newR<N and 0<=newC<N:
    #                     total += arr[newR][newC]

    #         if max_total < total:
    #             max_total = total
    #         if min_total > total:
    #             min_total = total
    # return max_total - min_total


T = int(input())

for tc in range(1, T+1):
    N = int(input()) #격자의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {balloon(arr, N)}')
