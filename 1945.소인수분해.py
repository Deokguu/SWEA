T =int(input())

for tc in range(1, T+1):
    N =int(input())
    arr = [2, 3, 5, 7, 11]
    answer = [0, 0, 0, 0, 0]
    
    for i in range(len(arr)):
            
        for _ in range(10):
            if N % arr[i] == 0:
                answer[i] += 1
                N = N // arr[i]
    result = ' '.join(map(str, answer))
    print(f'#{tc} {result}')
    