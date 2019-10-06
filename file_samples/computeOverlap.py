import math

def score(a,b):
    mat = {}
    mat["A"] = {"A" : 0, "C" : 4, "G" : 2, "T" : 4, "-" : 8}
    mat["C"] = {"A" : 4, "C" : 0, "G" : 4, "T" : 2, "-" : 8}
    mat["G"] = {"A" : 2, "C" : 4, "G" : 0, "T" : 4, "-" : 8}
    mat["T"] = {"A" : 4, "C" : 2, "G" : 4, "T" : 0, "-" : 8}
    mat["-"] = {"A" : 8, "C" : 8, "G" : 8, "T" : 8, "-" : 8}
    
    return mat[a][b]
    
    
def computeMatrix(X,Y, minLen = 0):
    # + 1 is for leading "-"
    x_len = len(X) + 1
    y_len = len(Y) + 1
    print(X)
    print(Y)
    A = []
    #initialize first column to 0 and first row to infinite
    
    for i in range(x_len - minLen + 1):
        A.append([0])
    for i in range(minLen -1):
        A.append([math.inf])
    for i in range(y_len -1 ):
        A[0].append(math.inf)
    
    for i in range(1,x_len):
        for j in range(1,y_len):
            c1 = A[i-1][j] + score(X[i-1], "-")
            c2 = A[i][j-1] + score("-", Y[j-1])
            c3 = A[i-1][j-1] + score(X[i-1],Y[j-1])
            #print("i,j: {},{}".format(i,j))
            A[i].append(min([c1,c2,c3]))
    if minLen != 0:
        for i in range(0,minLen):
            A[-1][i] = math.inf
    return A
    
def plotMatrix(Mat, X,Y):
    X = "-" + X
    outStr = "\t-" +"\t"+ "\t".join(list(Y))

    for i in range(len(X)):
        outStr+="\n" + X[i] +"\t"+ "\t".join([str(x) for x in Mat[i]])
    print(outStr)
    
    
X = "CTCGGCCCTAGG"
Y = "GGCTCTAGGCCC"

A = computeMatrix(X,Y,minLen = 5)

print("The overlap matrix:")
plotMatrix(A,X,Y)
print("\n")
X1 = "AATATACATAC"
Y1 = "TACGTACTTA"
B = computeMatrix(X1,Y1, minLen = 4)
print("The overlap matrix:")
plotMatrix(B,X1,Y1)
#X2 = "ATCGGTTCGGTGAAGTAA"
#Y2 = "CGGTGACGTTACCATATCCAG"
#C = computeMatrix(X2,Y2, minLen = 4)
#print("The overlap matrix:")
#plotMatrix(C,X2,Y2)
print("\n")
X3 = "ACACGGATT"
Y3 = "CGGTATT"
D = computeMatrix(X3,Y3, minLen = 3)
print("The overlap matrix:")
plotMatrix(D,X3,Y3)
#x1 = "GTCAGTCAATCTACTCGGAAACTATACACCG"
#y1 = "CTATTTCCGTAACACGGATT"
#B = computeMatrix(x1,y1, minLen = 3)
#print("The overlap matrix:")
#plotMatrix(B,x1,y1)