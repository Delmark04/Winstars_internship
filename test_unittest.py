# from unittest import TestCase
import numpy as np
# import pickle
import unittest

class input_test(unittest.TestCase):
    def setUp(self):
        self.csv_data = np.loadtxt("data.csv", delimiter=',')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # def std_(self):
        # with open('data.csv') as ifile:
        #     for iline in ifile:
        #         self.assertEqual(round(iline.std()), 0.0)

    # for i in self.XXX:
        #     self.assertEqual(round(i.std()), 0.0)

    def mean_(self):
        for i in self.csv_data:
            self.assertEqual(round(np.mean(i), 0.0))

if __name__ == '__main__':
    unittest.main()