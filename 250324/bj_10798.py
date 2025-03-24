arr = [list(input()) for _ in range(5)]
# print(arr)
max_v = 0
for i in range(5):
    if max_v < len(arr[i]):
        max_v = len(arr[i])
for row in range(5):
    if len(arr[row]) < max_v:
        arr[row] = arr[row] + [''] * (max_v-len(arr[row]))
# print(arr)
words = ''
for col in range(max_v):
    for row in range(5):
        words += arr[row][col]
print(words)