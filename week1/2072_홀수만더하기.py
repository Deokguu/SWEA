T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            sum_odd += arr[i]
    print(f'#{tc} {sum_odd}') 

    '''
    인덱스랑 값(value) 잘 구분해서 쓰기
    헷갈리지 말고...
    ex) arr[i] % 2 인지 i % 2인지 잘 구분
    '''