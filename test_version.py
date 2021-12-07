import unittest

from app.version_tool import get_newer_version


class TestGetLatestVersion(unittest.TestCase):
    """The class is used to test a function that returns a newer version """
    
    def test_different_versions(self):
        """ Test of different versions, having letters(1) and only numbers(2) """
        version_returned = get_newer_version("1.0.1-beta.1", "1.0.0")
        version_to_expect = "1.0.1-beta.1"
        self.assertEqual(version_returned, version_to_expect)

    def test_different_number_versions(self):
        """ Test of different versions, having numbers """
        version_returned = get_newer_version("3.1.1", "3.1.3")
        version_to_expect = "3.1.3"
        self.assertEqual(version_returned, version_to_expect)

    def test_equal_versions(self):
        """ Test of equal versions, having letters """
        version_returned = get_newer_version("v2.67-rc", "2.67rc")
        version_to_expect = "v2.67-rc"
        self.assertEqual(version_returned, version_to_expect)

    def test_reverse_equal_versions(self):
        """ Test of equal versions, having letters in other order"""
        version_returned = get_newer_version("2.67rc", "v2.67-rc")
        version_to_expect = "2.67rc"
        self.assertEqual(version_returned, version_to_expect)

    def test_almost_equal_different_versions(self):
        """ Test of almost equal versions, having letters """
        version_returned = get_newer_version("2.67rc", "2.67rc1")
        version_to_expect = "2.67rc1"
        self.assertEqual(version_returned, version_to_expect)

    def test_almost_different_versions(self):
        """ Test of different versions, having 'dev' """
        version_returned = get_newer_version("1.0b1", "1.ob1.dev456")
        version_to_expect = "1.0b1"
        self.assertEqual(version_returned, version_to_expect)

if __name__ == '__main__':
    unittest.main()
