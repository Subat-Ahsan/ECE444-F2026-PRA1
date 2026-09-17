import unittest

from utils import Utils


class UtilsTests(unittest.TestCase):

    def setUp(self):
        self.utils = Utils()


    def test_reversed_with_integer(self):
        self.assertEqual(self.utils.reversed(12345), 54321)
        self.assertEqual(self.utils.reversed(100), 1)
        self.assertEqual(self.utils.reversed(-123), -321)
        self.assertEqual(self.utils.reversed(0), 0)

    def test_reversed_with_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.utils.reversed("12345")

    def test_reversed_with_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.utils.reversed(123.45)


    def test_formatter_with_integer(self):
        result = self.utils.formatter(10)
        self.assertEqual(result, ("0b1010", "0o12"))

    def test_formatter_with_negative_integer(self):
        result = self.utils.formatter(-10)
        self.assertEqual(result, ("-0b1010", "-0o12"))

    def test_formatter_with_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.utils.formatter("10")

    def test_formatter_with_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.utils.formatter(10.5)


if __name__ == "__main__":
    unittest.main()