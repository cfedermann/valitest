"""
valitest: validatable test sets for machine translation
"""
import unittest
import urllib
import xmlschema


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


if __name__ == "__main__":
    unittest.main()
