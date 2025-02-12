#인덱스연산 이용하는 방법 중 한 가지
#A와 B의 글자를 차례로 늘어놓기
A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0 # A[i], B[j]
ans = ''
while i+j < N + M: #복사할 문자가 남아있으면
    if i < N: #A에 남은 문자가 있으면
        ans += A[i]
        i += 1
    if j < M:
        ans += B[j]
        j += 1

print(ans)

# A,B가 숫자로 이루어진 배열이라면?
A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0 # A[i], B[j]

ans = [0] * (N+M)
while i+j < N+M:
    if i < N:
        ans[i+j] = A[i]
        i += 1
    if j < M:
        ans[i+j] = B[j]
        j+=1
print(ans)
