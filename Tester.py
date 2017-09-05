import random
import unittest
import List


def random_list(lower_bound=0, upper_bound=100, size=10):
    return random.sample(range(lower_bound, upper_bound), size)


class TestAddMethods(unittest.TestCase):
    def test_add_last(self):
        data = random_list()
        test_struct = List.SinglyLinkedList()
        test_data = []
        for i in range(len(data)):
            test_data.append(data[i])
            test_struct.add_back(data[i])
            print("{0} vs {1}".format(test_data[i], test_struct.at(i)))
            self.assertEqual(test_data[i], test_struct.at(i))


if __name__ == '__main__':
    unittest.main()
