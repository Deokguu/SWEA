T = int(input())

for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    answer = 1

    #행 검사
    for i in range(9):
        if len(set(arr[i])) != 9:
            answer = 0
    
    #열 검사
    
    for i in range(9):
        col = []
        for j in range(9):
            col.append(arr[j][i])
        if len(set(col)) != 9:
            answer = 0

    # 3x3 격자
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            #행 우선 순회하면서 빈 리스트에 넣기
            grid = []
            for p in range(3):
                for q in range(3):
                    grid.append(arr[p][q])
            if len(set(grid)) != 9:
                answer = 0

    print(f'#{tc} {answer}')
            # arr[i][j]





