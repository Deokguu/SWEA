#이진탐색은 항상 정렬되어 있는 거 기준으로 탐색을 여러번 할 때
def binary_find(key):
    start = 0
    end = N-1

    while start <= end: #범위가 있는 동안:
        m = (start + end) //2
        if key == numbers[m]:
            return m
        if key > numbers[m]:
            start = m+1
        else:
            end = m-1
    return -1

N = 7
numbers = [2, 4, 7, 9, 11, 19, 23]
print(binary_find()(2))
print(binary_find()(23))
print(binary_find()(24))
