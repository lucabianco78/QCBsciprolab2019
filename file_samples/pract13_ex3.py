import random
import unittest

def sortCSV(mystr):
    tmp = mystr.split(",")
    tmp.sort(reverse=True)
    return ",".join(tmp)



class Testing(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testing, self).__init__(*args, **kwargs)
        #create a random string
        self.alphabet = "abcdefghkjilmnopqrstuvwyz"
        self.data = ""
        #create 15 random strings
        for i in range(15):
            word = ""
            #each of them has a random length up to 20
            j = random.randint(1,20)
            for ind in range(j):
                #pick up to 20 random letters
                t = random.randint(1,len(self.alphabet)-1)
                word += self.alphabet[t]
            if(len(self.data) == 0):
                self.data = word
            else:
                self.data += "," + word


    def test_reslen(self):
        self.assertTrue(len(self.data) == len(sortCSV(self.data)))

    def test_elcount(self):
        res = sortCSV(self.data).split(",")
        self.assertTrue(len(self.data.split(",")) == len(res))

    def test_elsorting(self):
        res = sortCSV(self.data).split(",")
        for ind in range(len(res)-1):
            self.assertTrue(res[ind]> res[ind+1])

    def test_empty(self):
        self.assertEqual(sortCSV(""),"")
    
    def test_onlyOne(self):
        j = random.randint(1,20)
        word = ""
        for ind in range(j):
            #pick up to 20 random letters
            t = random.randint(0,len(self.alphabet)-1)
            word += self.alphabet[t]
        self.assertEqual(sortCSV(word), word)

if __name__ == "__main__":
    mystr = "book,tree,final,example,testing,zed,all,hair,lady,figure,tap,spring,test,fin,tail"
    print("Original:\n{}".format(mystr))
    print("Sorted:\n{}".format(sortCSV(mystr)))
    unittest.main()
