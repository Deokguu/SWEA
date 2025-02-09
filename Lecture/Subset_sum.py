a = [2, 7, 3]
bit = [0] * 3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            # print(bit)
            s = 0 #부분집합의 합
            for b in range(3):
                if bit[b]:
                    print(a[b], end = ' ') #부분집합에 포합된 원소
                    s += a[b]
            print(bit, s)

arr = [1, 2, 3]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = ",")
    print()
print()