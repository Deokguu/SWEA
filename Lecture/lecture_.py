#key를 입력 받아서 key의 index를 return
#없으면 -1 return

def for_find(key):
    for i in range(N):
        if key == numbers[i]:
            return i
    return -1

def while_find(key):
    i = 0
    while i < N:
        if key == numbers[i]:
            return i
        i += 1
    return -1

def find(key):
    i = 0
    while i < N and key != numbers[i]: #주의할 점: i < N 조건이 먼저 와야함 / 범위 비교는 앞에, 값이나 데이터 비교는 뒤에 쓰자
        i += 1
        if i== N:
            return -1

    return i

N = 7
numbers = [ 4, 9, 11, 23, 2, 19, 7]

print(find(4))
print(find(7))
print(find(11))
print(find(1))
print(find(25))