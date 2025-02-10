N = 5
numbers = [64, 25, 10, 22, 11]
#i = 0: 제일 작은 값을 찾아서 0에 위치
# i =1: 1에서 시작하여 제일 작은 값을 찾아서 1에 위치
# i = 2, 3
for i in range(N-1):
    # i에서 N 까지 중 제일 작은 값의 위치를 찾아서
    # i번째와 교환
    # i:0 [10, 25, 64, 22, 11]
    # i:1 [    11, 64, 22, 25]
    # i:2 [        22, 64, 25]
    # i:3 [            25, 64]
    min_pos = i
    for j in range(i + 1, N):
        if numbers[min_pos] > numbers[i]:
            min_pos = j
            numbers[i], numbers[min_pos] = numbers[min_pos], numbers[i]
print(numbers)
