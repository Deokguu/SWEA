T = 10

for _ in range(1, T+1):
    tc = int(input())
    pattern = input()
    txt = input()

    N = len(txt)
    M = len(pattern)
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if txt[i+j] != pattern[j]:
                break
        else:
            cnt += 1

    print(f'#{tc} {cnt}')