t = 'TTTTTATTAATA'
p = 'TTA'

N = len(t)
M = len(p)
def search(p, t):
    N = len(t)
    M = len(p)

    for i in range(N-M+1): # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M): # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break
        else: #break가 발생하지 않고 for문이 종료된 경우 else를 실행
            return i #패턴이 처음 나타난 인덱스 리턴
    return -1 #보통 존재하지 않는다는 의미로 -1 리턴

print(search(p, t))
#

aws = ''
i = 0
j = 0
while i + j < N + M:
    if i < N:
        aws += A[i]