#import python unit test library
import unittest
#import function we want to test
from json_ex import check_char_count
from json_ex import check_char_type

#create class to test file
class TestJsonEx(unittest.TestCase):

    #function (method) inside class
    def test_check_char_count(self):
        #method assertEqual(a,b) checks that a == b
        self.assertEqual(check_char_count('AA'), 'AA count passes')
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
        #will raise a type error if int
        self.assertRaises(AssertionError, check_char_count, 1)
        #will raise a type error if boolean
        self.assertRaises(AssertionError, check_char_count, True)
        #will raise a type error if list
        self.assertRaises(AssertionError, check_char_count, ['AA', 'BB'])

    def test_check_char_type(self):
        self.assertEqual(check_char_type('AA'), 'AA type passes')
        self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
        self.assertEqual(check_char_type('aa'), 'aa type FAILS')
        self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
        self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
        self.assertRaises(AttributeError, check_char_type, 1)
        self.assertRaises(AttributeError, check_char_type, True)
        self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])

    def test_check_char_match(self):
        self.assertEqual(check_char_match('AZ', 'Arizona'), 'AZ match passes')
        self.assertEqual(check_char_match('AZ', 'Brizona'), 'AZ match FAILS')
        self.assertEqual(check_char_match('BZ', 'Arizona'), 'BZ match FAILS')
        self.assertEqual(check_char_match('1Z', 'Arizona'), '1Z match FAILS')
        self.assertRaises(IndexError, check_char_match, 'AA', '')
        self.assertRaises(IndexError, check_char_match, '', 'AA')
        self.assertRaises(IndexError, check_char_match, '', '')
        self.assertRaises(TypeError, check_char_match, 1, 1)
        self.assertRaises(TypeError, check_char_match, 1, 'AA')
        self.assertRaises(TypeError, check_char_match, True, 'AA')
        self.assertRaises(TypeError, check_char_match, ['AA', 'BB'], ['AA', 'BB'])

#calls main function to execute script
if __name__ == '__main__':
    unittest.main()
