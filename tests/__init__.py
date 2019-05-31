"""
valitest: validatable test sets for machine translation
"""

# From: [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/)
import os
import sys


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# pylint: disable-msg=wrong-import-position,unused-import
from valitest import valitest
