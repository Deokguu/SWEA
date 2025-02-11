#인덱스 연산으로 문자열 뒤집기
txt = list(input())
N = len(txt)

for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
print(txt)

s1 = 'string'
s = s1[::-1]
print(s)

s_lst = list(s)
s_lst.reverse()
print(s_lst)
print(''.join(s_lst))

#문자열 메모리 주소
s1 = 'abc'
s2 = 'ab'
s3 = 'def'
s4 = s2 + 'c' # 'abc'를 다른 메모리 위치에 저장한다.
print(s1 == s4) #같은 모양
print(s1 is s4) # 같은 메모리 위치인가?
print(s1 is 'abc')

print(ord('a'), ord('A'))

a = 'A'
b = int(a, 16) #a는 16진수이고 정수로 바꿔줘
c = '1001'
d = int(c, 2) #c는 2진수이고 정수로 바꿔줘

print(b)
print(d)

