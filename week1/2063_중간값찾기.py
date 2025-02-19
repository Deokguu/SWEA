def middle(arr):
    #중간값 찾는 함수
    N = len(arr)
    return arr[N//2]

N = int(input())
arr = sorted(list(map(int, input().split())))
print(middle(arr))