import unittest
from .extractor import extract_crosslist_from_description

class TestCrosslist(unittest.TestCase):
    def test_isolated_sentence_len3_code(self):
        description = "See ECE 408."
        self.assertEqual(extract_crosslist_from_description(description), ('ECE', '408'))
    def test_full_description_len4_code(self):
        description = "Same as STAT 420. See STAT 420."
        self.assertEqual(extract_crosslist_from_description(description), ('STAT', '420'))
    def test_full_description_len2_code(self):
        description = "Same as CS 473 and MATH 473. See CS 473."
        self.assertEqual(extract_crosslist_from_description(description), ('CS', '473'))
    def test_no_crosslist(self):
        description =  """Parallel programming with emphasis on developing
        applications for processors with many computation cores. 
        Computational thinking, forms of parallelism, programming models, 
        mapping computations to parallel hardware, efficient data structures, 
        paradigms for efficient parallel algorithms, and application case studies.
        Same as CS 483 and CSE 408. 4 undergraduate hours. 4 graduate hours. 
        Prerequisite: ECE 220.""" 
        self.assertIsNone(extract_crosslist_from_description(description))

if __name__ == '__main__': 
    unittest.main()