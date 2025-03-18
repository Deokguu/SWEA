# def powerset(cnt, n, sum):
#     if cnt == 10:
#         return
#
#     sum += n
#     powerset(cnt+1, n+1, sum)
#
# powerset(1, 1, 0)
'''
부분집합: 현재 원소를 포함하냐 안하냐
level: N개의 원소를 모두 고려하면
branch: 집합에 해당 원소를 포함 시키는 경우 or 안 시키는 경우 두 가지
누적값
    부분집합의 총합
    부분집합에 포함된 원소들
1.완전탐색(재귀)
2.가지치기 코드
재귀, DFS, 백트래킹 모두 한 세트이다.
DFS(재귀 or 스택) 위주로 공부하고 재귀라면 가지치기를 고려해라
'''
def dfs(cnt, total, subset):
    if total == 10: #1. total이 10이면 출력해라
        print(subset)
        return

    if total > 10: # 2. total이 10을 넘겼으면 가지치기하자
        return

    if cnt == 10:
        print(subset)
        return

    dfs(cnt + 1, total+ arr[cnt], subset + [arr[cnt]] ) #포함하는 경우
    dfs(cnt + 1, total, subset) # 집합에 포함 안 하는 경우

arr = [i for i in range(1, 11)]
# visited = [] 순열조합에선 필요하지만 부분집합에선 필요없다.

dfs(0,0,[])