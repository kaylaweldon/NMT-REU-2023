from Node import Node

class TreeProperties:

    @classmethod
    def listToString(self, lst): 
        result = ""
        if isinstance(lst, list):
            result += "["
            for item in lst:
                result += self.listToString(item) + ", "
            result = result.rstrip(", ") + "]"
        else:
            result += str(lst)
        return result
    
    @classmethod
    def countLevels(self, lst): 
        str = self.listToString(lst)
        count = 0
        deepestLvl = 0
        for element in str:
            if element == '[':
                count += 1
                if count > deepestLvl:
                    deepestLvl = count
            elif element == ']':
                count -= 1
        return deepestLvl

    '''@classmethod
    def numChildren(self, lst): 
         str = self.listToString(lst)
        #find 'node' in list
        for each elemen '''
    
    def getHammingDistance(self, canonicalNum1, canonicalNum2):
       # if len(canonicalNum1 != canonicalNum2):
            
        hammingDist = 0
        for i in range(len(canonicalNum1)):
            if canonicalNum1[i] != canonicalNum2[i]:
                hammingDist += 1
        return hammingDist

    def matchTree(self, node1, node2): 
        if len(node1.children) != len(node2.children):
            return False
        for i in range(len(node1.children)):
            if not self.matchTree(node1.children[i], node2.children[i]):
                return False
        return True
    
    def isSubtree(self, t1, t2):
        if t1 is None or t2 is None:
            return False
        
        if self.matchTree(t1, t2):
            return True

        for child in t1.children:
            if self.isSubtree(child, t2):
                return True

        return False    


    def main(self):
        """canonicalNum1 = "1110010100"
        canonicalNum2 = "0011110000"
        distance = (self.getHammingDistance(canonicalNum1, canonicalNum2))
        print(distance)"""

        t1Root = Node("1")
        t2Root = Node("2")

        child1 = Node("3")
        child2 = Node("4")
        child3 = Node("5")
        child4 = Node("6")
        child5 = Node("7")
        child6 = Node("8")
        child7 = Node("9")
        child8 = Node("10")

        t1Root.add_child(child1)
        t1Root.add_child(child2)
        t1Root.add_child(child3)
        child1.add_child(child4)
        t2Root.add_child(child5)
        t2Root.add_child(child6)
        child5.add_child(child8)




        print(self.isSubtree(t1Root, t2Root)) 
            
if __name__ == '__main__':
    TreeProperties().main()