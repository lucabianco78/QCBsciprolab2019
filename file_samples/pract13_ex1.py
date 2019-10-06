import unittest
import random

#this has problems (test X=[1,1,2,2,3], Y=[4,3])
def myListIntersection2(X,Y):
    tmp = X + Y
    vals = [x for x in tmp if tmp.count(x) == 2]
    return list(set(vals))

##Correct!
def myListIntersection(X,Y):
    inter = [ x for x in X if x in Y]
    print("X", X)
    print("Y", Y)
    print("inter", list(set(inter)))
    return list(set(inter))
    
A = [1, 2, 3, 4, 7, 12]
B = [4, 1, 7, 120]
C = [120, 6]
D = []


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create two test arrays:
        self.x = []
        self.y = []
        for i in range(15):    
            self.x.append(random.randint(0,10))
            self.y.append(random.randint(0,10))
        print("{}\n{}".format(self.x,self.y))
                          
    def test_reslen(self):
        r = myListIntersection(self.x, self.y)
        self.assertFalse(len(r) > len(self.x))
        self.assertFalse(len(r) > len(self.y))
        inter = list(set([a for a in self.x if a in self.y]))
        
        self.assertTrue(len(r) == len(inter))
    
    def test_empty(self):
            self.assertEqual(myListIntersection(self.x, []),[])
            self.assertEqual(myListIntersection([], self.y),[]) 
    
    def test_transitivity(self):
            v = myListIntersection(self.x, self.y).sort()
            v1 = myListIntersection(self.y, self.x).sort()              
            self.assertEqual(v,v1)
    
    def test_doubleEls(self):
        dX = self.x + self.x
        dY = self.y + self.y
        v1 = myListIntersection(dX,dY)
        v1.sort()
        v2 = myListIntersection(self.x,self.y)
        v2.sort()
        self.assertEqual(v1, v2)

if __name__ == "__main__":
    print("A, B: {}".format(myListIntersection(A,B)))
    print("A, C: {}".format(myListIntersection(A,C)))
    print("B, C: {}".format(myListIntersection(B,C)))
    print("A, D: {}".format(myListIntersection(A,D)))   
    #unittest.main()
