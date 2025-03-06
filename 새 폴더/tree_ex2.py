def pre_order(n): #완전이진트리의 전위순회 / 파이썬은 읽기(값 참조)만 할 거면  global 선언하지 않아도 되는데 쓸 거면 선언해야함
    if n <= N: # 실존하는 정점이면 if T:
        print(n) # visit(T)
        pre_order(n*2) # pre_order(left[T])
        pre_order(n*2+1) # pre_order(right[T])

N = 9 # 완전이진트리 정점 수
tree = [0, 33 , 31, 27, 21, 22,18 ,23, 14, 19] #정점번호를 인덱스로 하는 배열에 key값 저장
pre_order(1)

