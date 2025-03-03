T = 10

for tc in range(1, T+1):
    tc_number = int(input())
    queue = list(map(int, input().split()))
    k = 1
    while True:
        if k == 6:
            k = 1
        t = queue.pop(0)
        if t-k<=0:
            queue.append(0)
            break
        else:
            queue.append(t-k)
        k += 1
    print(f'#{tc}', *queue)

