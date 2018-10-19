# implement using only only string and list.

def anagram(st1, st2):

    return sorted(st1) == sorted(st2)

class test(unittest.TestCase):

    def test_anagram(self):

        self.assertTrue(anagram('iceman', 'cinema'))
        self.assertFalse(anagram('pikapika', 'pikapik'), False)
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
