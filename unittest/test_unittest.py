import numpy as np
import unittest


class InputTest(unittest.TestCase):
    def setUp(self):
        self.csv_data = np.loadtxt("data.csv", delimiter=',')

    def test_std(self):
        for i in self.csv_data:
            self.assertEqual(round(i.std()), 0.0, "Error, std is not 0")

    def test_mean(self):
        for i in self.csv_data:
            self.assertTrue(round(np.mean(i)) in [0.0, 1.0], "Error, mean value is not in range (0, 1)")

    def test_type(self):
        self.assertEqual(type(self.csv_data), np.ndarray, "Type error, data is not np.ndarray")


if __name__ == '__main__':
    unittest.main()
