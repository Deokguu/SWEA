T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    arr_answer = []
    for col in range(15):
        for row in range(5):
            if len(arr[row]) > col:
                arr_answer.append(arr[row][col])

    answer = ''.join(arr_answer)
    print(f'#{tc} {answer}')




