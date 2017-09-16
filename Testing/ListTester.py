import random
import unittest
import List


def random_list(lower_bound=0, upper_bound=100, size=10):
    return random.sample(range(lower_bound, upper_bound), size)


def content_equal(solution, answer):
    # print(solution, answer)
    # print('{0} vs {1}'.format(len(solution), len(answer)))
    if len(solution) != len(answer):
        return False
    for i, x in enumerate(answer):
        if solution[i] != answer.at(i) or x != answer.at(i):
            # print('{0} vs {1} vs {2}'.format(solution[i], answer.at(i), x))
            return False
    return True


class TestSinglyLinkedList(unittest.TestCase):
    def test_add_last(self):
        test_struct = List.SinglyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.append(i)
            test_struct.add_back(i)
        for i in range(len(test_data)):
            # print("{0} vs {1}".format(test_data[i], test_struct.at(i)))
            self.assertEqual(test_data[i], test_struct.at(i))

    def test_add_first(self):
        test_struct = List.SinglyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
        self.assertTrue(content_equal(test_data, test_struct))

    def test_add_random_index(self):
        test_struct = List.SinglyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
            # print("{0} vs {1}".format(test_data[0], test_struct.at(0)))
        self.assertTrue(content_equal(test_data, test_struct))

    def test_merge(self):
        first, second = random_list(), random_list()
        test_struct_first, test_struct_second = List.SinglyLinkedList(), List.SinglyLinkedList()
        for elem in first:
            test_struct_first.add_back(elem)
        for elem in second:
            test_struct_second.add_back(elem)
        index = random.randint(0, len(first) - 1)
        first = first[:index] + second + first[index:]
        test_struct_first.merge(test_struct_second, index)
        # print()
        self.assertTrue(content_equal(first, test_struct_first))

    def test_iteration(self):
        test_struct = List.SinglyLinkedList(random_list())
        counter = 0
        for x in test_struct:
            self.assertEqual(x, test_struct[counter])
            counter += 1
        self.assertEqual(counter, len(test_struct))

    def test_delete_index(self):
        data = random_list()
        test_list = List.SinglyLinkedList(data)
        # print()
        while len(data) > 0:
            rand_index = random.randint(0, len(data) - 1)
            data.remove(data[rand_index])
            test_list.remove_index(rand_index)
            # print(data, test_list)
            self.assertTrue(content_equal(data, test_list))


class TestDoublyLinkedList(unittest.TestCase):
    def test_at(self):
        data = random_list()
        test_struct = List.DoublyLinkedList(data)
        print(data, test_struct)
        for i, x in enumerate(test_struct):
            self.assertEqual(x, test_struct[i])

    def test_length(self):
        data = random_list()
        test_struct = List.DoublyLinkedList(data)
        self.assertEqual(len(test_struct), len(data))

    def test_add_last(self):
        test_struct = List.DoublyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.append(i)
            test_struct.add_back(i)
        for i in range(len(test_data)):
            # print("{0} vs {1}".format(test_data[i], test_struct.at(i)))
            self.assertEqual(test_data[i], test_struct.at(i))

    def test_add_first(self):
        test_struct = List.DoublyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
        self.assertTrue(content_equal(test_data, test_struct))

    def test_add_random_index(self):
        test_struct = List.DoublyLinkedList()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
            # print("{0} vs {1}".format(test_data[0], test_struct.at(0)))
        self.assertTrue(content_equal(test_data, test_struct))

    def test_merge(self):
        first, second = random_list(), random_list()
        test_struct_first, test_struct_second = List.DoublyLinkedList(), List.DoublyLinkedList()
        for elem in first:
            test_struct_first.add_back(elem)
        for elem in second:
            test_struct_second.add_back(elem)
        index = random.randint(0, len(first) - 1)
        first = first[:index] + second + first[index:]
        test_struct_first.merge(test_struct_second, index)
        # print()
        self.assertTrue(content_equal(first, test_struct_first))

    def test_iteration(self):
        test_struct = List.DoublyLinkedList(random_list())
        counter = 0
        for x in test_struct:
            self.assertEqual(x, test_struct[counter])
            counter += 1
        self.assertEqual(counter, len(test_struct))

    def test_delete_index(self):
        data = random_list()
        test_list = List.DoublyLinkedList(data)
        # print()
        while len(data) > 0:
            rand_index = random.randint(0, len(data) - 1)
            data.remove(data[rand_index])
            test_list.remove_index(rand_index)
            # print(data, test_list)
            self.assertTrue(content_equal(data, test_list))

if __name__ == '__main__':
    unittest.main()
