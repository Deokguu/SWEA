def compare(a, b):
    if a > b:
        return '>'
    elif a == b :
        return '='
    elif a < b :
        return '<'
    
T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    print(f'#{tc} {compare(a, b)}')
