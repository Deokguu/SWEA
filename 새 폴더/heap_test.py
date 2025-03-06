def enq(value):
    global last_pos
    TREE[last_pos] += 1
    TREE[last_pos] = value

    c = last_pos
    p = c // 2
    while c > 1 and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = p//2
TREE = [0, 20, 15, 19, 4, 13, 11] + [0] * 100
last_pos = 6

def deq():
    global last_pos
    result = TREE[1] #저장했다가 리턴할거야
    TREE[1] = TREE[last_pos]
    last_pos -= 1

    p = 1
    c = 2*p #left
    while c<=last_pos: #c는 left를 유지하도록
        if c+1 <= last_pos and [c] < TREE[c+1]:
            c = c+1
        else:
            c = p*2

        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c *= 2
        else:
            break




    return result

print(deq())
print(TREE)