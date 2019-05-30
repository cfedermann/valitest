"""
valitest: validatable test sets for machine translation
"""

import xmlschema


class ValidatableTestSet:
    """
    Test set for machine translation, which can be validated.

    Based on SGML format used at the Conference on Machine Translation
    (WMT; see, e.g., http://statmt.org/wmt19/) but adding XSD schema for
    validation of test sets and corresponding translation outputs.
    """

    def __init__(self, setid, srclang):
        """Load schema for validation."""
        self.schema = xmlschema.XMLSchema('valitest.xsd')

        self.__setid = setid
        self.__srclang = srclang

    @property
    def setid(self):
        """Gets set id for this test set."""
        return self.__setid

    @setid.setter
    def setid(self, val):
        """Sets set id for this test set."""
        self.__setid = val

    @property
    def srclang(self):
        """Gets srclang for this test set."""
        return self.__srclang

    @srclang.setter
    def srclang(self, val):
        """Sets srclang for this test set."""
        self.__srclang = val

    def __str__(self):
        """Human readable representation."""
        return '{0} ({1})'.format(self.setid, self.srclang)

    def __repr__(self):
        """Machine readable representation."""
        return 'ValidatableTestSet(setid={0}, srclang={1})'.format(
            self.setid, self.srclang
        )
