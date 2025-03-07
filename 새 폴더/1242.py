def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2     # 2로 나눈 나머지
        binary_number = str(remain) + binary_number     #나머지가 앞으로 들어옴
        target = target // 2    # 2로 나눈다.
    return binary_number
def test(s, K):
    if K >= N:
        for i in range(K-N, K):
            if bin_M[i] != '1':
                return 'OFF'
        else:
            return 'ON'
    return 'OFF'


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_M = dec_to_binary(M)
    K = len(bin_M)
    print(f'#{tc} {test(bin_M, K)}')



