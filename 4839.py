def bin(a, N, key):
    s = 0
    e = N-1
    cnt = 0
    while s <= e:
        middle = (s+e) // 2
        if a[middle] == key:
            break
        elif a[middle] > key:
            e = middle
        elif a[middle] < key:
            s = middle
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr_book = []
    for i in range(1, P+1):
        arr_book.append(i)


    cnt_a = bin(arr_book, P, A)
    cnt_b = bin(arr_book, P, B)
    # print(cnt_b, cnt_a)
    if cnt_a > cnt_b:
        print(f'#{tc} B')
    elif cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a == cnt_b:
        print(f'#{tc} 0')


