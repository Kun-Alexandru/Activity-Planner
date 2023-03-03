import unittest
from src.a10.sort_filter_iterable_data import *

class RepositoryActivityTest(unittest.TestCase):

    def test_len_iterable_data__list_itterable_data__correct_lenght(self):
        List = ItterableDataStructure([3, -4, 5, -8])
        self.assertEqual(len(List),4)

    def test_del_iterable_data__list_with_valid_key__element_removed(self):
        List = ItterableDataStructure([4, -4, 5, -8])
        del List[3]
        self.assertEqual(len(List), 3)

    def test_append_iterable_data__list___True(self):
        List = ItterableDataStructure([4, -4, 5, -8])
        self.assertTrue(List.append(10))

    def test_append_iterable_data__dictionary__False(self):
        List = ItterableDataStructure()
        self.assertFalse(List.append(10))

    def test_standard_compare__1st_bigger__False(self):
        self.assertFalse(standard_compare(5,3))

    def test_standard_compare__1st_smaller__True(self):
        self.assertTrue(standard_compare(3,5))

    def test_standard_filter_function__negative_number__True(self):
        self.assertTrue(standard_function_filter(-3))

    def test_standard_filter_function__positive_number__False(self):
        self.assertFalse(standard_function_filter(3))

    def test_gnomeSort__valid_list___correct_ordered_list(self):
        List = [3, -4, 5, -8]
        List = ArrayOperations.gnomeSort(List)
        self.assertEqual(List, [-8,-4,3,5])

    def test_filter__valid_list__correct_filtered_list(self):
        List = [3, -4, 5, -8]
        List = ArrayOperations.selfFilter(List)
        self.assertEqual(List, [-4,-8])

    def test_next__dictionary_itterable_type__next_index_in_dict(self):
        Dictionary = ItterableDataStructure()
        Dictionary[3]="a"
        Dictionary[7]="b"
        nextIndex = Dictionary.next()
        self.assertEqual(nextIndex,3)

    def test_next__dictionary__StopIteration(self):
        Dictionary = ItterableDataStructure()
        Dictionary[3] = "a"
        Dictionary[7] = "b"
        Dictionary.next()
        Dictionary.next()
        with self.assertRaises(StopIteration):
            Dictionary.next()


