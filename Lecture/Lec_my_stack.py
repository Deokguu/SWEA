# top 은 마지막 저장위치
# # 간단한 스택
# top = -1
# stack = [0] * 10
#
# #push(1) 동작 만들기
# top += 1
# stack[top] = 1
#
#
# top += 1
# stack[top] = 2
#
#
# top += 1 #push(3)
# stack[top] = 3
#
#
# top -= 1 #pop
# print(stack[top+1])
#
# top -= 1
# print(stack[top+1])
#
# top -= 1
# print(stack[top+1])

'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''

#여는괄호 만나면 push, 닫는괄호는 pop
#비어있거나 남아있으면 오류

# 1218 괄호 짝짓기 참고...
txt = input()

top = -1
stack = [0] * 100

ans = 1  # 짝이 맞다고 가정
for x in txt:
    if x == '(': # 여는 괄호 push, if x in '({[<':
        top += 1
        stack[top] = x
    elif x == ')': # 공백 제거할 겸 elif 씀
        if top == -1: # 스택이 비어있으면
            ans = 0
            break # for x
        else:
            top -= 1
                #소괄호만 있으므로 비교 작업 생략
if top > -1: # 여는괄호가 남아있으면
    ans = 0

print(ans)

def is_pair(s):
    STACK = []
    for c in s:
        if c == '(':
            STACK.append(c)
        elif c == ')':
            if not STACK:
                return False

            temp = STACK.pop(-1)
            if temp != '(':
                return False
    if STACK:
        return False

    return True

s = '()()'
print(is_pair(s))






















