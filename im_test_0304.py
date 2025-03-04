'''
N명의 야구선수 중에서 실력 차이가 K 이하인 최대 팀원을 찾는 문제
주어진 N명의 야구선수들 중 실력 차이가 K 이하인 선수를 선택하여 만들 수 있는 가장 큰 팀의 크기를 구해야함.
N: 야구선수의 수 / K: 실력 차이의 최대값 / 야구선수들의 실력 값을 나타내는 배열
'''
def baseball(arr, N, K): 
    for k in range(N, 0, -1): #팀 크기를 N부터 1까지 감소하며 확인
        for i in range(N-k+1): #가능한 모든 부분 배열 확인인
            team = arr[i:i+k] # 연속된 k명의 수
            if max(team) - min(team) <= K:
                return k

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    baseball_team = list(map(int, input().split()))
    baseball_team.sort() # 정렬하여 탐색 최적화
    print(f'#{tc} {baseball(baseball_team, N, K)}')

'''
1
4 2
6 4 2 3
'''
'''
def baseball(arr, N, K):
    max_size = 1  # 최소 한 명은 선택 가능
    start = 0

    for end in range(N):  # 끝 인덱스를 이동하면서 윈도우 확장
        while arr[end] - arr[start] > K:
            start += 1  # 차이가 K보다 크면 시작점 이동
        
        # 현재 윈도우 크기 갱신
        max_size = max(max_size, end - start + 1)

    return max_size

# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    baseball_team = list(map(int, input().split()))
    baseball_team.sort()  # 정렬하여 탐색 최적화
    print(f'#{tc} {baseball(baseball_team, N, K)}')
'''