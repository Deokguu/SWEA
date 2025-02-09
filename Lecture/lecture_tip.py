N = 4 #row
M = 3 #column
arr = [[1, 2, 3]
      [11, 12, 13]
      [21, 22, 23]
      [31, 32, 33]
      ]
#
# for row in range(N):
#     # print(arr[row])
#     for col in range(M):
#         print(arr[row][col])
#
# #0번째 컬럼에 대해 차례대로 출력
# for col in range(M):
#     for row in range(N):
#         # print(arr[row][col]) #누가 먼저 출력되느냐가 관건

# 행 별 합계의 최대최소값 구하기
max_v = -100 * M
min_v = 100 * M
for row in range(N):
    sum_v = 0
    for col in range(M):
        sum_v += arr[row][col]
        print(sum_v)
        if max_v < sum_v:
            max_v = sum_v
        if min_v < sum_v: #elif가 들어오면 안됨. max값과 min값 구하는 게 서로 영향을 주면 안되기 때문
            min_v = sum_v

# 열 별 합계의 최대최소값 구하기
max_v = -100 * N
min_v = 100 * N
for row in range(N): #COL for문 먼저 나오게!!!
    sum_v = 0
    for col in range(M):
        sum_v += arr[row][col]
        print(sum_v)
        if max_v < sum_v:
            max_v = sum_v
        if min_v < sum_v: #elif가 들어오면 안됨. max값과 min값 구하는 게 서로 영향을 주면 안되기 때문
            min_v = sum_v





for col in range(M):
    sum_v = 0 #초기화를 어디에 해야하는지 중요
    for row in range(N):
        sum_v += arr[row][col]
    print(sum_v)

#전체 합 낼 때는 전체 반복문의 바깥쪽
#각 row별로 할 땐 row 순회 도는 for문 밖에 나와있어야함

# print(arr[row][col]) #누가 먼저 출력되느냐가 관건

#좌표 그려놓고 특징찾아서 전개해나가자
#위쪽영역 합 구하기
sum_v = 0

for row in range(N):
    for col in range(M):
        if row < col:
            sum_v += arr[row][col]

#대각선 합 구하기
sum_v = 0
for row in range(N):
    sum_v += arr[row][col]

#2차원배열 문제 많이 풀어보는 게 굉장히 중요. 많이 돌려보기


#delta 2차원 배열 연습문제2
N = 5 #row
M = 5 #column
arr = [[1, 2, 3, 4, 5]
      [0, 0, 0, 0, 0]
      [0, 0, 0, 0, 0]
      [0, 0, 0, 0, 0]
      [0, 0, 0, 0, 0]
      ]
max_v = 0

for row in range(N):
    for col in range(M):
        sum_v = 0
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            #상단의 좌표 구해오기
            newR = row + dr
            newC = col + dc
            if 0 <= newR and 0 <= newC:
                sum_v += abs(arr[newR][newC] - arr[row][col])
        print(sum_v)
        if max_v > sum_v:
            max_v = sum_v


#부분집합 관련 이야기
a = 10
b = 0b10
c = 0o10
d = 0x10
print(a, b, c, d)
for i in range(2**6):
    print(i)

N = 6
arr = [3, 6, 7, 1, 5, 4]
#000000: {}, 000001: {3}, 000011: {3, 6}, 111111: {3, 6, 7, 1, 5, 4}
for i in range(64): # 2**6, 1 << 6
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end = ',')
    print()
print()
    # print(i,bin(i))

# & 앤드연산자는 가장 끝쪽의 값만 취한다

matrix = [list(map(int, input().split())) for _ in range(100)]