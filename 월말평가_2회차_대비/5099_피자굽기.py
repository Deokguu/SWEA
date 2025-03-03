T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = [i for i in range(1, M+1)]
    cheese = list(map(int, input().split()))

    num_ch = []
    for i in range(M):
        num_ch.append([pizza[i], cheese[i]])
    print(num_ch)