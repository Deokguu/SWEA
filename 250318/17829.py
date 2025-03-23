def solve(arr, N):
    new_arr = []
    for row in range(0, N, 2):
        new_row = [] #열 돌 때마다 새로운 행 만들어서 저장장
        for col in range(0, N, 2):
            #2x2 배열에서 두 번째 큰 값
            second = [arr[row][col], arr[row][col+1], arr[row+1][col], arr[row+1][col+1]]
            second.sort()
            new_row.append(second[2])
        new_arr.append(new_row)
    return new_arr
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

while N > 1:
    arr = solve(arr, N)
    N = N // 2

print(arr[0][0])
        

