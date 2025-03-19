'''
6개의 원소 (1~6)이 존재하는 경우
'''

def make_set(x):
    '''
    1. 집합을 만들어 주는 함수
    1~n까지의 원소가 있다고 가정 -> 총 n 개의 집합을 생성
    -> 각 원소의 부모(!= 대표자)를 자신으로 초기화. 부모가 항상 대표자는 아니지만 대표자일 수 있다.
    '''
    parents = [i for i in range(N + 1)] # 0인덱스는 버린다
    return parents

def find_set(x): #경로압축  추가
    if parents[x] == x:
        return x

    #경로압축 (path compression)을 통해 x의 부모를 대표자로 변경
    parents[x] = find_set(parents[x]) #대표자를 찾아오는 재귀 호출, 리턴받아서 부모를 대표자로 업데이트

    return parents[x]


def union(x, y):
    # 1. x, y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면? return
    if ref_x == ref_y:
        return

    #만약 다른 집합이라면 합친다.
    #문제에 따라 우선되는 집합으로 합쳐주면 된다.
    #-> 이번 예시에서는 더 작은 노드로 합친다.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


    pass

N = 6
parents = make_set(N)   # 해당 노드의 부모 정보를 가지고 있음
union(1, 3)
union(2, 3)
union(5,6)
# 3과 5는 같은 집합?
#if parents[3] == parents[5] => 대표자가 아니라 부모 노드를 기준으로 비교하는 것임
if find_set(3) == find_set(5):
    print("응")
else:
    print("아니")
print(parents)