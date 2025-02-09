#Greedy
# data = [4, 4, 4, 3, 4, 5]
# data = list(map(int, input()))
# counts = [0] * 10
# #숫자 세기
# for x in data:
#     counts[x] += 1


# num = 456789

num = int(input())
c = [0] * 12 # c[10]과 c[11]은 항상 0, run 확인을 위한 여분

for _ in range(6): #단순 반복 6회
    c[num % 10] += 1 # 1의 자릿수를 알아내는 연산 / 많이 쓰는 연산
    num //= 10 #num의 1의 자리 제거

i = 0
tri = run = 0
while i < 10: #카드 번호 9까지...
    #tri 확인
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue #tri 남아있는지 확인하려고 한 번 더 올라감
    #run 확인
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run +tri == 2:
    print('win')
else:
    print('lose')
