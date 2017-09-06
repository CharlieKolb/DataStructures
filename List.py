class SinglyNode:
    def __init__(self, data, next_node=None):
        if data is None:
            raise ValueError("SinglyLinkedList.__init__(): data is None!")
        self.data = data
        self.next_node = next_node
        self.length = 1 if next_node is None else next_node.length + 1

    def at(self, index):
        if index == 0:
            return self.data
        if self.next_node is None or index < 0 or index >= self.length:
            raise IndexError("SinglyLinkedList.at(): index too low/high!")
        return self.next_node.at(index-1)

    def insert(self, data, index):
        if data is None:
            raise ValueError("SinglyLinkedList.insert(): data is None!")
        if index > self.length:
            raise IndexError("IndexOutOfBounds!")
        if index == 0:
            temp = SinglyNode(self.data, self.next_node)
            self.next_node = temp
            self.data = data
        elif index == 1:
            self.next_node = SinglyNode(data, self.next_node)
        else:
            self.next_node.insert(data, index - 1)
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
            else:
                return False

    # merges the two lists and returns the new head
    def merge(self, otherHead, index=0):
        if otherHead is None:
            return self
        if index < 0 or index > self.length:
            raise IndexError('SinglyNode.merge: index too low/high!')
        if index == 0:
            otherHead.length += self.length
            otherHead.insert(self, otherHead.length)
            return otherHead
        elif self.next_node is None:
            self.length += otherHead.length
            self.next_node = otherHead
            return self
        else:
            self.next_node.merge(otherHead, index-1)
            return self



class SinglyLinkedList:
    # ToDo: Add a kind of initializer_list? maybe that *args / **kwargs thingy?
    def __init__(self):
        self.head = None

    def at(self, index):
        if self.head is None:
            raise IndexError("SinglyLinkedList.at(): list is empty!")
        return self.head.at(index)

    def __getitem__(self, item):
        return self.at(item)

    def empty(self):
        return self.head is None

    def add(self, data, index):
        if self.head is None:
            if index != 0:
                raise IndexError("SinglyLinkedList.add(): index too high!")
            self.head = SinglyNode(data)
        else:
            self.head.insert(data, index)

    def add_front(self, data):
        self.add(data, 0)

    def add_back(self, data):
        if self.head is None:
            self.head = SinglyNode(data)
        else:
            self.add(data, self.head.length)

    def merge(self, other, index=0):
        if other is None:
            return
        if self.head is None:
            if index != 0:
                raise IndexError('SinglyLinkedList.merge(): This list was previously empty, and merge index was not 0!')
            self.head = other.head
        elif index < 0 or index > self.head.length:
            raise IndexError('SinglyLinkedList.merge(): index too low/high!')
        else:
            self.head = self.head.merge(other.head)

