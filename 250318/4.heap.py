import heapq

arr = [20, 15, 19, 4, 13, 11]
# 1. 기본 리스트를 heap으로 만들기
heap_arr = heapq.heapify(arr) #반환없는 함수 / 최소힙으로 바뀐다.
# 디버깅 시에 이진 트리로 그림을 그려야 한다!
# 딱 봤을 때는 정렬이 안된 것처럼 보인다.
print(arr)

#2. 하나씩 데이터를 추가
min_heap=[]
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

#3. 최대힙?
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end = ' ')

#전자사전 예제
'''
1. 길이 순서로 먼저 출력
2. 길이가 같다면, 사전 순으로 출력
'''