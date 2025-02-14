def solve(n):
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 3
    for i in range(3, n+1):
        f[i] = f[i-1] + 2 * f[i-2]

    return f[n]

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10

    print(f'#{tc} {solve(N)}')

