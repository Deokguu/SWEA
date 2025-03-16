def post_order(root_idx): 
    if root_idx:
        post_order(left[root_idx])
        post_order(right[root_idx])
        if tree[root_idx] == '/':
            tree[root_idx] = tree[left[root_idx]] / tree[right[root_idx]]
        elif tree[root_idx] == '*':
            tree[root_idx] = tree[left[root_idx]] * tree[right[root_idx]]
        elif tree[root_idx] == '+':
            tree[root_idx] = tree[left[root_idx]] + tree[right[root_idx]]
        elif tree[root_idx] == '-':
            tree[root_idx] = tree[left[root_idx]] - tree[right[root_idx]]
        
T = 10

for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    parent = [0] * (N+1)
    tree = [0] * (N+1)
    for _ in range(N):
        arr = input().split()

        if len(arr) == 4:
            a, b, c, d = arr
            parent[int(c)] = int(a)
            parent[int(d)] = int(a)
            tree[int(a)] = b
            left[int(a)] = int(c)
            right[int(a)] = int(d)
        else:
            a, b = arr
            tree[int(a)] = int(b)
    post_order(1)
    print(f'#{tc} {int(tree[1])}')
