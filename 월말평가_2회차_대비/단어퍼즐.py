# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr_puzzle = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
    
#     for row in range(N):
#         for col in range(N):
#             if arr_puzzle[row][col] == 0:
#                 newR, newC = row, col + 1
#                 letter_cnt = 0
#                 while 0<=newR<N and 0<=newC<N:
#                     if arr_puzzle[newR][newC] == 0:
#                         break
#                     else:
#                         letter_cnt += 1
#                         newC += 1
#             elif arr_puzzle[row][0] == 1:
#                 letter_cnt = 1
#                 newR, newC = row, col + 1
#                 while 0<=newR<N and 0<=newC<N:
#                     if arr_puzzle[newR][newC] == 0:
#                         break
#                     else:
#                         letter_cnt += 1
#                         newC += 1
#                 if letter_cnt == K:
#                     cnt += 1
    
#     for col in range(N):
#         for row in range(N):
#             if arr_puzzle[row][col] == 0:
#                 newR, newC = row + 1, col
#                 letter_cnt = 0
#                 while 0<=newR<N and 0<=newC<N:
#                     if arr_puzzle[newR][newC] == 0:
#                         break
#                     else:
#                         letter_cnt += 1
#                         newR += 1
#                 if letter_cnt == K:
#                     cnt += 1
#             elif arr_puzzle[0][col] == 1:
#                 newR, newC = row + 1, col
#                 letter_cnt = 1
#                 while 0<=newR<N and 0<=newC<N:
#                     if arr_puzzle[newR][newC] == 0:
#                         break
#                     else:
#                         letter_cnt += 1
#                         newR += 1
#                 if letter_cnt == K:
#                     cnt += 1
#     print(f'#{tc} {cnt}')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr_puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 가로 방향 검사
    for row in range(N):
        length = 0  # 연속된 1의 개수
        for col in range(N):
            if arr_puzzle[row][col] == 1:
                length += 1
            if arr_puzzle[row][col] == 0 or col == N - 1:  # 벽이나 끝을 만나면 길이 체크
                if length == K:
                    cnt += 1
                length = 0  # 길이 초기화

    # 세로 방향 검사
    for col in range(N):
        length = 0
        for row in range(N):
            if arr_puzzle[row][col] == 1:
                length += 1
            if arr_puzzle[row][col] == 0 or row == N - 1:
                if length == K:
                    cnt += 1
                length = 0  # 길이 초기화

    print(f'#{tc} {cnt}')
