'''
행과 열을 각각 순회하며 연속된 1을 수집한다.
while문으로 배열의 현재요소와 다음요소가 1이고 다음요소가 벗어나지 않을 때 cnt에 1을 추가하고
다음요소가 0일 때 다음요소로 넘어가고 cnt를 초기화
'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #행 순회하며 검사
    for i in range(N):
        for j in range(M):
            newC = j + 1
            while arr[i][j] == 1 and 0 <= newC < N and arr[i][newC] == 1:



