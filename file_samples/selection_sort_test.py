import random
import time
import unittest

class SelectionSort:
    def __init__(self,data, verbose = True):
        self.__data = data
        self.__comparisons = 0
        self.__swaps = 0
        self.__verbose = verbose
        self.__time = 0
        
    def getData(self):
        return self.__data
    
    def getTime(self):
        return self.__time
    
    def getComparisons(self):
        return self.__comparisons
    
    def getSwaps(self):
        return self.__swaps
    
    def swap(self, i, j):
        """
        swaps elements i and j in data.
        """
        if(i != j): #no point in swapping if i==j
            tmp = self.__data[i]
            self.__data[i] = self.__data[j]
            self.__data[j] = tmp
        
    def argmin(self, i):
        """
        returns the index of the smallest element of
        self.__data[i:]
        """
        mpos = i
        N = len(self.__data)
        minV = self.__data[mpos]
        for j in range(i + 1,N): # from i+1 to N. U[i+1:]
            if(self.__data[j] < minV):
                mpos = j
                minV = self.__data[j]
            #just for checking
            self.__comparisons += 1
        
        return mpos
    
    def sort(self):
        self.__comparisons = 0
        self.__swaps = 1
        if self.__verbose:
            print("Initial list:")
            print(self.__data)
            print("\n")
            
        #to check performance    
        start_t = time.time()
        for i in range(len(self.__data) - 1):
                j = self.argmin(i)
                self.swap(i,j) 
                self.__swaps += 1
                if self.__verbose:
                    print("It. {}. data[{}]<->data[{}] {}<->{}".format(i,
                                                                       i,
                                                                       j,
                                                                       self.__data[i],
                                                                       self.__data[j]))
                    print(self.__data)    
        end_t = time.time()
        
        self.__time = end_t - start_t
        
        if self.__verbose:
            print(self.__data)
            print("\nNumber of comparisons: {}".format(self.__comparisons))
            print("Number of swaps: {}".format(self.__swaps))
            print("In {:.4f}s".format(self.__time))



if __name__ == "__main__":
    unittest.main()


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create a test list:
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = SelectionSort(x, verbose = False)
                          
    def test_swap1(self):
        """swap of swap is identical to beginning"""
        #let's copy data
        dcopy = self.sorter.getData()[:]
        for i in range(40):
            i1 = random.randint(0,len(dcopy) - 1)
            i2 = random.randint(0,len(dcopy) - 1)
            self.sorter.swap(i1,i2)
            self.sorter.swap(i1,i2)
            self.assertTrue(self.sorter.getData() == dcopy)
    def test_swap2(self):
        """length of swapped data does not change"""
        
        l = len(self.sorter.getData())
        for i in range(40):
            i1 = random.randint(0,l - 1)
            i2 = random.randint(0,l - 1)
            self.sorter.swap(i1,i2)
            self.assertTrue(len(self.sorter.getData()) == l)
        
    def test_swap3(self):
        """swapping only changes i and j indexes (if i!=j)"""
        #let's copy data
        dcopy = self.sorter.getData()[:]
        for i in range(40):
            #let's copy data
            dcopy = self.sorter.getData()[:]
            i1 = random.randint(0,len(dcopy) - 1)
            i2 = random.randint(0,len(dcopy) - 1)
            if i1 != i2:
                self.sorter.swap(i1,i2)
                for ind in range(0,len(dcopy)):
                    if ind != i1 and ind != i2:
                        self.assertTrue(dcopy[ind] == self.sorter.getData()[ind])
    
    def test_argmin(self):
        """
        tests if j=argmin(i) then j <= data[i:]
        """
        l = len(self.sorter.getData())
        for i in range(40):
            ind = random.randint(0,l - 1)
            minP = self.sorter.argmin(ind)
            for j in self.sorter.getData()[ind:]:
                self.assertTrue(self.sorter.getData()[minP] <= j)
                
    def test_sort(self):
        """tests if the sort works"""
        self.sorter.sort()
        d = self.sorter.getData()
        for el in range(0,len(d) - 2):
            self.assertTrue(d[el] <= d[el+1])
    
    def test_empty(self):
            """sorting of empty list is empty"""
            self.assertEqual(SelectionSort([]).getData(),[])
