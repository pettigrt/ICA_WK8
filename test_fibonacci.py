import unittest
import pytest
import fibonacci

def test_fibonacci_zero():
    assert fibonacci.fib(0) == 0

def test_fibonacci_one():
    assert fibonacci.fib(1) == 1

def test_fibonacci_random_val():
    assert fibonacci.fib(20) == 6765

#unittest test class
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(0, fibonacci.fib(0))

    def test_fibonacci_val(self):
        self.assertEqual(34, fibonacci.fib(9))

    def test_fibonacci_one(self):
        self.assertEqual(1, fibonacci.fib(1))

    def test_fibonacci_invalid(self):
        self.assertEqual(0, fibonacci.fib(-3))

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(1, fibonacci.factorial(0))

    def test_factorial_invalid(self):
        self.assertEqual(1, fibonacci.factorial(0))

    def test_factorial_random(self):
        self.assertEqual(6, fibonacci.factorial(3))

if __name__ == "__main__":
    unittest.main()