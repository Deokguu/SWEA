# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# N = int(input()) # 배열 행과 열의 크기
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# '''
# 3
# 123
# 456
# 789
# '''
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
#
#0으로 채워진 3x4 배열 만들기 N X M
N = int(input())
M = int(input())
arr = [[0] *4] *3 #[[0] * 4]의 참조를 세 번 반복하라는 의미, 즉, 복사가 제대로 이루어지지 않음

arr2 = [[0] * N for _ in range(N)] #정사각형 배열


# i 행, j 열 배열 만들기 i, j 범위가 같은 경우
for i in range(N):
    for j in range(N):
        print(arr[i][j])











