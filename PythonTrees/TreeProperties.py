class TreeProperties:

    @classmethod
    def listToString(cls, lst): 
        result = ""
        if isinstance(lst, list):
            result += "["
            for item in lst:
                result += cls.listToString(item) + ", "
            result = result.rstrip(", ") + "]"
        else:
            result += str(lst)
        return result
    
    @classmethod
    def countLevels(cls, lst): 
        str = cls.listToString(lst)
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
    def numChildren(cls, lst): 
         str = cls.listToString(lst)
        #find 'node' in list
        for each elemen '''

print("Deepest Level of: ")
print(TreeProperties.listToString(['hotels & travel', ['travel services', ['travel agents']], 'rv parks', 'bed & breakfast', 'hotels', 'airports']))
print(TreeProperties.countLevels(['hotels & travel', ['travel services', ['travel agents']], 'rv parks', 'bed & breakfast', 'hotels', 'airports']))