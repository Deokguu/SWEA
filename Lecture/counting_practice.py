def counting():
    cnts = [0] * 10 # cnts[0]은 0의 개수, ... cnts[9] / cnt를 변수 하나로 안되고 배열로 써야한다

    for number in numbers:
        cnts[number] += 1

    print(cnts)

    for i in range(9):
        cnts[i+1] = cnts[i] + cnts[i+1]
    print(cnts)

    temp = [-1] * N
    for number in numbers:
        # pos = cnts[number] - 1
        # temp[pos] = number
        # cnts[number] -= 1

        cnts[number] -= 1
        temp[cnts[number]] = number

    print(temp)





N = 8
numbers = [0, 4, 1, 3, 1, 2, 4, 2]
    #
    # [0, 0, 0, 0, 0, 0, 0, 0]
counting()