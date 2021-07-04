import unittest
from util.sentence import split_into_sentences

class TestSentenceSplit(unittest.TestCase):
    def test_restrict_not_intended_len2(self):
        restrict = "Restricted to Graduate - Urbana-Champaign. Not intended for EDD:Ed Pol Org &Ldshp Onl-UIUC."
        self.assertEqual(2, len(split_into_sentences(restrict)))
    def test_restrict_not_intended_len3(self):
        restrict = "Restricted to Computer Science or Bioinformatics major(s). Restricted to Graduate - Urbana-Champaign. Not intended for MCS:Computer Sci Online -UIUC, MCS:Computer Sci Online -UIUC, or NDEG:Computer Science Onl-UIUC."
        self.assertEqual(3, len(split_into_sentences(restrict)))
    def test_restrict_not_intended_len2_2(self):
        restrict = "Restricted to Graduate - Urbana-Champaign. Restricted to MSW:Social Work -UIUC."
        self.assertEqual(2, len(split_into_sentences(restrict)))
    def test_restrict_not_intended_len4(self):
        restrict = "Restricted to Gies College of Business. Restricted to Finance major(s). Restricted to students with Junior or Senior class standing. Restricted to Undergrad - Urbana-Champaign."
        self.assertEqual(4, len(split_into_sentences(restrict)))

if __name__ == '__main__':
    unittest.main()