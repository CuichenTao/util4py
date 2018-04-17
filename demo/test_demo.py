#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Do something to initiate the test environment here.
        pass

    def tearDown(self):
        # Do something to clear the test environment here.
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
