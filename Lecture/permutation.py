#순열 / 효율이 좋진 않음 / 완전탐색 알고리즘 / IM 문제는 되도록 완전탐색 알고리즘으로 시작하기
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i1 != i3 and i2 != i3:
                    print(i1, i2, i3)


arr = [2, 3, 7]

for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])


