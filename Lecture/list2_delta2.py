# N = 2
# M = 3
#
# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni = i + di
#             nj = j +dj
#             if 0 <= ni < N and 0 <= nj < M:
#                 print(ni, nj)
#
# #상하좌우 k칸 합계 중 최댓값
# max_v = 0
# for i in range(N):
#     for j in range(N):
#         s = arr[i][j] #변수 초기화
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]: #상하좌우 방향 4개
#             for c in range(1, k+1): #몇칸까지 볼 건지
#                 ni, nj = i + di * c, j + dj * c
#                 if 0 <= ni < N and 0 <= nj < N:
#                     s += arr[ni][nj]
#         if max_v < s:
#             max_v = s
#
# #연습문제1
# s = 0
# for i in range(5):
#     s += A[i][i]
#     s += A[i][4-i] # [i][M-1-j]
# s -= A[5//2][5//2] #행과 열 크기가 홀수

#연습문제2 + 테스트케이스 번호 추가해야함!!!
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

for i in range(N):
    for j in range(M):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]: #주변 원소 인덱스 구함
            ni = i + di
            nj = j +dj
            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni][nj] - arr[i][j])
print(total)

