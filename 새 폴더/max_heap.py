#최대힙 (99개의 값 저장가능한)
#우선순위 큐 구현하는 자료구조

def enque(n):
    global last # 마지막 정점
    last += 1
    heap[last] = n # 마지막 정점에 n 저장

    child = last #부모의 키값과 비교하기 위해
    parent = child // 2 #부모 정점 번호 계산
    # 부모가 있고, 부모 < 자식 (최대힙 조건에 위반)
    while parent != 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent #현재 부모를 자식으로
        parent = child // 2
def deq():
    global last
    tmp = heap[1] #루트 백업
    heap[1] = heap[last] #삭제할 노드의 키를 루트에 복사
    last -= 1 # 마지막 노드 삭제
    parent = 1
    child = parent * 2

    while child <= last: # 자식이 하나라도 있으면
        if child + 1 <= last and heap[child] < heap[child + 1]: #오른족 자식도 있고, 오른쪽 자식이 더 크면
            child += 1 # 비교 대상을 오른쪽 자식으로 정함
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        else:
            break
    return tmp


heap = [0] * 100
last = 0

enque(2)
enque(5)
enque(7)
enque(3)
enque(4)
enque(6)

print(heap)
while last:
    print(deq())