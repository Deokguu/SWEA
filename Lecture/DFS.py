# Practice 3
def dfs(st):
    STACK = []
    visited = [False] * (N+1)
    STACK.append(st)
    while STACK:    # STACK에 데이터가 있는 경우 len(STACK)>0
        v = STACK.pop(-1)
        # STACK에서 빼서 사용한다
        if not visited[v]:
            print(v)
            visited[v] = True
        print(v)

        for w in G[v]:
            if not visited[v]:
                STACK.append(w)

def dfs2(st):

    STACK = []
    visited = [False] * (N+1)

    STACK.append(st)
    visited[st] = True
    while STACK:
        v = STACK.pop(-1)
        print(v)

        for w in G[v]:
            if not visited[w]:
                STACK.append(w)
                visited[w] = True




lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# Graph = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], ...]
# v node와 연결된 노드들은? G[v]
N = 7
G = [[] for _ in range(N+1)]
# print(G)
for i in range(0, len(lst), 2):
    p1 = list[i]
    p2 = list[i+1]
    G[p1].append(p2)
    G[p2].append(p1)
# print(G)
# 그래프란 논리적인 자료구조. 2중 중첩된 리스트(2차원리스트)로 만듦

dfs(1)
print('===============')
visited = [False] * (N+1)

def dfs(v):
    print(v)
    visited