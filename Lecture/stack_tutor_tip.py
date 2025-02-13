'''
중간에 있는 거 볼 수 없다
다른 알고리즘에 이 자료구조(stack) 쓰면 유용한 것들이 있음
연산알고리즘, dfs 알고리즘의 기반이 되는 자료구조
top 속성 -> 마지막 데이터 가리킴
변수: 메모리를 잡아놓고 값을 바꿀 수 이쓴걱
상수: 메모리 잡아놓고 데이터 바꾸지 않는 것 - 주로 대문자로 씀
'''

# def push(value): #전역변수 읽어오는 건 괜찮은데 값을 바꾸려면 global 써줘야함
#     global top
#
#     if not is_full():
#         top += 1
#         STACK[top] = value
#
#     else:
#         print('가득 찼어')
#
# def pop():
#     global top
#
#     if not is_empty():
#         value = STACK[top]
#         top -= 1
#         return value # 빼서 그 데이터를 써야하기에 리턴함
#
# def is_full():
#     return top == SIZE-1
#
#
# def is_empty():
#     if top == -1:
#         return True
#     else:
#         return False
#
# def peek():
#     return STACK[top]
#
# SIZE = 10
# STACK = [-1] * SIZE
#
# top = -1
#
# push(3)
# print(top,STACK)
#
# push(4)
# print(top,STACK)
#
# push(10)
# print(top,STACK)
#
# print(pop())
# print(top,STACK)


#피보나치 수열
# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13
#n의 index의 fibo 값을 return한다
# def fibo(n):
#     return fibo(n-1) + fibo(n-2)

# def fun1(n):
#     fun2(n)
#
# def fun2(n):
#     print('func2')
#
# fun1(2)
# fun2(3)

def fibo(n):
    if n < 2:
        return n

    f1 = fibo(n-1)
    f2 = fibo(n-2)
    return f1+f2
fibo(3)

'''
memorization
dp
'''