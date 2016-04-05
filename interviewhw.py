'''
Created on March, 2016

@author: oovadia

Programming assignment for the job interview
Testing:

    python -munittest interviewhw
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK

'''
import unittest


# ===============================================================================
# ascii array sort question
# ===============================================================================
class BArrSorter(object):
    '''
    use to sort array of bytes (bytearray / str) with merge sort,
    if given input is a string it will be converted to bytearry
    Usage:
    >>> sorter = BArrSorter()
    >>> sorter('oren')
    bytearray(b'enor')
    >>> sorter('1243')
    bytearray(b'1234')
    '''

    def _calc_middle(self, start, end):
        return (start + end) / 2

    def _merge(self, merged_arr, left, right):
        total_len = len(merged_arr)
        i_left, i_right = 0, 0
        len_left, len_right = len(left), len(right)
        for k in xrange(total_len):
            if (i_left < len_left and (i_right >= len_right or left[i_left] <= right[i_right])):
                merged_arr[k] = left[i_left]
                i_left += 1
            else:
                merged_arr[k] = right[i_right]
                i_right += 1
        return merged_arr

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        end = len(arr)
        mid = self._calc_middle(0, end)
        left = self._merge_sort(arr[0:mid])  # slicing a list or bytearray is not in place
        right = self._merge_sort(arr[mid:end])
        return self._merge(arr, left, right)

    def sort(self, arr):
        return self._merge_sort(bytearray(arr))

    def __call__(self, arr):
        return self.sort(arr)


def merge_sort(arr):
    '''
    use to sort array of bytes with merge sort, 
    if given input is a string it will be converted to bytearry
    Usage:
    >>> 
    >>> merge_sort('oren')
    bytearray(b'enor')
    >>> merge_sort('1243')
    bytearray(b'1234')
    '''
    return BArrSorter()(arr)


# ===============================================================================
# bracket test part
# ===============================================================================
def check_pair_of_brackets(open_brk, close_brk):
    '''
    returns True if open_brk and close_brk both open and close the same type of brackets:
    e.g:
    >>> check_pair_of_brackets('{','}')
    True
    >>> check_pair_of_brackets('{',']')
    False
    >>> check_pair_of_brackets('{','a')
    False
    '''
    oc_brk = open_brk + close_brk
    return oc_brk in ('()', '{}', '[]')


def verify_brackets(brk_str):
    '''
    Returns True of brk_str has a valid bracket structure
    meaning, all brackets are closed properly
    False O.W
    Usage:
    >>> verify_brackets('[12{3}33]1()')
    True
    >>> verify_brackets('[(]')
    False
    '''
    brk_lifo = []
    for c in brk_str:
        if c in '{[(':
            brk_lifo.append(c)
        elif c in '}])':
            if not brk_lifo:
                return False
            open_brk = brk_lifo.pop(-1)  # get the last bracket from the lifo
            if not check_pair_of_brackets(open_brk, c):
                return False
        else:
            continue
    if brk_lifo:
        return False  # some brackets did not close
    return True


# ===============================================================================
# testing classes (unittest format)
# ===============================================================================
class SortingTests(unittest.TestCase):
    def test_sorts(self):
        sorter = BArrSorter()
        test_cases = [('12', '12'),
                      ('123', '123'),
                      ('312', '123'),
                      ('321', '123'),
                      ('4231', '1234'),
                      ('abcd', 'abcd'),
                      ('dcba', 'abcd'),
                      ('dbac', 'abcd'),
                      ('dbeac', 'abcde'),
                      ]
        for s, ret in test_cases:
            assert sorter(s) == ret, 'Checking sort of %s to %s' % (s, ret)
            assert merge_sort(s) == ret, 'Checking sort of %s to %s (via merge_sort function interface)' % (s, ret)

    def test_merge(self):
        sorter = BArrSorter()
        left, right = bytearray('ab'), bytearray('cd')
        merged_arr = bytearray('stam')
        assert sorter._merge(merged_arr, left, right) == 'abcd'
        left, right = bytearray('ac'), bytearray('bd')
        merged_arr = bytearray('stam')
        assert sorter._merge(merged_arr, left, right) == 'abcd'


class BracketTests(unittest.TestCase):
    def test_check_pair_of_brackets(self):
        test_cases = [('{', '}', True),
                      ('[', ']', True),
                      ('(', ')', True),
                      ('{', ')', False),
                      ('a', ')', False),

                      ]
        for a, b, ret in test_cases:
            assert check_pair_of_brackets(a, b) == ret, 'Checking test_check_pair_of_brackets with %s and %s eq %s' % (
                a, b, ret)

    def test_brk(self):
        test_cases = [('{}', True),
                      ('[]', True),
                      ('()', True),
                      ('{)', False),
                      ('a)', False),
                      ('[](', False),
                      ('([]', False),
                      (')', False),
                      ('(', False),
                      ('([)', False),
                      ('[1{2()3333}1]', True),

                      ]
        for s, ret in test_cases:
            assert verify_brackets(s) == ret, 'Checking test_brk with %s eq %s' % (s, ret)


if __name__ == "__main__":
    unittest.main(verbosity=2)
