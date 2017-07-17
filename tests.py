import os
import sys

# Testing framework libraries
import unittest
import mock

# The main function we want to test
from pytouch.pytouch import main



class TestMainBadArgs(unittest.TestCase):
    """
    Checks the pytouch tool when no extra arguments or too many arguments are passed in.
    """
    @mock.patch.object(sys, 'argv', ['pytouch'])
    def test_not_enough(self):
        """
        Test calling the bare `pytouch` command in the terminal.
        """
        # A ValuError should have been raised
        self.assertRaises(ValueError, main)

    @mock.patch.object(sys, 'argv', ['pytouch', 'filename.json', 'filename2.json'])
    def test_too_many(self):
        """
        Tests calling `pytouch` with filenames specified.
        """
        # A ValuError should have been raised
        self.assertRaises(ValueError, main)
        # The files shouldn't have been created.
        self.assertFalse(os.path.isfile('filename.json'))
        self.assertFalse(os.path.isfile('filename2.json'))

class TestMainGoodArgs(unittest.TestCase):
    """
    Tests calling the pytouch tool with the right number of arguments provided.
    """

    @mock.patch.object(sys, 'argv', ['pytouch', 'filename.json'])
    def test_too_many(self):
        # Call the main function
        main()
        # Check that the file exists
        self.assertTrue(os.path.isfile('filename.json'))

    def tearDown(self):
        # Remove the file
        os.remove('filename.json')
        # Assert that the file no longer exists
        self.assertFalse(os.path.isfile('filename.json'))

if __name__ == '__main__':
    unittest.main()
