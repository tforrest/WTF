import wtf
import argparse
import unittest

class WtfTest(unittest.TestCase):

    def setUp(self):
        self.parser = wtf.create_parser()
     
    def test_args(self):
        parsed = self.parser.parse_args(["thisisaterm", "123"])
        prosessed = wtf.process_args(parsed.term)
        self.assertEqual(prosessed,"thisisaterm 123")
