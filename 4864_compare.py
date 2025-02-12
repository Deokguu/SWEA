def search(t, p):
    N = len(p)
    M = len(t)

    for i in range(M-N+1): # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(N): # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break
        else: #break가 발생하지 않고 for문이 종료된 경우 else를 실행
            return 1 #패턴이 처음 나타난 인덱스 리턴
    return 0 #보통 존재하지 않는다는 의미로 -1 리턴



T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    print(f'#{tc} {search(str2, str1)}')