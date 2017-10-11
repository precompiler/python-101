from ut.filter_funcs import filter_ints
from unittest import TestCase
from unittest.mock import patch, call

class FilterIntsTest(TestCase):
    @patch("ut.filter_funcs.is_positive")
    def test_filter_ints(self, is_positive_mock):
        v = [3, -4, 0, 5, 8]
        ret = filter_ints(v)
        self.assertEqual([call(3), call(-4), call(0), call(5), call(8)], is_positive_mock.call_args_list)
        print(ret)