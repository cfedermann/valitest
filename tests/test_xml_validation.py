"""
valitest: validatable test sets for machine translation
"""
import unittest
import urllib
import xml

from os import getcwd
from os.path import join

import xmlschema

# pylint: disable-msg=no-name-in-module
from context import valitest


class TestXMLValidation(unittest.TestCase):
    """Tests XML validation code."""

    def test_can_import_xmlschema(self):
        """Checks if we can import xmlschema"""
        self.assertEqual(xmlschema.__name__, 'xmlschema')

    def test_can_load_xsd_schema(self):
        """Checks if we can load XSD schema"""
        schema = xmlschema.XMLSchema('valitest.xsd')
        self.assertIsInstance(schema, xmlschema.XMLSchema)

    def test_cannot_load_invalid_file(self):
        """Checks if we raise for invalid file"""
        with self.assertRaises(urllib.error.URLError):
            _ = xmlschema.XMLSchema('does-not-exist.xsd')

    def test_does_not_validate_invalid_files(self):
        """Checks if we raise for invalid SGML file"""
        bad_files = (
            'newstest2019-defr-src-ts.de.sgm',
            'newstest2019-defr-src-ts.de.xml',
        )
        for bad_file in bad_files:
            bad_path = join(getcwd(), 'testdata', bad_file)
            with self.assertRaises(xml.etree.ElementTree.ParseError):
                _ = valitest.ValidatableTestSet(bad_path)

    def test_does_validate_valid_xml_file(self):
        """Checks if we can load valid XML file"""
        xml_file = join(
            getcwd(), 'testdata', 'newstest2019-defr-src-ts.de.FIXED.xml'
        )
        doc = valitest.ValidatableTestSet(xml_file)
        self.assertEqual(doc.setid, "newstest2019")
        self.assertEqual(doc.srclang, "any")


if __name__ == "__main__":
    unittest.main()
