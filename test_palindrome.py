def test_pal(s):
    N = len(s)

    for i in range(N // 2):
        if s[i] != s[N - i - 1]:
            return 0
    return 1

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    answer = test_pal(word)

    print(f'#{tc} {answer}')

