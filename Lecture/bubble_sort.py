N = 5
numbers = [55, 7, 78, 12, 42]

#1. 78을 N-1으로 보낸다
# 0, 1번째 비교해서 뒤로 보내기 7 55 78 12 42
# 1, 2 번째 비교해서 뒤로 보내기 7 55 78 12 42
# 2, 3 번째 비교해서 뒤로 보내기 7 55 12 78 42
# 3, 4 번째 비교해서 뒤로 보내기 7 55 12 42 [78]

#2. 55를 N-2로 보낸다
# 0, 1 비교 7 55 12 42 [78]
# 1, 2 비교 7 12  55 42 [78]
# 2, 3 비교 7 12 42 [55] [78]

for phase in range(N-1, 0, -1):
    for i in range(0, phase):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)

#손으로 풀며 아이디어 내고 그걸 코드로 가져온다