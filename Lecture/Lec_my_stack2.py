'''
function call

재귀호출
필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조

'''
# def fibo(n) :
#     global cnt
#     cnt += 1
#     if n < 2 :
#         return n
#     else :
#         return fibo(n-1) + fibo(n-2)
#
# cnt = 0             # 호출 횟수 기록
# print(fibo(10), cnt)

# 모든 배열 원소에 접근하기!!
def f(i,N): # (현재상태와 목표치로 설정)
    if i == N: #배열 크기에 해당되면 그만해
        return
    else:
        print(A[i])
        f(i+1, N)

A= [1, 2, 3]
f(0, 3)

#배열에 V가 있으면1, 없으면 0 리턴

def f(i, N, v):
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else: # 리턴 값 있는 경우
        return f(i+1, N, v ) # 리턴 값 그대로 올리기