def todec(s, bit): # 10진수로 바꾸기
    value = 0
    for c in s:
        if c.isdigit():
            value = (value * bit) + int(c)
        else:
            mapp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
            value = (value * bit) + mapp[c]
    return value

T = int(input())

for tc in range(1,T+1):
    bin_num = list(input())
    tri_num = list(input())
    N = len(bin_num)
    M = len(tri_num)
    # print(bin_num)
    # print(tri_num)
    bin_lst = []
    tri_lst = []

    for i in range(N):
        arr = bin_num[:]
        if arr[i] == '0':
            arr[i] = '1'
        elif arr[i] == '1':
            arr[i] = '0'
        bin_lst.append(''.join(arr))
    # bin_lst = list(map(int, bin_lst))



    for i in range(M):
        arr = tri_num[:]
        for j in range(3):
            arr[i] = str(j)
            tri_lst.append(''.join(arr))

    # print(bin_lst)
    dec_bin = []
    dec_tri = []
    for i in bin_lst:
        dec_bin.append(todec(i, 2))
    for i in tri_lst:
        dec_tri.append(todec(i, 3))


    for i in dec_bin:
        if i in dec_tri:
            print(f'#{tc} {i}')
            break








    # arr = []
    # print(f'부분집합의 수 : {1 << len(arr)}')
    #
    # for i in range(1 << len(arr)):
    #     for idx in range(len(arr)):
    #         # (1<<idx) : ob1, 0b10, 0b100, 0b1000
    #         # i의 idx 번째 bit가 1인지 확인(부분 집합에 포함되어 있는지 확인)
    #         if i & (1 << idx):
    #             print(arr[idx], end=" ")
    #     print()