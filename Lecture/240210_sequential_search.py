#정렬되어 있지 않은 경우
def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1


def seq(arr, n, key):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == key:
                return 1
    return 0
#함수 만들어서 쓰기

arr = [4, 9, 11, 23, 2, 19, 7]
# print(seq_search(arr, len(arr), 23))

#정렬되어 있는 경우
arr.sort()
# print(arr)

def seq_search_sorted(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:
            return -1
    return -1 #모든 원소가 key보다 작은 경우
print(arr)
print(seq_search_sorted(arr, len(arr), 11))
print(seq_search_sorted(arr, len(arr), 100))