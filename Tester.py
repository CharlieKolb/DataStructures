import random
import unittest
import List

TestClass = List.SinglyLinkedList


def random_list(lower_bound=0, upper_bound=100, size=10):
    return random.sample(range(lower_bound, upper_bound), size)


class TestAddMethods(unittest.TestCase):
    def test_add_last(self):
        data = random_list()
        test_struct = TestClass()
        test_data = []
        for i in range(len(data)):
            test_data.append(data[i])
            test_struct.add_back(data[i])
            print("{0} vs {1}".format(test_data[i], test_struct.at(i)))
            self.assertEqual(test_data[i], test_struct.at(i))

    def test_add_first(self):
        data = random_list()
        test_struct = TestClass()
        test_data = []
        for i in range(len(data)):
            test_data.insert(0, data[i])
            test_struct.add_front(data[i])
            print("{0} vs {1}".format(test_data[0], test_struct.at(0)))
            self.assertEqual(test_data[0], test_struct.at(0))

    def test_add_random_index(self):
        data = random_list()
        test_struct = TestClass()
        test_data = []
        for i in range(len(data)):
            test_data.insert(0, data[i])
            test_struct.add_front(data[i])
            print("{0} vs {1}".format(test_data[0], test_struct.at(0)))
            self.assertEqual(test_data[0], test_struct.at(0))

if __name__ == '__main__':
    unittest.main()
