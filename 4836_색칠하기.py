T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []

    for _ in range(10): #10 x 10 배열 만들기
        arr.append([0] * 10)
    # print(arr)
    total = 0
    for _ in range(N):
        r1, c1, r2, c2, color = (list(map(int, input().split())))

        for i in range(r1, r2+1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

                if arr[i][j] == 3:
                    total += 1
    print(f'#{tc} {total}')




