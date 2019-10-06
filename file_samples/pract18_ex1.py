"""Implementation of a graph as a (weighted) adjacency matrix"""

class DiGraphAsAdjacencyMatrix:
    def __init__(self):
        #would be better a set, but I need an index
        self.__nodes = list()
        self.__matrix = list()
        
    def __len__(self):
        """gets the number of nodes"""
        return len(self.__nodes)
        
    def nodes(self):
        return self.__nodes
    
    def __str__(self):
        header = "\t".join([n for n in self.__nodes])
        data = ""
        for i in range(0,len(self.__matrix)):
            data += str(self.__nodes[i]) +"\t" + "\t".join([str(x) for x in self.__matrix[i]]) + "\n"

        return "\t"+ header +"\n" + data
    
    def insertNode(self, node):
        #add the node if not there.
        if node not in self.__nodes:
            self.__nodes.append(node)
            #add a row and a column of zeros in the matrix
            if len(self.__matrix) == 0:
                #first node
                self.__matrix = [[0]]
            else:
                N = len(self.__nodes)
                for row in self.__matrix:
                    row.append(0)
                self.__matrix.append([0 for x in range(N)])
    
    def insertEdge(self, node1, node2, weight):
        i = -1
        j = -1
        if node1 in self.__nodes:
            i = self.__nodes.index(node1)
        if node2 in self.__nodes:
            j = self.__nodes.index(node2)
        if i != -1 and j != -1:
            self.__matrix[i][j] = weight
    
    def deleteEdge(self, node1,node2):
        """removing an edge means to set its
        corresponding place in the matrix to 0"""
        i = -1
        j = -1
        if node1 in self.__nodes:
            i = self.__nodes.index(node1)
        if node2 in self.__nodes:
            j = self.__nodes.index(node2)
        if i != -1 and j != -1:
            self.__matrix[i][j] = 0
    
    def deleteNode(self, node):
        """removing a node means removing
        its corresponding row and column in the matrix"""
        i = -1

        if node in self.__nodes:
            i = self.__nodes.index(node)
        print("Removing {} at index {}".format(node, i))
        if node != -1:
            self.__matrix.pop(i)
            for row in self.__matrix:
                row.pop(i)
            self.__nodes.pop(i)
            
    def adjacent(self, node, incoming = True):
        """Your treat! (see exercise 1)"""
        
    def edges(self):
        """Your treat! (see exercise1). Returns all the edges"""
            
if __name__ == "__main__":
    G = DiGraphAsAdjacencyMatrix()
    
    for i in range(6):
        n = "Node_{}".format(i+1)
        G.insertNode(n)

    for i in range(6):
        n = "Node_" + str(i+1)
        six = "Node_6"
        n_plus = "Node_" + str((i+2) % 5)
        if n_plus != "Node_0":
            G.insertEdge(n, n_plus,0.5)
        if i != 5:
            G.insertEdge(n,six,1)
    print(G)
    
    G.insertNode("Node_7")
    G.insertEdge("Node_1", "Node_7", -1)
    G.insertEdge("Node_2", "Node_7", -2)
    G.insertEdge("Node_5", "Node_7", -5)
    G.insertEdge("Node_7", "Node_2", -2)
    G.insertEdge("Node_7", "Node_3", -3)
    
    print("Size is: {}".format(len(G)))
    print("Nodes: {}".format(G.nodes()))
    print("\nMatrix:")
    print(G)
    G.deleteNode("Node_7")
    G.deleteEdge("Node_6", "Node_2")
    #no effect, nodes do not exist!
    G.insertEdge("72", "25",3)
    print(G)
