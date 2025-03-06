N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
print(left)
print(right)