import random
import unittest
import List

TestClass = List.SinglyLinkedList


def random_list(lower_bound=0, upper_bound=100, size=10):
    return random.sample(range(lower_bound, upper_bound), size)


def content_equal(solution, answer):
    for i in range(len(solution)):
        if solution[i] != answer.at(i):
            return False
    return True


class TestAddMethods(unittest.TestCase):
    def test_add_last(self):
        test_struct = TestClass()
        test_data = []
        # print()
        for i in random_list():
            test_data.append(i)
            test_struct.add_back(i)
        for i in range(len(test_data)):
            # print("{0} vs {1}".format(test_data[i], test_struct.at(i)))
            self.assertEqual(test_data[i], test_struct.at(i))

    def test_add_first(self):
        test_struct = TestClass()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
        self.assertTrue(content_equal(test_data, test_struct))

    def test_add_random_index(self):
        test_struct = TestClass()
        test_data = []
        # print()
        for i in random_list():
            test_data.insert(0, i)
            test_struct.add_front(i)
            # print("{0} vs {1}".format(test_data[0], test_struct.at(0)))
        self.assertTrue(content_equal(test_data, test_struct))

    def test_merge(self):
        first, second = random_list(), random_list()
        test_struct_first, test_struct_second = TestClass(), TestClass()
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
        test_struct = TestClass()
        for i in random_list():
            test_struct.add_back(i)
        counter = 0

        for x in test_struct:
            self.assertEqual(x, test_struct[counter])
            counter += 1

if __name__ == '__main__':
    unittest.main()
