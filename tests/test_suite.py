"""
valitest: validatable test sets for machine translation
"""
import unittest

from os import getcwd
from os.path import join


def run_tests():
    """Runs all test files in the tests/ folder."""
    loader = unittest.TestLoader()
    test_path = join(getcwd(), 'tests')
    suite = loader.discover(test_path)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
