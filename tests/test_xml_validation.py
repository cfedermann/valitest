"""
valitest: validatable test sets for machine translation
"""
import unittest


class TestXMLValidation(unittest.TestCase):
    """Tests XML validation code."""
    def test_can_import_xmlschema(self):
        """Checks if we can import xmlschema"""
        import xmlschema
        self.assertEqual(xmlschema.__name__, 'xmlschema')


if __name__ == "__main__":
    unittest.main()
