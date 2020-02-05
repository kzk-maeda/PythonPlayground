import pytest
import unittest
import calcuration

release_name = 'dev'

# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('set up')
#         self.cal = calcuration.Cal()

#     def tearDown(self):
#         print('tear down')
#         del self.cal

#     # @unittest.skip('skip')
#     @unittest.skipIf(release_name=='test', 'skip test!')
#     def test_add_num_and_double(self):
#         self.assertEqual(
#             self.cal.add_num_and_double(1, 1),
#             4
#         )
        
#     def test_add_num_and_double_raise(self):
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double('1', '1')

class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = calcuration.Cal()

    @classmethod
    def teardown_class(cls):
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calcuration.Cal()
    
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4
    
    @pytest.mark.skip(reason='skip')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')