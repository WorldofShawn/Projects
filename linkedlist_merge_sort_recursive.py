from Linked_List import LinkedList

def merge_sort(linked_list):

    if linked_list.head == None or linked_list.head.next_node == None:
        return linked_list
    
    else:
        left_list, right_list = split(linked_list)
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        return merge(left_list,right_list)

def split(linked_list):
    mid = linked_list.size()//2
    current = linked_list.head
    left_list = linked_list
    right_list = LinkedList()
    position = 0

    while position < mid:
        if position == (mid-1):
            right_list.head = current.next_node
            current.next_node = None
            break

        current = current.next_node
        position += 1

    return left_list, right_list

def merge(left_list, right_list):
    merged_list = LinkedList()
    merged_list.add(0)
    current = merged_list.head
    left = left_list.head
    right = right_list.head

    while left != None or right != None:
        if left == None:
            current.next_node = right
            right = right.next_node
        elif right == None:
            current.next_node = left
            left = left.next_node
        else:
            if left.data > right.data:
                current.next_node = right
                right = right.next_node
            else:
                current.next_node = left
                left = left.next_node
        current = current.next_node
    merged_list.head = merged_list.head.next_node
    return merged_list

Worm = LinkedList()
Worm.add(20)
Worm.add(75)
Worm.add(30.3)
Worm.insert(3.3,5)
Worm.add(40.4)
print(Worm)
Worm.delete(3.3)
print(Worm)
print(merge_sort(Worm))
