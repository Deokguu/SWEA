def search(a, key):
    for i in range(100):
        if a[99][i] == key:
            return i



T = 10

for _ in range(1, 1+T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col = search(arr, 2)

    dx = [-1, 1, 0]
    dy = [0, 0, -1]




    while row > 0:
        for i in range(3):
            newC = col + dx[i]
            newR = row + dy[i] #1번방향: 왼쪽 2번방향: 오른쪽 3번방향: 위로
            if 0 <= newC <= 99 and 0 <= newR and arr[newR][newC] == 1:
                row = newR
                col = newC
                arr[row][col] = -1
                break

    print(f'#{tc} {col}')