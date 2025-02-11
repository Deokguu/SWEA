T = int(input())

for tc in range(1, T+1):
    txt = list(input())

    N = len(txt)

    for i in range(N//2):
        txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
    # # print(txt)
    for i in range(len(txt)):
        if txt[i] == 'q':
            txt[i] = 'p'
        elif txt[i] == 'p':
            txt[i] = 'q'
        elif txt[i] == 'b':
            txt[i] = 'd'
        elif txt[i] == 'd':
            txt[i] = 'b'
    txt = ''.join(txt)
    print(f'#{tc} {txt}')