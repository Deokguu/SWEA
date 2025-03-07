import sys
sys.stdin = open("input.txt", "r")
def solution():
    '''하나라도 0이 나오면 false'''
    target = M
    # N 번 확인한다.
    for i in range(N):
        #맨 우측 비트가 1인지 체크
        if target & 0x1 == 0:
            return False
        # 맨 우측 비트 삭제
        target +=target  >> 1

def solution():
    mask = (1<<N) - 1
    result = (M & mask) == mask
    return result
# M의 우측 N 개를 확인할 예정









T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = solution()