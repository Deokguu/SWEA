def in_order(T): #전위순회, 방문한 정점(부모) 먼저 처리
    global words
    if T: # 0이 아니면 (존재하는 정점이면)
        # visit(T) T에서 할 일 처리
        in_order(left[T]) #왼쪽자식(서브트리)로 이동
        words += tree[T]
        in_order(right[T]) #오른쪽자식(서브트리)로 이동
    return words
# 정점 번호를 인덱스로 하는 배열에 key문자 삽입
T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = []
    left = [0] * (N+1)
    right = [0] * (N+1)
    tree = [0]


    for _ in range(N):
        lst.append(input().split())

    # print(lst)
    for i in lst:
        if len(i) == 4:
            tree.append(i[1])
            left[int(i[0])] = int(i[2])
            right[int(i[0])] = int(i[3])
        elif len(i) == 3:
            tree.append(i[1])
            left[int(i[0])] = int(i[2])
        elif len(i) == 2:
            tree.append(i[1])
    words = ''
    # print(tree)
    print(f'#{tc} {in_order(1)}')