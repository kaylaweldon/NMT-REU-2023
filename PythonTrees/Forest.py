from collections import deque

complexityCounter = 0

class Forest:

    from RandomTreeGenerator import RandomTreeGenerator

    # the list containing trees of the forest
    forest = []

    # the list containing edit distances and LUBTs between each tree in the forest
    forestEditDistanceMatrix = []

    # dictionary for keeping track of Least upper bounds found
    # we store trees as their canonical numbers so isomorphic trees can be found
    LUBdictionary = []

    def __get_forest__(self):
        return self.forest
    
    def setForest(self, userForest):
        self.forest = userForest
    
    def build_forest_from_matrix_of_matches(self, matrixOfMatches):
        
        anonymized_forest = []

        for pairIndex in range(0, len(matrixOfMatches)):

            anonymized_forest.append(matrixOfMatches[pairIndex][2][0])
            anonymized_forest.append(matrixOfMatches[pairIndex][2][0])

        return anonymized_forest
    
    # brute force method to find the absolute best combination so forest has 2-anonymity
    # returns the return from anonymize_forest_brute_force_recursion
    # this is the method that the user should call, so they don't need to 
    # pass in a matrix of matches
    def anonymize_forest_brute_force(self):

        self.gather_edit_distances_for_forest()

        editDistanceMatrix = self.forestEditDistanceMatrix
        

        return self.anonymize_forest_brute_force_recursion(editDistanceMatrix, complexityCounter)

    # return: [anonymized forest, total edit distance]
    def anonymize_forest_brute_force_recursion(self, editDistanceMatrix):
        
        """
        print("edit distance matrix that was recieved in this matrix: ")
        for child in editDistanceMatrix:
            print(child)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        """

        combination_options = []

        anonymized_forest = []

        # base case
        # if the matrix is 1 x 1
        if len(editDistanceMatrix) == 1:

            """
            print("base case reached. returning: ")
            print([[editDistanceMatrix[0][1][1][0], editDistanceMatrix[0][1][1][0]], editDistanceMatrix[0][1][1][1]])
            """

            # you must duplicate the last element
            return [[editDistanceMatrix[0][1][1][0], editDistanceMatrix[0][1][1][0]], editDistanceMatrix[0][1][1][1]]

        # for each pairing for the first tree
        for optionIndexChosen in range(1, len(editDistanceMatrix[0])):

            """print("this is the pairing for the first tree we are appending to the combination options: ")
            print([editDistanceMatrix[0][optionIndexChosen][1]])
            print("________________________________________")"""

            # append the LUBT and edit distance associated with that pairing to a new
            # option in the combination matrix
            combination_options.append([editDistanceMatrix[0][optionIndexChosen][1]])

            # let's you know how many copies of this LUBT to create at the end, in case other trees can be joined in
            # the default is 2
            numberOfCopies = 2

            #initialize an altered EditDistanceMatrix
            alteredEditDistanceMatrix = []

            # for all other trees *except* if it was chosen to be matched with the first tree!
            for otherTreeIndex in range(1, len(editDistanceMatrix)):

                if otherTreeIndex + 1 == optionIndexChosen:
                    continue

                """
                treeAtOtherTreeIndex = editDistanceMatrix[otherTreeIndex][0]
                LUBTofFirstTreeAndMatch =  editDistanceMatrix[0][optionIndexChosen][1][0]
                LUBTandED = self.leastUpperBound(editDistanceMatrix[otherTreeIndex][0], editDistanceMatrix[0][optionIndexChosen][1][0])
                """

                # this is the case where a tree would already be matched with the LUBT of the first tree and its pair
                # we do not want to add it to the editDistanceMatrix anymore so we continue
                """if self.leastUpperBound(editDistanceMatrix[otherTreeIndex][0], editDistanceMatrix[0][optionIndexChosen][1][0])[1] == 0:

                    numberOfCopies += 1
                    continue
                """
                # append the tree to a list in the altered matrix
                alteredEditDistanceMatrix.append([editDistanceMatrix[otherTreeIndex][0]])

                # for each pairing associated with that tree
                # beginning at 2 to skip the first tree which we are pairing with above
                for pairingOptionIndex in range(2, len(editDistanceMatrix[otherTreeIndex])):
                    
                    # skip the pairing option already chosen for the first tree
                    if pairingOptionIndex == optionIndexChosen:
                        continue
                    
                    # add the pairing option to the tree's list in the altered edit distance matrix
                    pairingOption = editDistanceMatrix[otherTreeIndex][pairingOptionIndex]

                    alteredEditDistanceMatrix[len(alteredEditDistanceMatrix) - 1].append(pairingOption)
                
            """
            print("alteredEditdistanceMatrix to send : ")
            for child in alteredEditDistanceMatrix:
                print(child)
            print("+++++++++++++++++++++++++")"""

            # this is the recursive step
            if len(alteredEditDistanceMatrix) > 0:

                optimalAlteredPairings = self.anonymize_forest_brute_force_recursion(alteredEditDistanceMatrix)
                

                """
                print("optimal result of the alternative matrix: ")
                print(optimalAlteredPairings)
                """

                # append to the combination associated with chosing a particular pairing for the first tree
                combination_options[len(combination_options) - 1].append(optimalAlteredPairings)

                """
                print("combination options after appending: ")
                for option in combination_options:
                    print(option)
                print("==============================")"""

            # else, the two last things were paired with one another
            # this means there will be a combination option which is of length one, and we need to
            # watch out for this. 

        # find the best option

        # choose the first to compare with the rest
        bestOption = combination_options[0]

        # edit distance of the choice of the first tree plus the total edit distance for the rest of the matrix
        # which is stored at [0][1][1]
        bestEditDistance = bestOption[0][1]

        if len(bestOption) > 1:
            bestEditDistance += bestOption[1][1]
        
        for optionIndex in range(1, len(combination_options)):
            
            # get the total edit distance for that option
            optionEditDistance = combination_options[optionIndex][0][1]

            if len(combination_options[optionIndex]) > 1:
                optionEditDistance += combination_options[optionIndex][1][1]

            # if it is smaller than the best one so far, replace
            if optionEditDistance < bestEditDistance:

                bestOption = combination_options[optionIndex]
                bestEditDistance = optionEditDistance
        """
        print("best option: ")
        print(bestOption)
        print("****************************************")"""

        for copy in range(0, numberOfCopies):

            anonymized_forest.append(bestOption[0][0])


        if len(bestOption) > 1:

            for tree in bestOption[1][0]:

                anonymized_forest.append(tree)
        """
        print("anonymized forest to return: ")
        print(anonymized_forest)
        print("###############################")

        print("end of method reached. returning: ")
        print([anonymized_forest, bestEditDistance])
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")"""

        """print("complexity Counter: ")
        print(complexityCounter)"""

        return [anonymized_forest, bestEditDistance] 

    """
    return: [anonymized forest, total edit distance]
    """

    def updateComplexity(self, value):
        global complexityCounter
        complexityCounter += value

    def getComplexity(self):
        return complexityCounter

    def anonymize_forest_greedy(self):


        self.gather_edit_distances_for_forest()

        editDistanceMatrix = self.forestEditDistanceMatrix

        indicesOfTakenTrees = []
        matrixOfMatches = []

        # to print out which tree was matched with which in the end if you want
        treesMatched = []

        for treeIndex in range(0, len(editDistanceMatrix)):
            self.updateComplexity(1)
            # if it has already been paired, continue
            if treeIndex in indicesOfTakenTrees:
                continue
            
            matchIndexToBeginComparison = 1

            while matchIndexToBeginComparison - 1 in indicesOfTakenTrees:
                matchIndexToBeginComparison += 1

            # this is where the edit distance for the first match is stored 
            leastEditDistanceForTree = editDistanceMatrix[treeIndex][matchIndexToBeginComparison][1][1]
            indexFound = matchIndexToBeginComparison
            self.updateComplexity(1)

            # for each pairing available for that tree
            for matchIndex in range(matchIndexToBeginComparison, len(editDistanceMatrix[treeIndex])):

                self.updateComplexity(1)
                # if it has already been paired, continue
                if matchIndex - 1 in indicesOfTakenTrees:
                    continue
                
                if editDistanceMatrix[treeIndex][matchIndex][1][1] < leastEditDistanceForTree:

                    leastEditDistanceForTree = editDistanceMatrix[treeIndex][matchIndex][1][1]
                    indexFound = matchIndex
                    self.updateComplexity(1)
                    
            indicesOfTakenTrees.append(indexFound - 1)
            
            
            matchToAppend = [editDistanceMatrix[treeIndex][0], 
                             editDistanceMatrix[treeIndex][indexFound][0],
                               editDistanceMatrix[treeIndex][indexFound][1]]
            
            matrixOfMatches.append(matchToAppend)
            indicesOfTakenTrees.append(treeIndex)
            treesMatched.append([treeIndex, indexFound - 1])

        totalEditDistance = 0

        for pair in matrixOfMatches:

            totalEditDistance += pair[2][1]
            self.updateComplexity(1)
        # matrixOfMatches.append(totalEditDistance)

    
        return [self.build_forest_from_matrix_of_matches(matrixOfMatches), totalEditDistance, treesMatched]
    
    # given a forest, calculate the edit distance and LUBT for every possible 
    # pair of trees within the forest 
    # puts them in a global structure called forestEditDistanceMatrix
    #
    def gather_edit_distances_for_forest(self):

        # conjecture that sorting high to low will yield better results than low to high
        sorted_forest = self.sort_by_number_of_nodes_high_to_low(self.forest)

        self.forestEditDistanceMatrix = []

        for tree in range(0, len(sorted_forest)):

            self.forestEditDistanceMatrix.append([sorted_forest[tree]])

            for match in range(0, len(self.forest)):
                
                self.forestEditDistanceMatrix[tree].append([sorted_forest[match]])

                # this represents the trees matching with themselves along the diagonal
                # instead of filling it in with a zero, we are going to use it to represent 
                # the case where we choose to duplicate the tree and therefore need to 
                # create a tree of equal number of nodes, where the LUBT is equal to the tree itself
                if match == tree:

                    LUBTandEditDistance = [sorted_forest[match], self.number_of_nodes(sorted_forest[match])]
                
                # otherwise we just find the edit distance and LUBT of the two different trees
                else:

                    LUBTandEditDistance = self.leastUpperBound(sorted_forest[tree], sorted_forest[match])

                self.forestEditDistanceMatrix[tree][match + 1].append(LUBTandEditDistance)

        return self.forestEditDistanceMatrix
    
    """
    generates a random forest
    """
    def generate_forest(self, number_of_trees, max_levels, max_fan):

        # initialize a random tree generator
        RandomTreeGenerator = self.RandomTreeGenerator()

        # for each tree to generate
        for i in range(0, number_of_trees):

            # generate a tree of max levels 
            random_tree = RandomTreeGenerator.generate(max_levels, max_fan)

            # add that tree to the forest
            self.forest.append(random_tree)

    """
    return: [leastUpperBoundTree, editDistance]
    """
    def leastUpperBound(self, T1, T2):

        # base case: if either T1 or T2 consists of a single node
        if len(T1) == 1 or len(T2) == 1:

            T1nodes = self.number_of_nodes(T1)
            T2nodes = self.number_of_nodes(T2)
            self.updateComplexity(1)

            # edit distance is the difference in their nodes
            editDistance = abs(T1nodes - T2nodes)
            
            # return the bigger tree, or T2 if they are equal
            if T1nodes > T2nodes:
                self.updateComplexity(1)
                leastUpperBoundTree = T1

            if T1nodes == T2nodes:
                self.updateComplexity(1)
                leastUpperBoundTree = T2
            
            if T1nodes < T2nodes:
                self.updateComplexity(1)
                leastUpperBoundTree = T2

            return [leastUpperBoundTree, editDistance]
        
        # very important but complicated structure to store subresults
        distancesAndTrees = []

        # gather edit distance info for each pairing
        # for each child of the root of T1 
        # the range begins at 1 in order to skip the root
        for childT1 in range(1, len(T1)):
            
            # append an empty list to hold the results of each 
            # matching with childT1 and a child of T2

            # begin by appending the distancesAndTrees with a list 
            # beginning with the child of T1
            distancesAndTrees.append([T1[childT1]])
            self.updateComplexity(1)

            # for each child of the root of T2
            for childT2 in range(1, len(T2)):

                # consult dictionary to see if trees isomorphic to childT1 and childT2 have
                # already been evaluated
                dictionaryPairingResult = self.search_Dictionary(T1[childT1], T2[childT2])

                # if there was an entry in the dictionary, return the entry
                if dictionaryPairingResult != None:

                    dictionPairingResultToSend = [dictionaryPairingResult[0], dictionaryPairingResult[1], T2[childT2]]

                    # print("dictionPairingResultToSend: ")
                    # print(dictionPairingResultToSend)

                    distancesAndTrees[len(distancesAndTrees) - 1].append(dictionPairingResultToSend)
                    self.updateComplexity(1)

                # otherwise we must find the answer ourselves
                # this is the recursive step
                else:

                    pairingResult = self.leastUpperBound(T1[childT1], T2[childT2])

                    self.add_Dictionary(T1[childT1], T2[childT2], pairingResult)

                    # wrap the LUBT in ssome necessary brackets and send child information 
                    # incase the child needs to be duplicated
                    pairingResultToSend = [pairingResult[0], pairingResult[1], T2[childT2]]

                    # append the result to the list of results found for tree one
                    distancesAndTrees[len(distancesAndTrees) - 1].append(pairingResultToSend)
                    self.updateComplexity(1)
        """
        now that we've calculated all the pairs LUBT and edit distances we have to find the 
        best combination, i.e. how we should match children of T1 with children of T2 such that 
        the sum of edit distances is minimized
        we have another method that will find this optimal combination called optimal_pairing
        """

        optimalPairingAndEditDistance = self.optimal_pairing(distancesAndTrees)
        self.updateComplexity(1)

         
        # we want to use the above result to contruct a tree out of the LUBTs that it returns
        # along with any leftovers   
        # placeholder joining parent called 'x'
        finalLUBT = ['x']
        self.updateComplexity(1)


        # the first item in optimalPairingAndEditDistance is a list of all the LUBTs that should be appended a root
        for LUBT in optimalPairingAndEditDistance[0]:

            finalLUBT.append(LUBT)
            self.updateComplexity(1)
        finalEditDistance = optimalPairingAndEditDistance[1]

        return [finalLUBT, finalEditDistance]

    # necessary helper method for leastUpperBound method
    def deal_with_leftovers(self, distancesAndTrees):

        potential_main_match_indices = []
                
        leftovers = []

        # find the least edit distance
        leastEditDistance = distancesAndTrees[0][1][1]

        # compare it to the rest
        for matchIndex in range(2, len(distancesAndTrees[0])):

            # if it is smaller 
            if distancesAndTrees[0][matchIndex][1] < leastEditDistance:
                
                # make the new least edit distance
                leastEditDistance = distancesAndTrees[0][matchIndex][1]

        # find all indices which have the least edit distance, because there can be more than one
        # in which case we still need to find which one is the best
        for matchIndex in range(1, len(distancesAndTrees[0])):

            # if it is a candidate for main match subtree
            if distancesAndTrees[0][matchIndex][1] == leastEditDistance:

                potential_main_match_indices.append(matchIndex)
        
        # now that we have all of the indices of the potential main matches, we test to see which one, if picked, would 
        # have the least expensive edit distance combination

        # pick the first one to compare against the others
        best_match_index = potential_main_match_indices[0]
        least_total_edit_distance = distancesAndTrees[0][best_match_index][1]

        for matchIndex in range(1, len(distancesAndTrees[0])):

            if matchIndex == best_match_index:
                continue

            least_total_edit_distance += self.number_of_nodes(distancesAndTrees[0][matchIndex][2])
        
        # now we compare this to if we had picked any other candidate in match candidates
        for potential_match_index in potential_main_match_indices:

            editDistanceForMatch = distancesAndTrees[0][potential_match_index][1]

            for matchIndex in range(1, len(distancesAndTrees[0])):

                if matchIndex == potential_match_index:
                    continue

                editDistanceForMatch += self.number_of_nodes(distancesAndTrees[0][matchIndex][2])
            
            if editDistanceForMatch < least_total_edit_distance:

                least_total_edit_distance = editDistanceForMatch
                best_match_index = potential_match_index

        # now we have to add the total edit distance, which must include the number of nodes of the 
        # leftovers as they will have to be completely duplicated
        bestLUBT = distancesAndTrees[0][best_match_index][0]
        LUBTlistToReturn = [bestLUBT]

        for treeIndex in range(1, len(distancesAndTrees[0])):

            if treeIndex == best_match_index:
                continue
            
            else:
                LUBTlistToReturn.append(distancesAndTrees[0][treeIndex][2])

        return [LUBTlistToReturn, least_total_edit_distance]

    """
    With optimal_pairing method, we are given a matrix of editDistances and LUBTs for every possible pairing
    of children of T1 and children of T2. We want to find the combination of discrete pairings such that
    the sum their editDistances is minimized

    We use a simple brute force approach, checking every possible combination of discrete pairings and keeping track
    of each edit distance sum. We store the result of each combination in a data structure. Finally we search
    that data structure for the combination with the least edit distance

    @parameters: distancesAndTrees, a list of lists of lists of... editDistances and LUBTs
    @return: [list of LUBTs, editDistance, list of leftovers]
    """
    def optimal_pairing(self, distancesAndTrees):

        # initialize a list of leftovers to keep track of
        leftovers = []

        # if the length of the first child is zero, that means the options have been run out of
        if len(distancesAndTrees[0]) == 1:

                # that child itself must be constructed but there are no other leftovers
                # the edit distace is the number of nodes contained in child
                childrenToReturn = []
                editDistance = 0

                for child in distancesAndTrees:

                    childrenToReturn.append(child[0])
                    editDistance += self.number_of_nodes(child)
                    self.updateComplexity(1)
                    

                return [childrenToReturn, editDistance]

        # base case
        # if the matrix contains only one child of T1
        if len(distancesAndTrees) == 1:

            # if that child has no matches listed:
            if len(distancesAndTrees[0]) == 1:

                # that child itself must be constructed but there are no other leftovers
                # the edit distace is the number of nodes contained in child
                self.updateComplexity(1)
                return [[distancesAndTrees[0]], self.number_of_nodes(distancesAndTrees[0])]
        
            # if that child has exactly one match listed:
            if len(distancesAndTrees[0]) == 2:
                
                # return that match, which contains the information [LUBT(child, match), d(child, match)]
                # as well as the leftovers, which are empty
                self.updateComplexity(1)
                return [[distancesAndTrees[0][1][0]], distancesAndTrees[0][1][1]]
            
            # else that child has more than one match listed:
            # this is a special case where leftovers must be accounted for
            # it's a long and complicated case that we wrote another method for
            if len(distancesAndTrees[0]) > 2:
                self.updateComplexity(1)
                return self.deal_with_leftovers(distancesAndTrees)
        
        # other wise if it is not a base case
        # we first initialize a data structure to store information about every possible combination of matches
        combinationOptions = []
        
        # FIRST CHILD/SUBTREE REPLICATE OPTION
        # account for the case where the first child is chosen to be replicated

        # add new list (i.e. option) to combination options
        combinationOptions.append([])

        # to that option, append (within a list) the first subtree in distancesAndTrees 
        combinationOptions[len(combinationOptions) - 1].append([[distancesAndTrees[0][0]]])

        # also append its edit distance with itself, i.e. its number of nodes
        combinationOptions[len(combinationOptions) - 1][0].append(self.number_of_nodes(distancesAndTrees[0][0]))

        #
        combinationOptions[len(combinationOptions) - 1][0].append([distancesAndTrees[0][0]])
        
        # initialize an altered matrix
        alteredMatrix = []

        for child in range(1, len(distancesAndTrees)):
            self.updateComplexity(1)
            alteredMatrix.append(distancesAndTrees[child])     

        # this is  recursive step
        alteredMatrixBestOption = self.optimal_pairing(alteredMatrix)

        combinationOptions[len(combinationOptions) - 1].append(alteredMatrixBestOption)
    
        # for each match of the first child in the matrix (distancesAndTrees)
        for match in range(1, len(distancesAndTrees[0])):
            self.updateComplexity(1)
            # construct a new option and append the match, 
            # which again is a list and looks like match = [LUBT(child, match), d(child, match)]
            combinationOptions.append([])
            combinationOptions[len(combinationOptions) - 1].append([[distancesAndTrees[0][match][0]]])
            combinationOptions[len(combinationOptions) - 1][0].append(distancesAndTrees[0][match][1])

            # now we costruct an altered matrix without the first child and with out any of the other
            # children being able to match with the chosen match, and evaluate their best combination
            # recursively
            alteredMatrix = []

            # starting from 1 so as to skip the first child
            for child in range(1, len(distancesAndTrees)):
                self.updateComplexity(1)
                alteredMatrix.append([])
                
                # starting from range zero so as to include the original subtree associated with the child
                for alteredMatches in range(0, len(distancesAndTrees[child])):
                    self.updateComplexity(1)
                    # if we've reached the chosen column with is taken by the match for the first child, we skip it 
                    if alteredMatches == match:
                        continue
                    
                    # otherwise we append to our altered matrix
                    alteredMatrix[len(alteredMatrix) - 1].append(distancesAndTrees[child][alteredMatches])

            # now that we have constructed our altered matrix, we find its best option
            # this is the recursive step
            # it is of the form [bestLUBT, totalEditDistance, leftovers]
            alteredMatrixBestOption = self.optimal_pairing(alteredMatrix)

            combinationOptions[len(combinationOptions) - 1].append(alteredMatrixBestOption)

        # finally sum up the edit distances of each of the options
        # assume the first one is the best and compare it to the rest
        bestOption = combinationOptions[0]
        bestEditDistance = 0
        # we have to add up the editDistances for the first one to have a comparable editDistance
        for match in combinationOptions[0]:
            self.updateComplexity(1)
            # this is where the editDistance is located in the match
            bestEditDistance += match[1]

        # now we search the options to find the least editDistance
        for option in combinationOptions:
            self.updateComplexity(1)
            # initialize a variable to keep track of the total editDistance needed for this option
            optionEditDistance = 0

            # skip the first option because we already calculated it
            if option == combinationOptions[0]:
                continue
            
            # add up every editDistance in the matches of the option
            for match in option:

                optionEditDistance += match[1]

            # if this option is better than the best so far, update the best!
            if optionEditDistance < bestEditDistance:
                
                bestEditDistance = optionEditDistance
                bestOption = option
    
        bestChildrenToJoin = []

        for match in bestOption:

                for LUBT in match[0]:
                    self.updateComplexity(1)
                    bestChildrenToJoin.append(LUBT)
        
        # now we have the best combination, and its edit distance! we finally return

        return [bestChildrenToJoin, bestEditDistance]
    
    # searches for whether the LUB of two trees has already been found
    def search_Dictionary(self, T1, T2):

        canonT1 = self.canonize_tree(T1)
        canonT2 = self.canonize_tree(T2)

        for entry in self.LUBdictionary:

            if entry[0] == canonT1:
    
                for match in entry:

                    if match[0] == entry[0]:
                        continue
                    if match[0] == canonT2:
                        return match[1]
            
            if entry[0] == canonT2:

                for match in entry:

                    if match[0] == entry[0]:
                        continue
                    if match[0] == canonT1:
                        return match[1]
        
        return None
    
    # adds and entry to the dictionary of least upper bound trees and edit distances
    def add_Dictionary(self, T1, T2, listingToAdd):

        canonT1 = self.canonize_tree(T1)
        canonT2 = self.canonize_tree(T2)

        # search to see if either tree already has an entry listed
        for entry in self.LUBdictionary:

            if entry[0] == canonT1:
    
                entry.append([canonT2, listingToAdd])

                return
            
            if entry[0] == canonT2:

                entry.append([canonT1, listingToAdd])

                return
        # at this point it just needs to be added as a completely new entry
        self.LUBdictionary.append([canonT1, [canonT2, listingToAdd]])
        
        return

    # achieve the canonical number of a tree
    def canonize_tree(self, tree):

        # if leaf, it is already sorted

        if len(tree) == 1:

            canonical_number = "10"

            return canonical_number
        
        # otherwise make an array to store
        # the canonical numbers of each child

        canonical_numbers_to_sort = []

        # and then canonize each child
        # while simulateously identifying the 
        # longest canonical number

        longest_number_length = 0

        for child in tree:

            # skip over the root name
            if child == tree[0]:
                continue
            
            # request canonical number, recursively
            child_canonical_number = self.canonize_tree(child)

            # append the canonical number to the array
            canonical_numbers_to_sort.append(child_canonical_number)

            # compare to longest_number
            if len(child_canonical_number) > longest_number_length:

                longest_number_length = len(child_canonical_number)

        # sort the numbers of children lexiographically
        # meaning high to low

        # first pad each with leading zeroes so all are the same length
        for number in range(0, len(canonical_numbers_to_sort)):

            # use zfill to pad the beginning of the string with zeroes
            canonical_numbers_to_sort[number] = canonical_numbers_to_sort[number].zfill(longest_number_length)
        
        # sort the canonical numbers
        canonical_numbers = self.sort_canonical_numbers(canonical_numbers_to_sort, 0, longest_number_length)

        # append them to be one big number, wrap with 1 and 0

        canonical_number = "1"

        for number in canonical_numbers:

            canonical_number += number
        
        canonical_number += "0"

        return canonical_number

    # helper method for canonize tree
    def sort_canonical_numbers(self, canonical_numbers_to_sort, index, max_length):

        # if there is nothing to sort
        if len(canonical_numbers_to_sort) < 2 or index > max_length - 1:

            # return the list
            return canonical_numbers_to_sort

        # otherwise put numbers into two bins based on their significant digit

        # for ones
        high = []

        # for zeroes
        low = []

        for number in canonical_numbers_to_sort:

            if number[index] == "1":

                high.append(number)
            
            else:

                low.append(number)
        
        # sort each bin according to the digit at the next index
        high = self.sort_canonical_numbers(high, index + 1, max_length)

        low = self.sort_canonical_numbers(low, index + 1, max_length)

        # let's now remove the leading zeroes for each number
        # because we won't need them anymore

        # for high
        for item in range(0, len(high)):

            index = 0

            while (high[item][index] != "1"):

                index += 1
            
            high[item] = high[item][index:]

        # and low
        for item in range(0, len(low)):

            index = 0

            while (low[item][index] != "1"):

                index += 1

            low[item] = low[item][index:]
        
        # append each item in low to the high bin

        for number in low:

            high.append(number)
        
        return high
    
    # this method is slightly unncessesary. test_subtree is doing grunt work
    # this method just sorts the order that the trees are passed into test_subtree
    def is_subtree(self, tree1, tree2):

        # if the trees are isomorphic then return true
        if self.canonize_tree(tree1) == self.canonize_tree(tree2):
            return True

        # treat the smaller one as the potential subtree
        if self.number_of_nodes(tree1) > self.number_of_nodes(tree2):

            subTree = tree2
            mainTree = tree1

        else:
            subTree = tree1
            mainTree = tree2

        # TO DO BEFORE, very IMPORTANT: NORMALIZE THE ACTUAL TREES
        # USING CANONICAL NUMBERS SCHEME!

        return self.test_subtree(subTree, mainTree)

    # this is the main method for testing whether one tree is a subtree of another
    # returns true if true and false if false
    def test_subtree(self, subTree, mainTree):

        if len(subTree) > len(mainTree):
            return False
        
        if self.number_of_nodes(subTree) > self.number_of_nodes(mainTree):
            return False

        # if the trees are isomorphic return true
        if self.canonize_tree(subTree) == self.canonize_tree(mainTree):
            return True
        
        # if there are sufficiently little nodes, it is already true
        if self.number_of_nodes(subTree) <= 2:
            return True
        
        # create a matrix for keeping track of successful pairings
        successMatrix = []

        # after a certain threshhold, if the trees are sorted, you don't need to check afterwards

        # for each subChild from biggest to smallest node size
        
        ''' for subChild in subTree:

            # skip the root node
            if subChild == subTree[0]:
                continue '''
        for subChild in subTree[1]:
            if isinstance(subChild, list):

                successMatrix.append(subChild)
            
            else:

                successMatrix.append([])
                successMatrix[len(successMatrix) - 1].append(subChild)

            # create a queue for possibilities to check
            possibilitiesQueue = deque()

            # for each mainChild from biggest to smallest node size
            for mainChild in mainTree:
                
                # skip the root node
                if mainChild == mainTree[0]:
                    continue

                # if a subtree is remotely possible,
                # i.e. if mainChild is of sufficient degree
                # and of sufficient number of descendants
                # TO DO: and of sufficient total levels (finish level counter method above)
                if len(mainChild) >= len(subChild) \
                and self.number_of_nodes(mainChild) >= self.number_of_nodes(subChild):

                    # add the mainChild to the possibilities queue (deque, really)
                    # we are adding in this way to they are ordered such that the
                    # possibilities with the greatest number of nodes are at the front
                    # (right) of the queue
                    possibilitiesQueue.appendleft(mainChild)
            
            # if the queue is empty then there were no possible routes
            # so we return false
            if len(possibilitiesQueue) == 0:
                return False
            
            # while there are still items in the queue
            while len(possibilitiesQueue) > 0:

                # grab the largest child from the queue
                possibility = possibilitiesQueue.pop()

                # recursive step, check if it is indeed a successful route
                if self.test_subtree(subChild, possibility):

                    successMatrix[len(successMatrix) - 1].append(possibility[0])
        
        # sort the matrix for ease of further testing
        # sorts from low to high
        successMatrix = self.sort_by_number_of_nodes_low_to_high(successMatrix)

        # if there exists a viable combination in the success matrix
        # then return true
        if self.test_success_matrix(successMatrix):
            return True
        
        # else this path was not successful and we return false
        else:
            return False
        
    # helper method for test_subtree
    def test_success_matrix(self, successMatrix):

        # base case: if there is only one child with at least one possibility
        if len(successMatrix) == 1 and len(successMatrix[0]) > 1:
            return True
        
        # if any of the children have exhausted their possibilities, return false
        for subTreeChild in successMatrix:

            if len(subTreeChild) < 2:

                return False

        for subTreeChild in successMatrix:

            for testPath in subTreeChild:

                # skip the first element in the list
                if testPath == subTreeChild[0]:
                    continue

                # create a new success matrix to be passed during the recursive step
                testPathSuccessMatrix = []

                # delete that test path from each of the remaining subtree children
                # and test if the resulting matrix is also successful

                for otherChild in successMatrix:

                    if otherChild == subTreeChild:
                        continue
                    
                    newChild = []

                    # fill newChild with all paths from otherChild except the path already chosen
                    for childTestPath in otherChild:

                        # add all paths which are not equal to the path already chosen
                        if childTestPath != testPath:

                            newChild.append(childTestPath)

                    # add this corrected child to the new success matrix to test
                    testPathSuccessMatrix.append(newChild)

                # now we have the altered success matrix, 
                # and we can test if that matrix is also successful

                # if it is successful return true

                if self.test_success_matrix(testPathSuccessMatrix):

                    return True
                
                # if it was not successful, the for loop will continue to check the next 
                # possible path

        # if we have exhausted all possibilities, no path exists
        return False

    # quicksort, it sorts from low to high number of nodes
    def sort_by_number_of_nodes_high_to_low(self, forest):

        if len(forest) <= 1:
            return forest

        # choose first tree as pivot
        pivot = forest[0]
        number_of_nodes_in_pivot = self.number_of_nodes(pivot)

        # create three arrays
        low, same, high = [], [], []

        # sort each tree into low, high, or same,
        # depending on if it has more or less nodes than
        # the pivot element

        for tree in forest:

            number_of_nodes_in_tree = self.number_of_nodes(tree)

            if number_of_nodes_in_tree == number_of_nodes_in_pivot:
                same.append(tree)

            if number_of_nodes_in_tree < number_of_nodes_in_pivot:

                low.append(tree)
            
            if number_of_nodes_in_tree > number_of_nodes_in_pivot:

                high.append(tree)
        
        # sort the high and low arrays, 'same' does not need sorting

        low = self.sort_by_number_of_nodes_high_to_low(low)

        high = self.sort_by_number_of_nodes_high_to_low(high)

        # append the three sorted arrays together

        sorted_forest = high
            
        if len(same) > 0:

            for same_item in same:

                sorted_forest.append(same_item)

        if len(low) > 0:

            for low_item in low:

                sorted_forest.append(low_item)


        return sorted_forest

    # quicksort, it sorts from low to high number of nodes
    def sort_by_number_of_nodes_low_to_high(self, forest):

        if len(forest) <= 1:
            return forest

        # choose first tree as pivot
        pivot = forest[0]
        number_of_nodes_in_pivot = self.number_of_nodes(pivot)

        # create three arrays
        low, same, high = [], [], []

        # sort each tree into low, high, or same,
        # depending on if it has more or less nodes than
        # the pivot element

        for tree in forest:

            number_of_nodes_in_tree = self.number_of_nodes(tree)

            if number_of_nodes_in_tree == number_of_nodes_in_pivot:
                same.append(tree)

            if number_of_nodes_in_tree < number_of_nodes_in_pivot:

                low.append(tree)
            
            if number_of_nodes_in_tree > number_of_nodes_in_pivot:

                high.append(tree)
        
        # sort the high and low arrays, 'same' does not need sorting

        low = self.sort_by_number_of_nodes_low_to_high(low)

        high = self.sort_by_number_of_nodes_low_to_high(high)

        # append the three sorted arrays together

        sorted_forest = low
            
        if len(same) > 0:

            for same_item in same:

                sorted_forest.append(same_item)

        if len(high) > 0:

            for high_item in high:

                sorted_forest.append(high_item)


        return sorted_forest

    def partition_forest(self, k):

        # sort the forest
        self.forest = self.sort_by_number_of_nodes_low_to_high(self.forest)

        # if k is too big there is nothing to be done
        if k >= len(self.forest) + 1:
            return

        # otherwise
        # calculate number of groups needed
        # in order to have k trees in each group

        number_of_groups = len(self.forest) // k

        # counter to keep track of where we are in the forest list
        index_in_forest = 0

        # for each group there is to do
        for i in range (1, number_of_groups):
            
            # create a group for the k or more trees
            group = []
            
            # append k trees to the group
            for tree in range(1, k):

                group.append(self.forest[index_in_forest])
    
                # increase counter
                index_in_forest += 1

            # to take care of the leftover trees
            
            # TO DO: double check these indices! They probably don't work!

            if (len(self.forest) - index_in_forest + 1) < k:

                # append all leftover trees to the last group

                while (index_in_forest != len(self.forest) - 1):

                    group.append(self.forest[index_in_forest])

                    index_in_forest += 1

            # add the group to the partitioned forest

            self.partitioned_forest.append(group)

    # TO DO: test this
    def number_of_nodes(self, tree):

        if not isinstance(tree, list):

            return 1

        # initialize nodes
        nodes = 0

        # for each node in the tree
        for node in tree:

            # if the node is a subtree
            if isinstance(node, list):

                # count the nodes in that subtree, add to node count
                nodes += self.number_of_nodes(node)
            
            # otherwise is is a regular node to count
            else:
                nodes += 1
        
        # return ttotal number of nodes
        return nodes

    # TO DO: write this
    def number_of_levels(list):

        deepest_level = 0

        return None

    # this was being used with the method below called normalize_tree
    # not useful really
    def normalize_forest(self):
        
        #normalize each tree
        for tree in self.forest:

            self.normalize_tree(tree)
            
        return None
    
    # our first attempt at normalization, not good don't use
    def normalize_tree(self, tree):
    
        # if leaf, return
        if len(tree) == 1:

            return tree
        
        # check if there is a list
        hasList = False

        for node in tree:
            if isinstance(node, list):
                hasList = True 
        
        # if there is no list, then all children are leaves
        if hasList == False:

            return tree
        
        # create three lists to store low, same, high

        low, same, high = [], [], []


        # Select pivot element as first child, for simplicity

        pivot = tree[1]

        # if it is a leaf, set children to zero
        if not isinstance(pivot, list):
            pivot_children = 0
        
        # else, count and normalize its children
        else:
            pivot_children = len(pivot) - 1
            pivot = self.normalize(pivot)

        # now we compare every other node to the pivot

        for node in tree:

            # skip the root node

            if node == tree[0]:

                low.append(node)

                continue

            # Elements that are smaller than the `pivot` go to

            # the `low` list. Elements that are larger than

            # `pivot` go to the `high` list. Elements that are

            # equal to `pivot` go to the `same` list.


            # set default children to zero
            node_children = 0

            # if the node is a list
            if isinstance(node, list):

                # access its number of children
                node_children = len(node) - 1

                # and normalize it
                node = self.normalize(node)

            # if it has less children than the pivot
            if node_children < pivot_children:

                low.append(node)

            # if equal
            elif node_children == pivot_children:

                same.append(node)

            # if greater
            elif node_children > pivot_children:

                high.append(node)


        # The final result combines the sorted `low` list

        # with the `same` list and the sorted `high` list

        low = self.normalize(low)

        high = self.normalize(high)

        if len(same) > 0:
            for same_item in same:
                low.append(same_item)
        if len(high) > 0:
            for high_item in high:
                low.append(high_item)

        return low 

    def test_LUB_method(self):
        # """
        T1 = ['rT1', ['a', ['c'], ['d']], ['b', ['e', ['f'], ['g']]]]
        T2 = ['r', ['A', ['C', ['E'], ['F']], ['D']], ['B']]
        # result should be T12 = [['r', ['x', ['x'], ['x']], ['x', ['x', ['x'], ['x']], ['x']]], 3]
        T12 = self.leastUpperBound(T1, T2)
        # got              T12 = [['x', ['a', ['c'], ['d']], ['x', ['x', ['E'], ['F']], ['D']]], 3]
        print("T12:")
        print(T12)
        

        #"""
        # this works
        T3 = ['rT3:']
        T4 = ['rT4', ['A']]
        T34 = self.leastUpperBound(T3, T4)
        # correct got [['rT4', ['A']], 1]
        print("T34:")
        print(T34)

        #"""
        T5 = ['rT5', ['a'], ['b']]
        T6 = ['rT6', ['A'], ['B', ['C']]]
        T56 = self.leastUpperBound(T5, T6)
        # correct if [['x', ['A'], ['B', ['C']]], 1]
        print("T56:")
        print(T56)

        #"""
        print("beginning of fourth example: ")
        T7 = ['a', ['c'], ['d']]
        T8 = ['A', ['C', ['E'], ['F']], ['D']]
        # correct if [['x', ['C', ['E'], ['F']], ['D']], 2]
        T78 = self.leastUpperBound(T7, T8)
        print("T78: ")
        print(T78)
        #"""

        print("bBEGINNIG OF FIFTH EXAMPLE: ")
        T9 =  ['a', ['b', ['c'], ['d']]]
        T10 = ['A', ['B', ['D'], ['E']], ['C']]
        T910 = self.leastUpperBound(T9, T10)
        # correct if [['x', ['x', ['D'], ['E']], ['C']], 1]
        print("T910: ")
        print(T910)

        # """
        print("BEGINNING OF SIXTH EXAMPLE: ")
        T11 = ['b', ['c'], ['d']]
        T12 = ['B', ['D'], ['E']]
        T1112 = self.leastUpperBound(T11, T12)
        #correct if [['x', ['D'], ['E']], 0]
        print("T1112 : ")
        print(T1112)
        # """

        print("BEGINNING OF SEVENTH EXAMPLE: ")
        T13 = ['rT1', ['a', ['c'], ['d']], ['b', ['e', ['f'], ['g']]]]
        T14 = ['r', ['A', ['C', ['E'], ['F']], ['D']], ['B']]
        # result should be T1314 = [['r', ['x', ['x'], ['x']], ['x', ['x', ['x'], ['x']], ['x']]], 3]
        T1314 = self.leastUpperBound(T13, T14)
        #              got:        [['x', ['a', ['c'], ['d']], ['x', ['x', ['E'], ['F']], ['D']]], 3]

        print("T1314:")
        print(T1314)

        print("BEGINNING OF EIGHTH EXAMPLE: ")
        T15 = ['r', ['a', ['b', ['c']]]]
        T16 = ['r', ['A'], ['B'], ['C']]
        T1516 = self.leastUpperBound(T16, T15)
        # returned [['x', ['A'], ['B'], ['a', ['b', ['c']]]], 4]
        print("T1516: ")
        print(T1516)
        
        print("BEGINNING OF NINTH EXAMPLE: ")
        T17 = ['a', ['b', ['c'], ['d']], ['f'], ['e']]
        T18 = ['A', ['B', ['C'], ['D']]]
        T1718 = self.leastUpperBound(T17, T18)
        print("T17T18: ")
        # returned [['x', ['x', ['C'], ['D']], ['f'], ['e']], 2]
        print(T1718)


        print("BEGINNING OF TENTH EXAMPLE: ")
        T19 = ['a', ['b', ['c'], ['d', ['e']]], ['f'], ['g']]
        T20 = ['A', ['B', ['C', ['D']]]]
        T1920 = self.leastUpperBound(T19, T20)
        # returned correct = [['x', ['x', ['c'], ['x', ['D']]], ['f'], ['g']], 3]
        print("T1920: ")
        print(T1920)
        
    def test_optimal_combination(self):
        """
        distancesAndTrees1 = [['a', [['A'], 0], [['B', ['C']], 1]],
                              ['b', [['A'], 0], [['B', ['C']], 1]] ]
        
        print(self.optimal_pairing(distancesAndTrees1))
        """
        distancesAndTrees2 = [[['d', ['e', ['f'], ['g'], ['h']]], 
                               [['x', ['x', ['f'], ['g'], ['F']]], 2, ['D', ['E', ['F']]]], 
                               [['x', ['x', ['f'], ['I'], ['J']]], 1, ['G', ['H', ['I'], ['J']]]], 
                               [['x', ['e', ['f'], ['g'], ['h']]], 3, ['K', ['L']]], 
                               [['x', ['e', ['f'], ['g'], ['h']]], 3, ['M', ['N']]]]
                                                                                      ]
        print(self.optimal_pairing(distancesAndTrees2))

    def test_subtree_method(self):
        """
        testing successMatrix confirmation
        """
        # should return true
        testSuccessMatrix1 = [["A1", "B1", "B3"], ["A2", "B1", "B3"], ["A3", "B4"]]
        print("First test matrix:")
        print(self.test_success_matrix(testSuccessMatrix1))

        # second testSuccessMatrix
        # should return false
        testSuccessMatrix2 = [["A1", "B1", "B3"], ["A2", "B1", "B3"], ["A3", "B1", "B3"]]     
        print("Second test matrix:")
        print(self.test_success_matrix(testSuccessMatrix2))   

        # third testSuccessMatrix
        # should return true
        testSuccessMatrix3 = [["A1", "B1"], ["A2", "B2"], ["A3", "B3"]]               
        print("third test matrix:")
        print(self.test_success_matrix(testSuccessMatrix3))

        # fourth testSuccessMatrix
        # should return false
        testSuccessMatrix4 = [["A1", "B1"], ["A2", "B2"], ["A3", "B1"]]               
        print("fourth test matrix:")
        print(self.test_success_matrix(testSuccessMatrix4))

        """ 
        testing isSubtree method
        """
        # first test
        # should return true
        mainTree1 = ["root", ["1"], ["2"]]
        subTree1 = ["root", ["3"], ["4"]]
        print("first subtree test:")
        print(self.test_subtree(subTree1, mainTree1))

        # second test
        # should return true
        mainTree2 = ["root", ["1"], ["2"]]
        subTree2= ["root", ["1"]]
        print("second subtree test:")
        print(self.test_subtree(subTree2, mainTree2))

        # third test
        # should return false
        mainTree3 = ["3", ["1"], ["2"]]
        subTree3= ["3", ["1"], ["2"], ["3"]]
        print("third subtree test:")
        print(self.test_subtree(subTree3, mainTree3))

        # fourth test
        # should return true
        mainTree4 = ["r", ["1"], ["2"], ["3", ["4", ["5"]]], ["6", ["7"], ["8"]]]
        subTree4 = ["r", ["1", ["2", ["3"]]], ["4", ["5"], ["6"]]]
        print("fourth subtree test:")
        print(self.test_subtree(subTree4, mainTree4))


        # fifth test
        # should return false
        mainTree5 = ["r", ["1", ["2", ["3"]]], ["4", ["5"], ["6"]]]
        subTree5 = ["r", ["1"], ["2"], ["3", ["4", ["5"]]], ["6", ["7"], ["8"]]]
        print("fifth subtree test:")
        print(self.test_subtree(subTree5, mainTree5))

    def test_canonical_number(self):

        practice_list = ['root', ['xvae', 'L7h1'], ['N2Di', '7iCo'], ['5g5d', 'elPP', '5Q0K']]

        # testing canonical number sorter

        canonical_numbers_to_sort = ["10","110100"]

        longest_number_length = 6

        # first pad each with leading zeroes so all are the same length

        for i in range(0, len(canonical_numbers_to_sort)):
            
            number = canonical_numbers_to_sort[i]
            # use zfill to pad the beginning of the string with zeroes
            canonical_numbers_to_sort[i] = number.zfill(longest_number_length)
        
        canonical_numbers = self.sort_canonical_numbers(canonical_numbers_to_sort , 0, longest_number_length)

        print(canonical_numbers)

        """
        testing canonical number generator
        """ 

        tree1 = ["hello"]
        tree2 = ["hello", ["world"]]
        tree3 = ["hello", ["world"], ["we're"], ["back"]]
        tree4 = ["hello", ["world"], ["did", ["you"], ["miss", ["me"]]]]

        print(self.canonize_tree(tree1))
        print(self.canonize_tree(tree2))
        print(self.canonize_tree(tree3))
        print(self.canonize_tree(tree4))



    def __init__(self):

        self.forest = []
        self.LUBdictionary = []


    def main(self):
        
        """self.generate_forest(4, 2, 2)
        
        print("forest before sorting: ")
        for tree in self.forest:
            print(tree)

        sorted_forest = self.sort_by_number_of_nodes_low_to_high(self.forest)

        print("forest after sorting: ")
        for tree in sorted_forest:
            print(tree)
        
        print("number of trees in forest: ")
        print(len(sorted_forest))"""
        
        # testing high to low sorting
        # highToLow = self.sort_by_number_of_nodes_high_to_low([['root1', ['h']], ['hey', ['i', ['am', ['home']]]], ['root2', ['hey'],['hey']], ['root3'], ['root4', ['l', ['j']], ['m']]])
        # print(highToLow)
        # self.forest = [['root1'], ['root2'], ['root3', ['a'], ['I']], ['root4', ['J'], ['q']]]
        # self.forest = [['root1'], ['root2'], ['root3'], ['root4', ['l'], ['m']]]

        
        # self.forest = [['root3', ['w']], ['root2'], ['root1']]
        # self.forest = [['root4', ['l'], ['m']], ['root3', ['w']], ['root2'], ['root1']]
        # self.forest = [['root1'], ['root2'], ['root3'], ['root4', ['l'], ['m']]]
        # self.forest = [['root1'], ['root2'], ['root3', ['a'], ['I']], ['root4', ['J'], ['q']]]
        # self.forest = [['root1', ['h']], ['hey', ['i', ['am', ['home']]]], ['root2', ['hey'],['hey']], ['root3'], ['root4', ['l', ['j']], ['m']]]
        # self.forest = [['root1'], ['root2'], ['root3'], ['hey', ['i', ['am', ['home']]]], ['root4', ['l', ['j']], ['m']]]
        # self.forest = [['root1'], ['root2'], ['root3'], ['root4'], ['root5']]
        """
        ['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'],
            ['counseling & mental health']],
        ['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']],
        ['nightlife', ['bars'], ['lounges']],
        ['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], 
            ['police departments'], ['post offices']],
        ['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], 
            ['forestry'], ['pest control'], ['funeral services & cemeteries'],
            ['appraisal services']],
        ['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]],
            ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ["breakfast & brunch"], ["burgers"]], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], 
            ['sandwiches', ['fast food']]],
        ['pets', ['animal shelters'], ['veterinarians']],
        ['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]],
            ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], 
            ['flea markets'], ['department stores']],
        ['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']],
        ['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']],
        ['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']],
        ['mass media ', ['radio stations'], ['print media']],
        ['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']],
        ['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]],
        ['beauty & spas']]"""

        editDistanceMatrix = [[['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 24]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['x', ['steakhouses', ['seafood']]], ['x', ["women's clothing"]], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['x', ['hardware stores'], ['furniture stores']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']], ['department stores']], 12]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['x', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 15]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['x', ['real estate agents'], ['steakhouses', ['seafood']], ['home developers'], ['solar installation']], ['x', ['electricity suppliers']]], 19]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 16]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['x', ['travel agents']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 17]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 17]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 18]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 18]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 18]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['x', ['fast food'], ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']]], 19]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 19]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 20]], [['nightlife', ['bars'], ['lounges']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 21]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 21]], [['mass media ', ['radio stations'], ['print media']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 21]], [['religious organizations', ['churches']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 22]], [['arts & entertainment', ['rodeo']], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 22]], [['beauty & spas'], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 23]]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['discount stores'], ['american (new)', ['steakhouses', ['seafood']]], ['x', ['fastfood']], ['x', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['x', ['breakfast & brunch'], ['burgers']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['steakhouses', ['seafood']]], 12]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 14]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['x', ['trailer rental']], ['body shop'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['car dealers'], ['auto detailing'], ['auto parts']], 5]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['x', ['electricity suppliers']], ['thrift stores'], ['x', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['art galleries'], ['flea markets'], ['plumbing']], 9]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['shipping centers'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 6]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['rv parks'], ['x', ['hardware stores'], ['furniture stores']], ['bed & breakfast'], ['hotels'], ['airports']], 7]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['steakhouses', ['seafood']], ['web design'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['accountants'], ['bookkeepers'], ['lawyers']], 7]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['hospitals'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['physical therapy'], ['dentists'], ['counseling & mental health']], 8]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['food trucks'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['bakeries'], ['grocery'], ['farmers market']], 8]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['landmarks & historical buildings'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['museums'], ['police departments'], ['post offices']], 8]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['x', ['hardware stores'], ['furniture stores']], ['art galleries'], ['swimming pools'], ['golf']], 9]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['tax services'], ['insurance'], ['title loans']], 9]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 10]], [['nightlife', ['bars'], ['lounges']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['bars'], ['lounges']], 11]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['animal shelters'], ['veterinarians']], 11]], [['mass media ', ['radio stations'], ['print media']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['radio stations'], ['print media']], 11]], [['religious organizations', ['churches']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['churches']], 12]], [['arts & entertainment', ['rodeo']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['rodeo']], 12]], [['beauty & spas'], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 13]]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['x', ['fastfood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['steakhouses', ['seafood']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 15]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['x', ['gift shops']], ['mobile phones'], ['steakhouses', ['seafood']], ['thrift stores'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['art galleries'], ['flea markets'], ['department stores']], 5]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 9]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['gas stations'], ['x', ['electricity suppliers']], ['body shop'], ['auto repair'], ['car dealers'], ['plumbing'], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 8]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['steakhouses', ['seafood']], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 1]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['gas stations'], ['x', ['travel agents']], ['body shop'], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 2]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 2]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 3]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 3]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 3]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['gas stations'], ['x', ['gyms']], ['body shop'], ['auto repair'], ['car dealers'], ['swimming pools'], ['golf']], 4]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 4]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 5]], [['nightlife', ['bars'], ['lounges']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['bars'], ['lounges']], 6]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['animal shelters'], ['veterinarians']], 6]], [['mass media ', ['radio stations'], ['print media']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['radio stations'], ['print media']], 6]], [['religious organizations', ['churches']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['churches']], 7]], [['arts & entertainment', ['rodeo']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['rodeo']], 7]], [['beauty & spas'], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 8]]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['x', ['fastfood']], ['x', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 19]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['x', ['gift shops']], ['x', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['mobile phones'], ['fashion', ["women's clothing"]], ['thrift stores'], ['art galleries'], ['flea markets'], ['department stores']], 9]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['x', ['trailer rental']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 8]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 9]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 9]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['rv parks'], ['x', ['travel agents']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['hotels'], ['airports']], 6]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['accountants'], ['bookkeepers'], ['lawyers']], 8]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['dentists'], ['counseling & mental health']], 7]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['grocery'], ['farmers market']], 7]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['police departments'], ['post offices']], 7]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['x', ['gyms']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 4]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']], ['title loans']], 6]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 5]], [['nightlife', ['bars'], ['lounges']], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['mass media ', ['radio stations'], ['print media']], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['religious organizations', ['churches']], [['x', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['arts & entertainment', ['rodeo']], [['x', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['beauty & spas'], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 8]]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['steakhouses', ['seafood']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 16]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['thrift stores'], ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']], ['art galleries'], ['flea markets'], ['department stores']], 6]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 1]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 9]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 8]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['cemeteries'], ['community service/non-profit'], ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 3]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['cemeteries'], ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 1]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['cemeteries'], ['community service/non-profit'], ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 2]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['cemeteries'], ['community service/non-profit'], ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 2]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['cemeteries'], ['community service/non-profit'], ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 2]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 5]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 3]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 4]], [['nightlife', ['bars'], ['lounges']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['bars'], ['lounges']], 5]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['animal shelters'], ['veterinarians']], 5]], [['mass media ', ['radio stations'], ['print media']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['radio stations'], ['print media']], 5]], [['religious organizations', ['churches']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['churches']], 6]], [['arts & entertainment', ['rodeo']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['rodeo']], 6]], [['beauty & spas'], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 7]]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['x', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 17]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['x', ['gift shops']], ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 7]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['x', ['trailer rental']], ['gas stations'], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 2]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['x', ['electricity suppliers']], ['rv parks'], ['bed & breakfast'], ['plumbing'], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['steakhouses', ['seafood']], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 3]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 7]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['steakhouses', ['seafood']], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 2]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['steakhouses', ['seafood']], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 1]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['steakhouses', ['seafood']], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 1]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['steakhouses', ['seafood']], ['parks'], ['museums'], ['police departments'], ['post offices']], 1]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['x', ['gyms']], ['rv parks'], ['bed & breakfast'], ['swimming pools'], ['golf']], 2]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['travel services', ['travel agents']], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 3]], [['nightlife', ['bars'], ['lounges']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['bars'], ['lounges']], 4]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['animal shelters'], ['veterinarians']], 4]], [['mass media ', ['radio stations'], ['print media']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['radio stations'], ['print media']], 4]], [['religious organizations', ['churches']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['churches']], 5]], [['arts & entertainment', ['rodeo']], [['x', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['rodeo']], 5]], [['beauty & spas'], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 6]]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['steakhouses', ['seafood']], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 17]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['thrift stores'], ['art galleries'], ['home & garden', ['hardware stores'], ['furniture stores']], ['flea markets'], ['department stores']], 7]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 2]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['advertising'], ['web design'], ['business consulting'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 8]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 1]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['advertising'], ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 2]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 7]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['advertising'], ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 1]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['advertising'], ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 1]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['advertising'], ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 1]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['advertising'], ['web design'], ['business consulting'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 4]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['advertising'], ['web design'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['advertising'], ['web design'], ['business consulting'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 3]], [['nightlife', ['bars'], ['lounges']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bars'], ['lounges']], 4]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['animal shelters'], ['veterinarians']], 4]], [['mass media ', ['radio stations'], ['print media']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['radio stations'], ['print media']], 4]], [['religious organizations', ['churches']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['churches']], 5]], [['arts & entertainment', ['rodeo']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['rodeo']], 5]], [['beauty & spas'], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 6]]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 18]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 8]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 3]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['hospitals'], ['home health care'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 2]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 1]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 1]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 6]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 0]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 0]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['hospitals'], ['home health care'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 3]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['hospitals'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 1]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['hospitals'], ['home health care'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 2]], [['nightlife', ['bars'], ['lounges']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['bars'], ['lounges']], 3]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['animal shelters'], ['veterinarians']], 3]], [['mass media ', ['radio stations'], ['print media']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['radio stations'], ['print media']], 3]], [['religious organizations', ['churches']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['churches']], 4]], [['arts & entertainment', ['rodeo']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['rodeo']], 4]], [['beauty & spas'], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 5]]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 18]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 8]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 3]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['food trucks'], ['coffee & tea'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 2]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 1]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 1]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 0]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 6]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 0]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['food trucks'], ['coffee & tea'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 3]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['food trucks'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 1]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['food trucks'], ['coffee & tea'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 2]], [['nightlife', ['bars'], ['lounges']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['bars'], ['lounges']], 3]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['animal shelters'], ['veterinarians']], 3]], [['mass media ', ['radio stations'], ['print media']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['radio stations'], ['print media']], 3]], [['religious organizations', ['churches']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['churches']], 4]], [['arts & entertainment', ['rodeo']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['rodeo']], 4]], [['beauty & spas'], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 5]]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]]], 18]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 8]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 3]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['landmarks & historical buildings'], ['parks'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 2]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 1]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 1]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 0]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 0]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 6]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['landmarks & historical buildings'], ['parks'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 3]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['landmarks & historical buildings'], ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 1]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['landmarks & historical buildings'], ['parks'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 2]], [['nightlife', ['bars'], ['lounges']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['bars'], ['lounges']], 3]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['animal shelters'], ['veterinarians']], 3]], [['mass media ', ['radio stations'], ['print media']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['radio stations'], ['print media']], 3]], [['religious organizations', ['churches']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['churches']], 4]], [['arts & entertainment', ['rodeo']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['rodeo']], 4]], [['beauty & spas'], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 5]]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['x', ['fastfood']], ['steakhouses', ['seafood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 19]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['x', ['gift shops']], ['mobile phones'], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 9]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['x', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 4]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['x', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 4]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['steakhouses', ['seafood']], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 5]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['rv parks'], ['x', ['travel agents']], ['bed & breakfast'], ['hotels'], ['airports']], 2]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['steakhouses', ['seafood']], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 4]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['steakhouses', ['seafood']], ['physical therapy'], ['dentists'], ['counseling & mental health']], 3]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['steakhouses', ['seafood']], ['bakeries'], ['grocery'], ['farmers market']], 3]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['steakhouses', ['seafood']], ['museums'], ['police departments'], ['post offices']], 3]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], 5]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['steakhouses', ['seafood']], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['steakhouses', ['seafood']], ['colleges & universities']], 1]], [['nightlife', ['bars'], ['lounges']], [['x', ['swimming pools'], ['steakhouses', ['seafood']], ['lounges']], 2]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['swimming pools'], ['steakhouses', ['seafood']], ['veterinarians']], 2]], [['mass media ', ['radio stations'], ['print media']], [['x', ['swimming pools'], ['steakhouses', ['seafood']], ['print media']], 2]], [['religious organizations', ['churches']], [['x', ['swimming pools'], ['fitness & instructions', ['gyms']], ['churches']], 3]], [['arts & entertainment', ['rodeo']], [['x', ['swimming pools'], ['fitness & instructions', ['gyms']], ['rodeo']], 3]], [['beauty & spas'], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], 4]]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 19]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['steakhouses', ['seafood']], ['thrift stores'], ['fashion', ["women's clothing"]], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 9]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 4]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['banks & credit unions'], ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 3]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 2]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 2]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 1]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 1]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 1]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['banks & credit unions'], ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 2]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 5]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['banks & credit unions'], ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 1]], [['nightlife', ['bars'], ['lounges']], [['x', ['banks & credit unions'], ['tax services'], ['bars'], ['lounges']], 2]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['banks & credit unions'], ['tax services'], ['animal shelters'], ['veterinarians']], 2]], [['mass media ', ['radio stations'], ['print media']], [['x', ['banks & credit unions'], ['tax services'], ['radio stations'], ['print media']], 2]], [['religious organizations', ['churches']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['churches']], 3]], [['arts & entertainment', ['rodeo']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['rodeo']], 3]], [['beauty & spas'], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 4]]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['steakhouses', ['seafood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 20]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['thrift stores'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 10]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['steakhouses', ['seafood']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 5]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 5]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 4]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 3]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 3]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 2]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 2]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 2]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['steakhouses', ['seafood']], ['golf']], 1]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 1]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 4]], [['nightlife', ['bars'], ['lounges']], [['x', ['middle & high schools'], ['bars'], ['lounges']], 1]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['middle & high schools'], ['animal shelters'], ['veterinarians']], 1]], [['mass media ', ['radio stations'], ['print media']], [['x', ['middle & high schools'], ['radio stations'], ['print media']], 1]], [['religious organizations', ['churches']], [['x', ['middle & high schools'], ['elementary schools'], ['churches']], 2]], [['arts & entertainment', ['rodeo']], [['x', ['middle & high schools'], ['elementary schools'], ['rodeo']], 2]], [['beauty & spas'], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 3]]], [['nightlife', ['bars'], ['lounges']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 21]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 11]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['body shop'], ['truck rental', ['trailer rental']], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 6]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 5]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 4]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 4]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 3]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 3]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 3]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['golf'], ['fitness & instructions', ['gyms']]], 2]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 1]], [['nightlife', ['bars'], ['lounges']], [['nightlife', ['bars'], ['lounges']], 3]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['animal shelters'], ['veterinarians']], 0]], [['mass media ', ['radio stations'], ['print media']], [['x', ['radio stations'], ['print media']], 0]], [['religious organizations', ['churches']], [['x', ['bars'], ['churches']], 1]], [['arts & entertainment', ['rodeo']], [['x', ['bars'], ['rodeo']], 1]], [['beauty & spas'], [['nightlife', ['bars'], ['lounges']], 2]]], [['pets', ['animal shelters'], ['veterinarians']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 21]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 11]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['body shop'], ['truck rental', ['trailer rental']], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 6]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 5]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 4]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 4]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 3]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 3]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 3]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['golf'], ['fitness & instructions', ['gyms']]], 2]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 1]], [['nightlife', ['bars'], ['lounges']], [['x', ['bars'], ['lounges']], 0]], [['pets', ['animal shelters'], ['veterinarians']], [['pets', ['animal shelters'], ['veterinarians']], 3]], [['mass media ', ['radio stations'], ['print media']], [['x', ['radio stations'], ['print media']], 0]], [['religious organizations', ['churches']], [['x', ['animal shelters'], ['churches']], 1]], [['arts & entertainment', ['rodeo']], [['x', ['animal shelters'], ['rodeo']], 1]], [['beauty & spas'], [['pets', ['animal shelters'], ['veterinarians']], 2]]], [['mass media ', ['radio stations'], ['print media']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['american (new)', ['steakhouses', ['seafood']]], ['steakhouses', ['seafood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 21]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 11]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['body shop'], ['truck rental', ['trailer rental']], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 6]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['steakhouses', ['seafood']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 6]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 5]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['steakhouses', ['seafood']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 4]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 4]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 3]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 3]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 3]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['golf'], ['fitness & instructions', ['gyms']]], 2]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 2]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 1]], [['nightlife', ['bars'], ['lounges']], [['x', ['bars'], ['lounges']], 0]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['animal shelters'], ['veterinarians']], 0]], [['mass media ', ['radio stations'], ['print media']], [['mass media ', ['radio stations'], ['print media']], 3]], [['religious organizations', ['churches']], [['x', ['radio stations'], ['churches']], 1]], [['arts & entertainment', ['rodeo']], [['x', ['radio stations'], ['rodeo']], 1]], [['beauty & spas'], [['mass media ', ['radio stations'], ['print media']], 2]]], [['religious organizations', ['churches']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 22]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 12]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 7]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 6]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['rv parks'], ['travel services', ['travel agents']], ['bed & breakfast'], ['hotels'], ['airports']], 5]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 5]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 4]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 4]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 4]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], 3]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 3]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 2]], [['nightlife', ['bars'], ['lounges']], [['x', ['bars'], ['lounges']], 1]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['animal shelters'], ['veterinarians']], 1]], [['mass media ', ['radio stations'], ['print media']], [['x', ['radio stations'], ['print media']], 1]], [['religious organizations', ['churches']], [['religious organizations', ['churches']], 2]], [['arts & entertainment', ['rodeo']], [['x', ['rodeo']], 0]], [['beauty & spas'], [['religious organizations', ['churches']], 1]]], [['arts & entertainment', ['rodeo']], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['x', ['steakhouses', ['seafood']], ['american (new)', ['steakhouses', ['seafood']]], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 22]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['x', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 12]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['x', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 7]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['x', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 7]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['x', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 6]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['x', ['rv parks'], ['travel services', ['travel agents']], ['bed & breakfast'], ['hotels'], ['airports']], 5]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['x', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 5]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['x', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 4]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['x', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 4]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['x', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 4]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['x', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], 3]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['x', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 3]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['x', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 2]], [['nightlife', ['bars'], ['lounges']], [['x', ['bars'], ['lounges']], 1]], [['pets', ['animal shelters'], ['veterinarians']], [['x', ['animal shelters'], ['veterinarians']], 1]], [['mass media ', ['radio stations'], ['print media']], [['x', ['radio stations'], ['print media']], 1]], [['religious organizations', ['churches']], [['x', ['churches']], 0]], [['arts & entertainment', ['rodeo']], [['arts & entertainment', ['rodeo']], 2]], [['beauty & spas'], [['arts & entertainment', ['rodeo']], 1]]], [['beauty & spas'], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], [['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]], ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ['breakfast & brunch'], ['burgers']], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]], 23]], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], [['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]], ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], ['flea markets'], ['department stores']], 13]], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], [['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'], ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], 8]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], [['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]], 8]], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], [['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['appraisal services']], 7]], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], ['hotels'], ['airports']], 6]], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], [['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], 6]], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], [['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'], ['counseling & mental health']], 5]], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], [['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], 5]], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], [['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], ['police departments'], ['post offices']], 5]], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], [['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], 4]], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], [['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']], 4]], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], [['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], 3]], [['nightlife', ['bars'], ['lounges']], [['nightlife', ['bars'], ['lounges']], 2]], [['pets', ['animal shelters'], ['veterinarians']], [['pets', ['animal shelters'], ['veterinarians']], 2]], [['mass media ', ['radio stations'], ['print media']], [['mass media ', ['radio stations'], ['print media']], 2]], [['religious organizations', ['churches']], [['religious organizations', ['churches']], 1]], [['arts & entertainment', ['rodeo']], [['arts & entertainment', ['rodeo']], 1]], [['beauty & spas'], [['beauty & spas'], 1]]]]

        
        # print("greedily anonymized forest: ")

        
        """treexmpl1 = ['root', ['x', 'x', 'x', 'x']]
        treexmpl2 = ['root', ['x', ['x', ['x']]]]
        forestxmpl1 = [treexmpl1, treexmpl2]
        

        T1 = ['x', ['x', ['x', 'x']]]
        T2 = ['x']
        T12 = self.leastUpperBound(T1, T2)
        print("T12:")
        print(T12)

        T7 = ['a', ['b', ['c']], ['d', ['e', ['f'], ['g'], ['h']]]]
        T8 = ['A', ['B', ['C']], ['D', ['E', ['F']]], ['G', ['H', ['I'], ['J']]], ['K', ['L']], ['M', ['N']]]
        T78 = self.leastUpperBound(T7, T8)
        # with edit distance 9
        print("T78: ")
        print(T78)"""

        print("running...")
        self.generate_forest(20, 4, 4)

        anonymized_forest_greedy = self.anonymize_forest_greedy()

        for tree in anonymized_forest_greedy[0]:
            print(tree)

        print("total edit distance greedy: ")
        print(anonymized_forest_greedy[1])

        print("number of trees in anonymized forest:")
        print(len(anonymized_forest_greedy))

        print("which trees were matched")

        for pair in anonymized_forest_greedy[2]:
            print("=========")
            print(pair[0])
            print("was matched with")
            print(pair[1])
 
        # self.forestEditDistanceMatrix = editDistanceMatrix
        # print("edit Distance Matrix used: ")
        # print(self.forestEditDistanceMatrix)

        print("running...")
        

        # print("brute-forcedly anonymized forest: ")
        # anonymized_forest_brute = self.anonymize_forest_brute_force()

        # for tree in anonymized_forest_brute[0]:
        #    print(tree)
        
        # print("total edit distance brute: ")
        # print(anonymized_forest_brute[1])

        print("greedily anonymized forest: ")

        for tree in anonymized_forest_greedy[0]:
            print(tree)

        print("total edit distance greedy: ")
        print(anonymized_forest_greedy[1])

        print("COMPLEXITY: ")
        print(self.getComplexity())
        # print("edit distance matrix used: ")
        # print(self.forestEditDistanceMatrix)


        """
        editDistanceMatrix = [[['B'], [['B'], [['B'], 0]]]]
        print(self.anonymize_forest_greedy(editDistanceMatrix))

        # self.test_optimal_combination()

        # extra examples
        T5 = ['f', ['x', ['6']], ['u', ['2', ['q'], ['M']]]]
        T6 = ['c', ['x', ['K', ['l', ['E']], ['4', ['a', ['y'], ['f'], ['l']]], ['G', ['J', ['3'], ['A']]]]], ['K', ['C']]]
        T56 = self.leastUpperBound(T5, T6)
        print("T56:")
        print(T56)
        """
        """
        T7 = ['a', ['b', ['c']], ['d', ['e', ['f'], ['g'], ['h']]]]
        T8 = ['A', ['B', ['C']], ['D', ['E', ['F']]], ['G', ['H', ['I'], ['J']]], ['K', ['L']], ['M', ['N']]]
        T78 = self.leastUpperBound(T7, T8)
        ['x', ['x', ['C']], ['x', ['x', ['f'], ['I'], ['J']]], [['D', ['E', ['F']]], 2], ['K', ['L']], ['M', ['N']]]
        # with edit distance 9
        print("T78: ")
        print(T78)"""
        """
        # example that didn't work 
        T9 = ['C', ['N', ['q', ['J'], ['m'], ['f'], ['F']]], ['w', ['O', ['r']]]]
        # Random Tree 2:
        T10 = ['q', ['C', ['b']], ['v', ['f', ['Y'], ['h']]], ['T', ['i', ['U'], ['v'], ['u'], ['m'], ['n']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]]
        print("BEGINNING OF EXAMPLE")
        T910 = self.leastUpperBound(T9, T10)
        print("T910: ")
        print(T910)"""

        # Common Tree & LUB:

        # [['x', ['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], ['x', ['O', ['r']]], ['v', ['f', ['Y'], ['h']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]], 14]
        # got = ['x', ['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], ['x', ['x', ['Y'], ['h']]], ['C', ['b']], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]]

        """[[['root3', ['w']], [['root3', ['w']], [['root3', ['w']], 2]], [['root2'], [['root3', ['w']], 1]], [['root1'], [['root3', ['w']], 1]]], 
         [['root2'], [['root3', ['w']], [['root3', ['w']], 1]], [['root2'], [['root2'], 1]], [['root1'], [['root1'], 0]]], 
         [['root1'], [['root3', ['w']], [['root3', ['w']], 1]], [['root2'], [['root2'], 0]], [['root1'], [['root1'], 1]]]]

        [[['root3', ['w']], [['root3', ['w']], [['root3', ['w']], 2]], [['root2'], [['root3', ['w']], 1]], [['root1'], [['root3', ['w']], 1]]], 
         [['root2'], [['root3', ['w']], [['root3', ['w']], 1]], [['root2'], [['root2'], 1]], [['root1'], [['root1'], 0]]], 
         [['root1'], [['root3', ['w']], [['root3', ['w']], 1]], [['root2'], [['root2'], 0]], [['root1'], [['root1'], 1]]]]
"""
if __name__ == '__main__':
    Forest().main()