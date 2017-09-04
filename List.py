class SinglyNode:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
        self.length = 1 if next_node is None else next_node.length + 1

    def insert(self, data, index):
        if index > self.length:
            raise IndexError("IndexOutOfBounds!")
        if index == 0:
            temp = SinglyNode(data, self.next_node)
            self.next_node = temp
            self.length = self.next_node.length + 1
        else:
            self.insert(data, index - 1)
            self.length += 1

    # call recursively until we find data, if found rotate out deleted data to last node and return true,
    # signaling successful removal, so that other nodes decrease length accordingly
    def remove(self, data):
        if data == self.data:
            current = self
            while current.next_node is not None:
                current.data = current.next_node.data
                current.length -= 1
                if current.length == 0:
                    current.next_node = None
                else:
                    current = current.next_node
            return True
        else:
            if self.next_node is None:
                return False
            elif self.next_node.remove(data):
                self.length -= 1
                return True
            else :
                return False

'''
class SinglyLinkedList:
    def __init__(self, data = None, head = None):
        self.head = head
        self.data = data

    def add(self, data, index):
        temp = self.head
        prev = None
        while index > 0:
            prev = temp
            temp = temp.head
            index -= 1
        if prev is None:
            return SinglyLinkedList(data, self.head)
        else:
            prev.head = SinglyLinkedList(data, temp)
            return self.head

    def add_front(self, data):
        return SinglyLinkedList(data, self.head)

    def add_back(self, data):
        return add(data, )
'''