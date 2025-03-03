def same_extract(words):
    stack = []

    for letter in words:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        elif stack and stack[-1] == letter:
            stack.pop()
    answer = ''.join(stack)
    return answer

T = 10

for tc in range(1, T+1):
    n, arr= input().split() # 문자의 총 개수, 문자열
    print(f'{tc} {same_extract(arr)}')
    
