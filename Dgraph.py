from math import gcd


def graph(origin, destination, k):
    mp = {}
    for i in range(len(origin)):
        for j in range(len(destination)):
            if gcd(origin[i], destination[j]) >= k:
                if origin[i] not in mp:
                    mp[origin[i]] = []
                mp[origin[i]].append(destination[j])
    print(mp)


def main():
    origin = [2, 3, 4, 6, 3, 6, 8]
    dest = [6, 8, 2, 6, 2, 8, 0, 2]
    k = 0
    graph(origin, dest, k)


main()
