def BF(t, p):
    N = len(t)
    M = len(p)

    tp = pp = 0
    while tp < N and pp < M:
        if t[tp] == p[pp]:
            tp += 1
            pp += 1
        else:
            tp = tp - pp + 1
            pp = 0
    if pp == M:
        return tp - M

t = 'TTTTAACCA'
p = 'TTA'
print(BF(t, p))
# 첫번째, 마지막꺼, 못찾는 것도

#KMP알고리즘

def KMP(t, p):
    N = len(t)
    M = len(p)

    lps = [0] * (M+1)
    lps[0] = -1
    j =0
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print('=>', lps)

    tp = pp = 0
    while tp<N and pp<N:
        if lps[pp] == -1 or t[tp] == p[pp]:
            tp += 1
            pp += 1
        else:
            pp = lps[pp]
    if pp == M:
        return tp-M
    return -1


t = 'abcabcdabcefsss'
p = 'abcdabcef'

print(KMP(t, p))