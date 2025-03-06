#이진트리탐색 삽입 연산
def insert(value):
    idx = 1
    while Tree[idx]: #데이터가 없을 때까지
        if Tree[idx] < value:
            idx = idx*2+1
        else:
            idx = idx*2
    Tree[idx] = value
def find(key):
    idx = 1
    while idx < SIZE and Tree[idx]: #데이터가 없을 때까지
        if Tree[idx] == key:
            return idx
        if Tree[idx] < key:
            idx = idx*2+1
        else:
            idx = idx*2
    return -1

N = 8
lst = [9, 4, 12 ,3, 6, 15, 13, 17]
Tree = [0] * 100 # 이진트리탐색 생성 / 완전이진트리가 아니기 때문에 [0] * (N+1)이 아닌 [0] * 충분히 큰 수 100을 곱해줌
for data in lst:
    insert(data)
    print(Tree)

print(find(8))