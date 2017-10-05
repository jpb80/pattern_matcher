#!/usr/bin/env python

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath("../src/pattern_matcher"))

import pattern_matcher

HERE = os.path.abspath(os.path.dirname(__file__))
test_path = "a/b/c"
test_pattern = "a,*,c"
PATH_FLAG = 1
PATTERN_FLAG = 2

class PatternMatcherTests(unittest.TestCase):

    def test_parse(self):
        result = pattern_matcher.parse(test_pattern)
        self.assertEqual(result, "a/*/c")

    def test_process_input_if_path(self):
        pattern_matcher.process_input(test_path, PATH_FLAG)

suite = unittest.TestLoader().loadTestsFromTestCase(PatternMatcherTests)
unittest.TextTestRunner(verbosity=2).run(suite)
