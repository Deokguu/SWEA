T = int(input())

for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    sum_arr = 0
    cnt = 0

    for i in arr:
        sum_arr += i
        cnt += 1

    avg = round(sum_arr / cnt)
    print(f'#{tc} {avg}')