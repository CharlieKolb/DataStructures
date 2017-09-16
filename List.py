class SinglyNode:
    def __init__(self, data, next_node=None):
        if data is None:
            raise ValueError("SinglyLinkedList.__init__(): data is None!")
        self.data = data
        self.next_node = next_node

    def at(self, index):
        if index == 0:
            return self.data
        if self.next_node is None or index < 0:
            raise IndexError("SinglyLinkedList.at(): index too low/high!")
        return self.next_node.at(index-1)

    def insert(self, data, index):
        if data is None:
            raise ValueError("SinglyNode.insert(): data is None!")
        if index < 0:
            raise IndexError("SinglyNode.insert(): index too low!")
        if index == 0:
            temp = SinglyNode(self.data, self.next_node)
            self.next_node = temp
            self.data = data
        elif index == 1:
            self.next_node = SinglyNode(data, self.next_node)
        elif self.next_node is None:
            raise IndexError("SinglyNode.insert(): index too high!")
        else:
            self.next_node.insert(data, index - 1)

    # call recursively until we find data, if found rotate out deleted data to last node and return true,
    # signaling successful removal, so that other nodes decrease length accordingly
    # returns new_head, bool_found_data
    def remove(self, data):
        if data == self.data:
            return self.next_node, True
        else:
            if self.next_node is None:
                return self, False
            self.next_node, found_data = self.next_node.remove(data)
            return self, found_data

    # merges the two lists and returns the new head
    def merge(self, other_head, index=0):
        if other_head is None:
            return self
        if index < 0:
            raise IndexError('SinglyNode.merge: index too low/high!')
        if index == 0:
            temp = other_head
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = self
            return other_head
        else:
            if self.next_node is None:
                if index == 1:
                    self.next_node = other_head
                else:
                    raise IndexError("SinglyNode.merge(): index too high!")
            else:
                self.next_node = self.next_node.merge(other_head, index - 1)
            return self

    def __repr__(self):
        out = repr(self.data)
        if self.next_node is None:
            return out
        out += ', ' + repr(self.next_node)
        return out


class DoublyNode:
    def __init__(self, data, prev_node=None, next_node=None):
        if data is None:
            raise ValueError("SinglyLinkedList.__init__(): data is None!")
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        out = repr(self.data)
        if self.next_node is None:
            return out
        out += ', ' + repr(self.next_node)
        return out


class SinglyLinkedList:
    def __init__(self, initializer_list=None):
        self.head = None
        self.length = 0
        if initializer_list is not None:
            for x in reversed(initializer_list):
                self.head = SinglyNode(x, self.head)
            self.length = len(initializer_list)
        self.iter_elem = self.head

    def at(self, index):
        if self.empty():
            raise IndexError("SinglyLinkedList.at(): list is empty!")
        return self.head.at(index)

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        return self.at(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_elem is None:
            self.iter_elem = self.head
            raise StopIteration()
        else:
            out = self.iter_elem.data
            self.iter_elem = self.iter_elem.next_node
            return out

    def empty(self):
        return self.head is None

    def add(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError("SinglyLinkedList.add(): index too high! Is {0}, length is {1}".format(index, self.length))
        if self.head is None:
            if index != 0:
                raise IndexError("SinglyLinkedList.add(): index too high! Is {0}, length is {1}".format(index, self.length))
            self.head = SinglyNode(data)
            self.iter_elem = self.head
        else:
            self.head.insert(data, index)
        self.length += 1

    def add_front(self, data):
        self.add(data, 0)

    def add_back(self, data):
        if self.head is None:
            self.head = SinglyNode(data)
            self.iter_elem = self.head
            self.length = 1
        else:
            self.add(data, self.length)

    def merge(self, other, index=0):
        if other is None:
            return
        if self.head is None:
            if index != 0:
                raise IndexError('SinglyLinkedList.merge(): This list was previously empty, and merge index was not 0!')
            self.head = other.head
            self.iter_elem = self.head
            self.length = other.length
        elif index < 0 or index > self.length:
            raise IndexError('SinglyLinkedList.merge(): index too low/high!')
        else:
            self.head = self.head.merge(other.head, index)
            self.iter_elem = self.head
            self.length += other.length

    # removes the first occurrence of the specified element and returns True if the element was found in the list
    def remove_elem(self, data):
        if self.head is None:
            return False
        self.head, found_data = self.head.remove(data)
        self.iter_elem = self.head
        if found_data:
            self.length -= 1
        return found_data

    # this runs in O(2 * n), whereas it could run in O(n) if the implement it separately
    def remove_index(self, index):
        found_data = self.remove_elem(self[index])
        return found_data

    def __str__(self):
        if self.empty():
            return '[]'
        out = '[' + repr(self.head) + ']'
        return out


class DoublyLinkedList:
    def __init__(self, initializer_list=None):
        self.front = None
        self.back = None
        self.length = 0
        if initializer_list is not None:
            self.length = len(initializer_list)
            new_front = None
            for x in initializer_list:
                temp = self.back
                self.back = DoublyNode(data=x, prev_node=temp)
                if temp is not None:
                    temp.next_node = self.back
                if new_front is None:
                    new_front = self.back
            self.front = new_front
        self.iter_elem = self.front
        self.iter_front = self.front

    def at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("DoublyLinkedList.at: Index too low/high. Length is {0}, index is {1}".
                             format(self.length, index))
        if index > self.length//2:
            temp = self.back
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev_node
            return temp.data
        else:
            temp = self.front
            for _ in range(0, index):
                temp = temp.next_node
            return temp.data

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        return self.at(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_front is not self.front:
            self.iter_elem = self.front
            self.iter_front = self.front
        if self.iter_elem is None:
            self.iter_elem = self.front
            raise StopIteration()
        else:
            out = self.iter_elem.data
            self.iter_elem = self.iter_elem.next_node
            return out

    def empty(self):
        return self.front is None

    def add(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError("DoublyLinkedList.add: Index too low/high. Length is {0}, index is {1}".
                             format(self.length, index))
        if index == 0:
            temp = self.front
            self.front = DoublyNode(data=data, prev_node=None, next_node=self.front)
            if temp is not None:
                temp.prev_node = self.front
            else:
                self.back = self.front
        elif index == self.length:
            temp = self.back
            self.back = DoublyNode(data=data, prev_node=self.back, next_node=None)
            if temp is not None:
                temp.next_node = self.back
            else:
                self.front = self.back
        else:
            current_node = None
            if index > self.length//2:
                current_node = self.back
                for _ in range(self.length - 1, index, -1):
                    current_node = current_node.prev_node
            else:
                current_node = self.front
                for _ in range(0, index):
                    current_node = current_node.next_node
            current_node.prev_node.next_node = DoublyNode(data=data, prev_node=current_node.prev_node, next_node=current_node)
            current_node.prev_node = current_node.prev_node.next_node
        self.length += 1

    def add_front(self, data):
        self.add(data=data, index=0)

    def add_back(self, data):
        self.add(data=data, index=self.length)

    def merge(self, other, index=0):
        pass

    # removes the first occurrence of the specified element and returns True if the element was found in the list
    def remove_elem(self, data):
        pass

    # this runs in O(2 * n), whereas it could run in O(n) if the implement it separately
    def remove_index(self, index):
        pass

    def __str__(self):
        if self.empty():
            return '[]'
        out = '[' + repr(self.front) + ']'
        return out
