'''
x = input()
x = x.split()
n = int(x[0])
k = int(x[1])
Q = int(x[2])

ar = input().split()
queries = []
while Q > 0:
    queries.append(int(input()))
    Q -= 1


'''

print(set(input().split()))
print(n, k, q)

n, k, Q = 5, 2, 4
ar = ['2', '1', '3', '2', '3']
queries = [6, 2, 10, 15]
que = [int(i) for i in ar]      # [2,1,3,2,3]

# [4,3,2,1]
# [1,2,3,4]
# new_list = to_copy_list[:]      temp = ar[:]


def deque(attack):
    temp = []
    for i in range(len(attack)):
        if attack[i][1] <= 0:
            continue
        temp.append(attack[i])
    if len(temp) < 1:
        return -1
    return temp


def que_1(t, attack):
    result = [-1 for _ in range(len(queries))]
    for i in range(t):
        if attack[0][0] == 0:
            temp = attack.pop(0)
            temp[1] -= k
            if temp[1] != 0:
                attack.append(temp)
        else:
            temp = attack.pop(0)
            temp[1] -= 1
            if temp[1] != 0:
                attack.append(temp)
        attack = deque(attack)
        if attack == -1:
            return result
        if i+1 in queries:
            idx = queries.index(i+1)
            x = []
            for j in range(len(attack)):
                x.append(attack[j][0] + 1)
            result[idx] = x

    return result


attack = [[i, int(ar[i])] for i in range(len(ar))]
q_max = max(queries)
result = que_1(q_max, attack)
print(result)
