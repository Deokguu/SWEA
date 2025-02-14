def fibo(n) :
    global cnt
    cnt += 1
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

cnt = 0             # 호출 횟수 기록
print(fibo(10), cnt)

def fibo1(n) :
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n), cnt)