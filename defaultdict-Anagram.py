
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
