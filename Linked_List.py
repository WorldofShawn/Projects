class Node:
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Node Data: {}".format(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        snakebody = list()
        current = self.head
        while current != None:
            if current == self.head:
                snakebody.append("[Head: {}]".format(current.data))
            elif current.next_node == None:
                snakebody.append("[Tail: {}]".format(current.data))
            else:
                snakebody.append("[{}]".format(current.data))
            current = current.next_node
        return "-->".join(snakebody)

    def search(self,key):
        current = self.head
        while current != None:
            if key == current.data:
                return current
            current = current.next_node
        return None

    def insert(self,data,index):
        if index > self.size():
            index = self.size()
        
        current = self.head
        new_node = Node(data)
        position = 0

        if index == 0:
            self.add(data)
        if index > 0:
            while current != None:
                if position == (index-1):
                    prev = current
                    after = current.next_node
                    current = new_node
                    prev.next_node = current
                    current.next_node = after
                    break
                else:
                    current = current.next_node
                    position += 1

    def delete(self,data):
        current = self.head
        while current != None:
            if current.data != data:
                prev = current
                current = current.next_node
            else:
                if current == self.head:
                    self.head = current.next_node
                else:
                    prev.next_node = current.next_node
                break


if __name__ == "__main__":
    Snake=LinkedList()
    Snake.add(10.1)
    Snake.add(20.2)
    Snake.add(30.3)
    Snake.add(40.4)

    print(Snake)

    Snake.delete(40.4)
    print(Snake)

    Snake.delete(20.2)
    print(Snake)