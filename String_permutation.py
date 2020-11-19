def utilstr(string, level):
    if level == len(result):
        print(result)
        return

    for i in string:
        if strii[i] == 0:
            continue
        
        result[level] = i
        strii[i] -= 1
        utilstr(strii, level + 1)
        strii[i] += 1

stri = input("Enter String for permutations:\n")
strii = { i: stri.count(i) for i in stri}
result = [None for i in range(len(stri))]
utilstr(strii, 0)




    
