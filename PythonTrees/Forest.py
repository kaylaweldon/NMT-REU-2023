from collections import deque

"""Random Tree 1:
['C', ['N', ['q', ['J'], ['m'], ['f'], ['F']]], ['w', ['O', ['r']]]]
Random Tree 2:
['q', ['C', ['b']], ['v', ['f', ['Y'], ['h']]], ['T', ['i', ['U'], ['v'], ['u'], ['m'], ['n']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]]
Common Tree & LUB:
[['x', ['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], ['x', ['O', ['r']]], ['v', ['f', ['Y'], ['h']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]], 14]"""
class Forest:

    from RandomTreeGenerator import RandomTreeGenerator
    import random

    # the list containing trees of the forest
    forest = []

    # the list containing edit distances and LUBTs between each tree in the forest
    forestEditDistanceMatrix = []

    # dictionary for keeping track of Least upper bounds found
    # we should store things as their canonical numbers so isomorphic trees can be found
    LUBdictionary = []


    def __get_forest__(self):
        return self.forest
    
    def build_forest_from_matrix_of_matches(self, matrixOfMatches):
        
        anonymized_forest = []

        for pairIndex in range(0, len(matrixOfMatches)):

            if pairIndex == len(matrixOfMatches) - 1:
                continue

            anonymized_forest.append(matrixOfMatches[pairIndex][2][0])
            anonymized_forest.append(matrixOfMatches[pairIndex][2][0])

        return anonymized_forest
    
    def anonymize_forest_greedy(self, editDistanceMatrix):

        indicesOfTakenTrees = []
        matrixOfMatches = []

        for treeIndex in range(0, len(editDistanceMatrix)):
            
            # if it has already been paired, continue
            if treeIndex in indicesOfTakenTrees:
                continue

            
            # this is where the edit distance for the first match is stored
            leastEditDistanceForTree = editDistanceMatrix[treeIndex][1][1][1]
            indexFound = 1

            # for each pairing available for that tree
            for matchIndex in range(1, len(editDistanceMatrix[treeIndex])):
                
                # if it has already been paired, continue
                if matchIndex - 1 in indicesOfTakenTrees:
                    continue
                
                if editDistanceMatrix[treeIndex][matchIndex][1][1] < leastEditDistanceForTree:

                    leastEditDistanceForTree = editDistanceMatrix[treeIndex][matchIndex][1][1]
                    indexFound = matchIndex

                indicesOfTakenTrees.append(matchIndex - 1)
            
            
            matchToAppend = [editDistanceMatrix[treeIndex][0], 
                             editDistanceMatrix[treeIndex][matchIndex][0],
                               editDistanceMatrix[treeIndex][matchIndex][1]]
            
            matrixOfMatches.append(matchToAppend)
            indicesOfTakenTrees.append(treeIndex)

        totalEditDistance = 0

        for pair in matrixOfMatches:

            totalEditDistance += pair[2][1]
        
        matrixOfMatches.append(totalEditDistance)
    
        return matrixOfMatches
    
    # given a forest, calculate the edit distance and LUBT for every possible 
    # pair of trees within the forest 
    # puts them in a global structure called forestEditDistanceMatrix
    def gather_edit_distances_for_forest(self):

        sorted_forest = self.sort_by_number_of_nodes(self.forest)

        self.forestEditDistanceMatrix = []

        for tree in range(0, len(sorted_forest)):

            self.forestEditDistanceMatrix.append([sorted_forest[tree]])

            for match in range(0, len(self.forest)):
                
                self.forestEditDistanceMatrix[tree].append([sorted_forest[match]])

                # this represents the trees matching with themselves along the diagonal
                # instead of filling it in with a zero, we are going to use it to represent 
                # the case where we choose to duplicate the tree and therefore need to 
                # create a tree of equal number of nodes
                if match == tree:

                    LUBTandEditDistance = [sorted_forest[match], self.number_of_nodes(sorted_forest[match])]
                
                # otherwise we just find the edit distance and LUBT of the two different trees
                else:

                    LUBTandEditDistance = self.leastUpperBound(sorted_forest[tree], sorted_forest[match])

                self.forestEditDistanceMatrix[tree][match + 1].append(LUBTandEditDistance)
 
    

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

        # dictionaryEntry = self.search_Dictionary(T1, T2)

        # if dictionaryEntry != None:
        #     return dictionaryEntry[0] 

        # base case
        # if either T1 or T2 consists of a single node

        if len(T1) == 1 or len(T2) == 1:

            T1nodes = self.number_of_nodes(T1)
            T2nodes = self.number_of_nodes(T2)

            # edit distance is the difference in their nodes
            editDistance = abs(T1nodes - T2nodes)
            
            # return the bigger tree, or T2 if they are equal
            if T1nodes > T2nodes:

                leastUpperBoundTree = T1

            if T1nodes == T2nodes:

                leastUpperBoundTree = T2
            
            if T1nodes < T2nodes:

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

            # for each child of the root of T2
            for childT2 in range(1, len(T2)):
                
                """
                print("pairing with: ")
                print(T1[childT1])
                print("is: ")
                print(T2[childT2])
                """

                # consult dictionary to see if trees isomorphic to childT1 and childT2 have
                # already been evaluated

                dictionaryPairingResult = self.search_Dictionary(T1[childT1], T2[childT2])

                # if there was an entry in the dictionary, return the entry
                if dictionaryPairingResult != None:

                    """
                    print("Dictionary result found. Result: of ")
                    print(T1[childT1])
                    print("and ")
                    print(T2[childT2])
                    print("is: ")
                    print(dictionaryPairingResult)
                    """
                    
                    dictionPairingResultToSend = [dictionaryPairingResult[0], dictionaryPairingResult[1], T2[childT2]]

                    # print("dictionPairingResultToSend: ")
                    # print(dictionPairingResultToSend)

                    distancesAndTrees[len(distancesAndTrees) - 1].append(dictionPairingResultToSend)
                
                # otherwise we must find the answer ourselves
                # THIS IS THE RECURSIVE STEP
                else:

                    pairingResult = self.leastUpperBound(T1[childT1], T2[childT2])

                    """
                    print("adding to dictionary ")
                    print(T1[childT1])
                    print("and ")
                    print(T2[childT2])
                    print("as")
                    print(pairingResult)
                    """

                    self.add_Dictionary(T1[childT1], T2[childT2], pairingResult)

                    # print("dictionary is now: ")
                    # print(self.LUBdictionary)

                    """
                    print("LUBT and edit Distance of :")
                    print(T1[childT1])
                    print("and")
                    print(T2[childT2])
                    print("is: ")
                    print(pairingResult)
                    """

                    # wrap the LUBT in ssome necessary brackets and send child information 
                    # incase the child needs to be duplicated
                    pairingResultToSend = [pairingResult[0], pairingResult[1], T2[childT2]]
                    # print("pairing result to send: ")
                    # print(pairingResultToSend)

                    # append the result to the list of results found for tree one
                    distancesAndTrees[len(distancesAndTrees) - 1].append(pairingResultToSend)
        """
        now that we've calculated all the pairs LUBT and edit distances we have to find the 
        best combination, i.e. how we should match children of T1 with children of T2 such that 
        the sum of edit distances is minimized
        we have another method that will find this optimal combination called optimal_pairing
        """

        
        print("distances and trees to be sent to for optimization: ")
        print(distancesAndTrees)
        

        optimalPairingAndEditDistance = self.optimal_pairing(distancesAndTrees)

        
        print("Optimal pairing and edit distance: ")
        print(optimalPairingAndEditDistance)
        
            
        # we want to use the above result to contruct a tree out of the LUBTs that it returns
        # along with any leftovers   
        # placeholder joining parent called 'x'
        finalLUBT = ['x']

        # the first item in optimalPairingAndEditDistance is a list of all the LUBTs that should be appended a root
        for LUBT in optimalPairingAndEditDistance[0]:

            finalLUBT.append(LUBT)
        
        finalEditDistance = optimalPairingAndEditDistance[1]

        
        print("final return for this recursion of trees ")
        print(T1)
        print("and ")
        print(T2)
        print("is: ")
        print([finalLUBT, finalEditDistance])
        

        return [finalLUBT, finalEditDistance]


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

        # add this to the editDistance assocaited with the best pair and we have our final editDistance
        print("LUBTlistToReturn: ")
        print(LUBTlistToReturn)

        # this will cause a problem with how ive set it up. really it should be wrapped in the aprentheses, all the above should, and then
        # they should be unwrapped later.
        # also each leftover should be appended to LUBTlist to return which starts with the main LUBT 

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

        # print("distancesAndTrees:")
        # print(distancesAndTrees)

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

                return [childrenToReturn, editDistance]

        # base case
        # if the matrix contains only one child of T1
        if len(distancesAndTrees) == 1:

            # if that child has no matches listed:
            if len(distancesAndTrees[0]) == 1:

                # that child itself must be constructed but there are no other leftovers
                # the edit distace is the number of nodes contained in child
                return [[distancesAndTrees[0]], self.number_of_nodes(distancesAndTrees[0])]
        
            # if that child has exactly one match listed:
            if len(distancesAndTrees[0]) == 2:
                
                # return that match, which contains the information [LUBT(child, match), d(child, match)]
                # as well as the leftovers, which are empty
                return [[distancesAndTrees[0][1][0]], distancesAndTrees[0][1][1]]
            
            # else that child has more than one match listed:
            # this is a special case where leftovers must be accounted for
            # it's a long and complicated case that we wrote another method for
            if len(distancesAndTrees[0]) > 2:

                return self.deal_with_leftovers(distancesAndTrees)
                leftover_combination_matrix = []

                matches_with_least_edit_distances = []
                        
                leftovers = []

                # find the match with least edit distance and choose that to be paried with the child
                # pick the editDistance associated with the first match to compare to the rest
                # as well as keep track of which LUBT it has
                
                bestLUBT = distancesAndTrees[0][1][0]
                leastEditDistance = distancesAndTrees[0][1][1]
                OGtreeofbestLUBT = distancesAndTrees[0][1][2]
                # print("loop reached")

                # compare it to the rest
                for match in range(2, len(distancesAndTrees[0])):
                    #print("match: ")
                    #print(match)

                    # if it is smaller 
                    if distancesAndTrees[0][match][1] < leastEditDistance:

                        # append the current best its LUBT to the leftovers list,
                        # as it is about to be updated and will no longer be used
                        leftovers.append(OGtreeofbestLUBT)

                        # update the LUBT and leastEditDistance
                        bestLUBT = distancesAndTrees[0][match][0]
                        leastEditDistance = distancesAndTrees[0][match][1]
                        OGtreeofbestLUBT = distancesAndTrees[0][match][2]
                
                    # else just its LUBT should be added to the leftovers (we dont care about its editDistance anymore
                    else:
                        leftovers.append(distancesAndTrees[0][match][2])
                
                # now we have to add the total edit distance, which must include the number of nodes of the 
                # leftovers as they will have to be completely duplicated

                numberOfLeftoverNodes = 0
                LUBTlistToReturn = [bestLUBT]

                print("leftovers: ")
                print(leftovers)

                for leftover in leftovers:

                        numberOfLeftoverNodes += self.number_of_nodes(leftover)
                        LUBTlistToReturn.append(leftover)

                # add this to the editDistance assocaited with the best pair and we have our final editDistance
                print("LUBTlistToReturn: ")
                print(LUBTlistToReturn)

                totalEditDistance = numberOfLeftoverNodes + leastEditDistance

                # this will cause a problem with how ive set it up. really it should be wrapped in the aprentheses, all the above should, and then
                # they should be unwrapped later.
                # also each leftover should be appended to LUBTlist to return which starts with the main LUBT 

                return [LUBTlistToReturn, totalEditDistance]
        
        # other wise if it is not a base case
        # we first initialize a data structure to store information about every possible combination of matches
        combinationOptions = []
        
        # FIRST CHILD REPLICATE OPTION
        # account for the case where the first child is chosen to be replicated
        combinationOptions.append([])
        combinationOptions[len(combinationOptions) - 1].append([[distancesAndTrees[0][0]]])
        combinationOptions[len(combinationOptions) - 1][0].append(self.number_of_nodes(distancesAndTrees[0][0]))
        combinationOptions[len(combinationOptions) - 1][0].append([distancesAndTrees[0][0]])

        print("combination options after adding first child replicate case: ")
        print(combinationOptions)
        
        alteredMatrix = []

        for child in range(1, len(distancesAndTrees)):

            alteredMatrix.append(distancesAndTrees[child])     

        print("altered Matrix to send recursively for first child replicate case: ")
        print(alteredMatrix)

        alteredMatrixBestOption = self.optimal_pairing(alteredMatrix)

        print("altered matrix best option: ")
        print(alteredMatrixBestOption)

        alteredMatrixBestOption = self.optimal_pairing(alteredMatrix)

        combinationOptions[len(combinationOptions) - 1].append(alteredMatrixBestOption)
        #print("combinationOptions after adding result of altered matrix: ")
        # print(combinationOptions)

    
        # for each match of the first child in the matrix (distancesAndTrees)
        for match in range(1, len(distancesAndTrees[0])):

            print("match chosen: ")
            print(distancesAndTrees[0][match])

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

                # why is this necessary?
                alteredMatrix.append([])
                
                # starting from range zero so as to include the original subtree associated with the child
                # although maybe this is not necessary
                for alteredMatches in range(0, len(distancesAndTrees[child])):
                    
                    # if we've reached the chosen column with is taken by the match for the first child, we skip it 
                    if alteredMatches == match:
                        continue
                    
                    # otherwise we append to our altered matrix
                    alteredMatrix[len(alteredMatrix) - 1].append(distancesAndTrees[child][alteredMatches])

            # now that we have constructed our altered matrix, we find its best option
            # this is the recursive step
            # it is of the form [bestLUBT, totalEditDistance, leftovers]

            print("altered Matrix: ")
            print(alteredMatrix)

            alteredMatrixBestOption = self.optimal_pairing(alteredMatrix)

            print("altered matrix best option: ")
            print(alteredMatrixBestOption)

            combinationOptions[len(combinationOptions) - 1].append(alteredMatrixBestOption)
            print("combinationOptions after adding result of altered matrix: ")
            print(combinationOptions)

        # finally sum up the edit distances of each of the options
        # assume the first one is the best and compare it to the rest
        bestOption = combinationOptions[0]
        bestEditDistance = 0
        # we have to add up the editDistances for the first one to have a comparable editDistance
        for match in combinationOptions[0]:
            
            # this is where the editDistance is located in the match
            bestEditDistance += match[1]

        # now we search the options to find the least editDistance
        for option in combinationOptions:
            
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

        print("best option:")
        print(bestOption)
        bestChildrenToJoin = []

        for match in bestOption:

                for LUBT in match[0]:

                    bestChildrenToJoin.append(LUBT)
        
        # now we have the best combination, and its edit distance! we finally return

        return [bestChildrenToJoin, bestEditDistance]
    
    # TO DO: DICTIONARY DOESN'T WORK YET
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

    # TO DO: DICTIONARY DOESN'T WORK YET
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
        successMatrix = self.sort_by_number_of_nodes(successMatrix)

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

    # Let's do a quicksort with this, it sorts from low to high number of nodes
    # TO DO: test this. should sort from low to high
    def sort_by_number_of_nodes(self, forest):

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

        low = self.sort_by_number_of_nodes(low)

        high = self.sort_by_number_of_nodes(high)

        # append the three sorted arrays together

        sorted_forest = low
            
        if len(same) > 0:

            for same_item in same:

                sorted_forest.append(same_item)

        if len(high) > 0:

            for high_item in high:

                sorted_forest.append(high_item)


        return sorted_forest
    
    # TO DO: test this
    def partition_forest(self, k):

        # sort the forest
        self.forest = self.sort_by_number_of_nodes(self.forest)

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

        choose_leftovers = [[['w', ['O', ['r']]], [['x', ['O', ['r']]], 1, ['C', ['b']]], [['x', ['x', ['Y'], ['h']]], 1, ['v', ['f', ['Y'], ['h']]]], [['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], 4, ['T', ['i', ['U'], ['v'], ['u'], ['m'], ['n']]]], [['x', ['O', ['r']]], 1, ['I', ['z']]]]]

        print(choose_leftovers)

        LUBTlistReturned = self.deal_with_leftovers(choose_leftovers)

        print(LUBTlistReturned)

        """
        editDistanceMatrix = [[['B'], [['B'], [['B'], 0]]]]
        print(self.anonymize_forest_greedy(editDistanceMatrix))"""

        # self.test_optimal_combination()
        """
        # extra examples
        T5 = ['f', ['x', ['6']], ['u', ['2', ['q'], ['M']]]]
        T6 = ['c', ['x', ['K', ['l', ['E']], ['4', ['a', ['y'], ['f'], ['l']]], ['G', ['J', ['3'], ['A']]]]], ['K', ['C']]]
        T56 = self.leastUpperBound(T5, T6)
        print("T56:")
        print(T56)"""
        """
        T7 = ['a', ['b', ['c']], ['d', ['e', ['f'], ['g'], ['h']]]]
        T8 = ['A', ['B', ['C']], ['D', ['E', ['F']]], ['G', ['H', ['I'], ['J']]], ['K', ['L']], ['M', ['N']]]
        T78 = self.leastUpperBound(T7, T8)
        ['x', ['x', ['C']], ['x', ['x', ['f'], ['I'], ['J']]], [['D', ['E', ['F']]], 2], ['K', ['L']], ['M', ['N']]]
        # with edit distance 9
        print("T78: ")
        print(T78)"""
        
        # example that didn't work 
        T9 = ['C', ['N', ['q', ['J'], ['m'], ['f'], ['F']]], ['w', ['O', ['r']]]]
        # Random Tree 2:
        T10 = ['q', ['C', ['b']], ['v', ['f', ['Y'], ['h']]], ['T', ['i', ['U'], ['v'], ['u'], ['m'], ['n']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]]
        print("BEGINNING OF EXAMPLE")
        T910 = self.leastUpperBound(T9, T10)
        print("T910: ")
        print(T910)

        # Common Tree & LUB:

        # [['x', ['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], ['x', ['O', ['r']]], ['v', ['f', ['Y'], ['h']]], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]], 14]
        # got = ['x', ['x', ['x', ['U'], ['v'], ['u'], ['m'], ['n']]], ['x', ['x', ['Y'], ['h']]], ['C', ['b']], ['L', ['T', ['i'], ['J'], ['G'], ['B']]], ['I', ['z']]]

        """self.generate_forest(4, 2, 2)
        print(self.forest)

        for tree in self.forest:
            print(tree)
        
        print("forest before sorting: ")
        for tree in self.forest:
            print(tree)

        sorted_forest = self.sort_by_number_of_nodes(self.forest)

        print("forest after sorting: ")
        for tree in sorted_forest:
            print(tree)

        self.gather_edit_distances_for_forest()
        print("edit distance matrix not chosen yet: ")
        print(self.forestEditDistanceMatrix)
        print("editDistance matrix final: ")
        anonymized_list = self.anonymize_forest_greedy(self.forestEditDistanceMatrix)
        print(anonymized_list)
        print("anonymous forest: ")
        anonymized_forest = self.build_forest_from_matrix_of_matches(anonymized_list)
        print(anonymized_forest)
        print(len(anonymized_forest))"""




if __name__ == '__main__':
    Forest().main()