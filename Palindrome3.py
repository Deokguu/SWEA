def isPali(s):
    if s != s[::-1]:
            return False
    return True

T = 10

for _ in range(T):
    test_case = int(input())
    arr = [list(input()) for _ in range(100)]
    max_length = 1

    for i in range(100, 0, -1):
        for row in range(100):
            for start in range(100 - i + 1):  
                if isPali(arr[row][start: start + i]):
                    max_length = max(max_length, i)


    for i in range(100, 0, -1):    
        for col in range(100):
            for start in range(100 - i + 1):
                s = ''
                for row in range(start, start + i): 
                    s += arr[row][col]
                if isPali(s):
                    max_length = max(max_length, i)

    print(f'#{test_case} {max_length}')
