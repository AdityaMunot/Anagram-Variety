
# Anagram Using Defaultdict function

def anagram_dd(st1, st2):

    dd = defaultdict(int)
    for c in st1:
        dd[c] += 1
    for c in st2:
        if c in dd:
            dd[c] -= 1
        else:
            return False
    
    return not any(dd.value())


class test(unittest.TestCase):
    
    def test_anagram_dd(self):

        self.assertEqual(anagram_dd('hello', 'ollhe'), True)
        self.assertEqual(anagram_dd('pikapika', 'pikapiko'), False)
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
