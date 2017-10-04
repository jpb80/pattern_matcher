#!/usr/bin/env python

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath("../src/pattern_matcher"))

import pattern_matcher

HERE = os.path.abspath(os.path.dirname(__file__))
test_path = "a/b/c"
test_pattern = "a,*,c"

class PatternMatcherTests(unittest.TestCase):

    # @patch("os.path.isfile")
    # @patch("json.load")
    # @patch("__builtin__.open", new_callable=mock_open())
    # def test_process_inventory(self, m, m_json, isfile):
    #     workflow.process_inventory("file.json")
    #     m.assert_called_with("file.json", "r")


    def testParse(self):
        result = pattern_matcher.parse(test_pattern)
        self.assertEqual(result, "a/*/c")
        # sorted_values = [5.0,4.5,3.0,2.5,1.0]
        # result = workflow._min(sorted_values)
        # self.assertEqual(result, 1.0)


suite = unittest.TestLoader().loadTestsFromTestCase(PatternMatcherTests)
unittest.TextTestRunner(verbosity=2).run(suite)
