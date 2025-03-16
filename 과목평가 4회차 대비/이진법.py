def to_bin(s):
    binN = ''
    for c in s:
        if c.isdigit():
            c = int(c)
            temp = ''
            while c > 0:
                remain = c % 2
                temp = str(remain) + temp
                c = c // 2
            if len(temp) < 4:
                zero = 4-len(temp)
                binN = binN + '0'*zero
            binN = binN + temp
        else:
            mapp = {'A':1010, 'B':1011, 'C':1100, 'D':1101, 'E':1110, 'F':1111}
            binN += str(mapp[c])
    return binN
 
T = int(input())
for tc in range(1, T+1):
    N, s = input().split() 
    print(f'#{tc} {to_bin(s)}')