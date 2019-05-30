"""
valitest: validatable test sets for machine translation
"""
import unittest

from os import getcwd


def run_tests():
    """Runs all test files in the tests/ folder."""
    loader = unittest.TestLoader()
    suite = loader.discover(getcwd())
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
