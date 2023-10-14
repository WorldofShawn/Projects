def selection_sort (user_list):
    sorted_list = list()
    for index in range(len(user_list)):
        sorted_list.append(user_list.pop(index_min(user_list)))
    return sorted_list

def index_min(user_list):
    for index in range(len(user_list)):
        if index == 0:
            min = index
        else:
            if user_list[index] < user_list[min]:
                min = index
    return min

randomlist = [57, 80, 25, 89, 92, 100, 20.1, 10.5, 20, 30.7]

print(selection_sort(randomlist))