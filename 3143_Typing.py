T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)

    #전체 length에서 겹치는 횟수 빼자

    cnt = 0
    i = 0
    while i < N-M+1:
        for j in range(M):
            if A[i+j] != B[j]:
               break
        else:
            cnt += 1
            i += M - 1
        i += 1
    answer = N - (cnt * M) + cnt
    print(f'#{tc} {answer}')