def position(N):
    sum_pos = 0
    while N >= 1:
        sum_pos += N % 10
        N //= 10 
    return sum_pos
        


N = int(input())
print(position(N))