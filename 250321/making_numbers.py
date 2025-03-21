def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2
    elif oper_idx == 1:
        return num1 - num2
    elif oper_idx == 2:
        return num1 * num2
    elif oper_idx == 3: # 나눗셈에서 예외처리
        if num1 < 0:
            return -(abs(num1) // num2) # 음수 // 양수 연산이 불가능함
        return num1 // num2

def dfs(depth, total):
    global max_result
    global min_result

    if depth == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    for i in range(4):
        if operlands[i] == 0:
            continue
        operlands[i] -= 1
        dfs(depth+1, cal(total, numbers[depth], i))
        operlands[i] += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input()) #숫자의 개수
    operlands = list(map(int, input().split())) #   (+, -, *, /) 순서로 각각의 개수
    numbers = list(map(int, input().split()))   # 피연산자
    min_result = 10e9
    max_result = -10e9

    dfs(1, numbers[0]) # depth가 1일 때, 첫 번째 숫자에 연산을 한 번 하는 동작
    print(f'#{tc} {abs(max_result-min_result)}')