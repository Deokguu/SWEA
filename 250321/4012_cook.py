def cal_synergy(lst):
    total = 0

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
    return total

def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

    return cal_synergy(A_list), cal_synergy(B_list)

def dfs(depth, start):
    global result

    if depth == N // 2:
        a_total, b_total = get_synergy()
        result = min(result, abs(a_total - b_total))
        return
    for food_num in range(start, N):
        if visited[food_num]:
            continue
        visited[food_num] = 1
        dfs(depth + 1, food_num + 1)
        visited[food_num] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 21e8
    dfs(0, 0)
    print(f'#{tc} {result}')
