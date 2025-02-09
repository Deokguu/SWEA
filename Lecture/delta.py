di = [0, 1, 0, -1] #오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]
N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < M: #없는 인덱스 제거
                print(ni, nj)
# i = 2
# j = 3
# for dir in range(4): #4개의 방향이 기준일 때
#     ni = i + di[dir]
#     nj = j + dj[dir]
#     print(ni, nj)
