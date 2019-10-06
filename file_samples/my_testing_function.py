"""
In file my_testing_function.py
"""

import unittest
import random

def getFirstNprimes(N):
    '''
    This function should output the first N prime numbers.
     '''
    if N <= 0:
        return []
    res = [2]
    current = 3
    while len(res) < N:
        if len([x for x in res if current % x == 0]) == 0:
            res.append(current)
        current += 1
    #uncomment next line to introduce a bug
    #res.append(1)
    #or a more subtle error:
    ind = random.randint(0,len(res)-1)
    res[ind] = 10
    
    return res        

class Testing(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(getFirstNprimes(0),[])
    
    def test_one(self):
        self.assertEqual(getFirstNprimes(1),[2])
    
    def test_ten(self):
        self.assertEqual(getFirstNprimes(10),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    def test_len(self):
        for i in range(0,10):
            n = random.randint(1,1000)
            self.assertFalse(len(getFirstNprimes(n)) != n)
    
    
    def test_negative(self):
        self.assertTrue(len(getFirstNprimes(-1)) == 0)

if __name__ == "__main__":
#    unittest.main()
    print(getFirstNprimes(20))
