T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    max_numbers = 0

    for letter in str1:
        cnt = 0
        for letter2 in str2:
            if letter == letter2:
                cnt += 1
        if max_numbers < cnt:
            max_numbers = cnt

    print(f'#{tc} {max_numbers}')