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
        hammingDist = 0
        for i in range(len(canonicalNum1)):
            if canonicalNum1[i] != canonicalNum2[i]:
                hammingDist += 1
        return hammingDist



    def main(self):
        canonicalNum1 = "1110010100"
        canonicalNum2 = "0011110000"
        distance = (self.getHammingDistance(canonicalNum1, canonicalNum2))
        print(distance)
if __name__ == '__main__':
    TreeProperties().main()