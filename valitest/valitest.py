"""
valitest: validatable test sets for machine translation
"""

import xml

import xmlschema


class ValidatableTestSet:
    """
    Test set for machine translation, which can be validated.

    Based on SGML format used at the Conference on Machine Translation
    (WMT; see, e.g., http://statmt.org/wmt19/) but adding XSD schema for
    validation of test sets and corresponding translation outputs.
    """

    def __init__(self, xml_path):
        """
        Creates validatable test set from given XML path.

        Validates contents from XML file against valitest XSD schema.
        """
        # Load XSD schema for document validation
        self.__schema = xmlschema.XMLSchema('valitest.xsd')

        try:
            self.__schema.validate(xml_path)
            self.__xmldoc = xml.etree.ElementTree.parse(xml_path)

        # pylint: disable-msg=bad-continuation
        except (
            xmlschema.XMLSchemaValidationError,
            xml.etree.ElementTree.ParseError,
        ) as error:
            raise ValueError(error)

        # XML is valid, so setid and srclang do exist
        _root = self.__xmldoc.getroot()
        self.__setid = _root.attrib['setid']
        self.__srclang = _root.attrib['srclang']

    @property
    def setid(self):
        """Gets set id for this test set."""
        return self.__setid

    @property
    def srclang(self):
        """Gets srclang for this test set."""
        return self.__srclang

    def __str__(self):
        """Human readable representation."""
        return '{0} ({1})'.format(self.setid, self.srclang)

    def __repr__(self):
        """Machine readable representation."""
        return 'ValidatableTestSet(setid={0!r}, srclang={1!r})'.format(
            self.setid, self.srclang
        )
