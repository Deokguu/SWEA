N = int(input())
arr = [input() for _ in range(8)]
# print(arr)

#문자열 s를 입력받아 회문이면 true, 아니면 false return
def isPali(s):
    # if s == s[::-1]:
    #     return True
    # return False

    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return False
    return True

cnt = 0
for row in range(8):
    #한 줄에 대해서
    for start in range(8-N+1): #예시 하나 잡고 해보기
        if isPali(arr[row][start : start +N]):
            cnt += 1
#세로로 갈 땐 슬라이싱을 못 씀.
for col in range(8):
    for start in range(8 - N + 1):
        s = ''
        for row in range(start, start + N): #슬라이싱 대신 씀
            s += arr[row][col]
        if isPali(s):
            cnt += 1

print(cnt)


# #편법: 세로를 가로배열로 만들어서 풀기
# arr2 = list(zip(*arr))
# cnt = 0
# for row in range(8):
#     #한 줄에 대해서
#     for start in range(8-N+1): #예시 하나 잡고 해보기
#         if isPali(arr[row][start : start +N]):
#             cnt += 1
#
#
#         if isPali(arr2[row][start: start + N]):
#             cnt += 1














N = int(input())
txt = [input() for _ in range(8)]

total = 0

for j in range(8-N+1): #회문을 확인하는 구간의 첫 글자 인덱스 / range문이니까 1더해줌
    for k in range(N//2): #회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:
            break #비교 글자가 다르면 현재구간 중지
    else:
        total += 1 #break에 걸리지 않고 for문 종료 시 or 회문이면

print(total)