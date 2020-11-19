def merge(list1, list2):
    i, j = 0, 0
    merge_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    if i == len(list1):
        merge_list += list2[j:]
    if j == len(list2):
        merge_list += list1[i:]
    return merge_list


def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)//2
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


print(merge_sort([5, 4, 3, 2, 1]))
