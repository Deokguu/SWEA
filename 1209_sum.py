T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr_list = []
    N = 100

    for i in range(N):
        arr_list.append(list(map(int, input().split())))



    max_total = []
    # 행 별 합계의 최대값 구하기
    max_r = 0

    for row in range(100):
        sum_r = 0
        for col in range(100):
            sum_r += arr_list[row][col]
            # print(sum_r)
        if max_r < sum_r:
            max_r = sum_r
    max_total.append(max_r)


    # print(max_r, min_r)

    # 열 별 합계의 최대값 구하기
    max_c = 0

    for col in range(100): #COL for문 먼저 나오게!!!
        sum_c = 0
        for row in range(100):
            sum_c += arr_list[row][col]
            # print(sum_c)
        if max_c < sum_c:
            max_c = sum_c

    max_total.append(max_c)

    # print(max_c, min_c)

    #대각선 합계의 최대 구하기기
    sum_t = 0
    for row in range(100):
        sum_t += arr_list[row][row]
    max_total.append(sum_t)

    sum_t2 = 0
    for row in range(100):
        for col in range(100):
            if row + col == 99:
                sum_t2 += arr_list[row][col]
    max_total.append(sum_t2)

    answer = max(max_total)

    print(f'#{tc} {answer}')
    # print(sum_t)