def merge_sort (list):
    
    if len(list) <=1:
        return list
    
    else:
        left_list, right_list = split(list)
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
    
    return merge(left_list, right_list)

def split(list):
    middle = len(list)//2
    left_list = list[:middle]
    right_list = list[middle:]

    return left_list, right_list

def merge(left_list, right_list):
    i = 0
    j = 0
    merged_list=list()

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1
    return merged_list

TestList = [57, 23, 100, 30, 1, 5, 10, 7, 3, 67, 72, 52, 32]
TestList2 = [57, 23, 100, 30, 1, 10, 7, 3, 67, 72, 52, 32]
TestList3 = [1, 2, 3, 4, 20, 10, 13, 14]
TestList4 = [1, 2, 3, 4, 20, 10, 14, 13, 25]
TestList5 = [1, 2, 3, 4, 20, 20, 25, 10, 14, 13, 25]

print(merge_sort(TestList))
print(merge_sort(TestList2))
print(merge_sort(TestList3))
print(merge_sort(TestList4))
print(merge_sort(TestList5))