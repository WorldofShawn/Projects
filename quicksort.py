def quick_sort(user_list):
    if user_list == None or len(user_list) <= 1:
        return user_list
    else:
        pivot = user_list[0]
        less_pivot = list()
        greater_pivot = list()
        
        for num in user_list[1:]:
            if num <= pivot:
                less_pivot.append(num)
            else:
                greater_pivot.append(num)

        less_pivot = quick_sort(less_pivot)
        greater_pivot = quick_sort(greater_pivot)      
        sorted_list = less_pivot + [pivot] + greater_pivot
    return sorted_list



randomlist = [57, 80, 25, 92, 89, 100, 20.1, 10.5, 20, 30.7]

print(quick_sort(randomlist))