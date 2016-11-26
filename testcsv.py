import unittest
import learncsv

class CsvTestCase(unittest.TestCase):
    def setUp(self):
        self.withBlock = [i["Provider"] for i in
                          learncsv.read_valid_universities("uniData.csv", True)]
        self.sansBlock = [i["Provider"] for i in
                          learncsv.read_valid_universities("uniData.csv", False)]

    def test_block(self):
        self.assertNotIn("The Institute of Cancer Research", self.withBlock)
        self.assertIn("The Institute of Cancer Research", self.sansBlock)

unittest.main(exit=False, verbosity=2)

