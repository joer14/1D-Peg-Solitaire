#1D Peg Solitaire
#Joe Rowley
#jrowley@ucsc.edu
#For CS101
#Winter Quarter 2013
#Manfred Warmuth

from optparse import OptionParser
import math
def getInput():
    input_board = raw_input("Enter board:")
    return input_board.upper().strip().replace('X', '1').replace('|', '0').replace(" ", "")

class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    

class HashTable:
    myList = list([0]*4097)

    def __init__(self):
        self.hashTableSize = 10
        self.myList = list([0]*self.hashTableSize)
        self.load = 0

    def search(self,key):
        #print "doing lookup for: ", key
        searching = True
        attempt = 0
        while (searching):
            thehash = self.hash(key, attempt)

            if (self.myList[attempt] == key ):
                #print "found in table"
                return True 
            if (self.myList[attempt] == int("0")):
                return False
            attempt = attempt+1

        
    def insert(self, value):
        self.checkLoad()
        #print "Inserting"  
        key = self.hash(value,0)
        self.myList[key] = value
        self.load = self.load + 1
        return self.myList
        
        # call self.hash(key) to get index
        # insert key value pair into table .

    def hash(self,key, ivalue):
        h1 = self.hash1(key)
        h2 = self.hash1(key)
        m = float(self.hashTableSize) 
        
        return int((h1 + ivalue*h2) % m)
  
    def hash1(self,value):
        A = (math.sqrt(5)-1)/2
        key = float(value)  
        frac = key*A % 1
        m = float(self.hashTableSize) 

        return math.floor(m*frac)

    def hash2(self,value):
        A = (math.sqrt(5)-1)/2
        key = float(value)  
        frac = key*A % 1
        m = float(self.hashTableSize) 
        return math.floor(m*((m*frac) % 1))


    def printHash(self):
        print "Printing HashTable:"
        loadRatio = float(self.load)/float(self.hashTableSize)
        print "Load Ratio: ", loadRatio, "hashTableSize: ", self.hashTableSize, " Load: ", self.load

        for nums in self.myList:
            if (nums != 0):
                print nums

    def checkLoad(self):
        loadRatio = float(self.load)/float(self.hashTableSize)
        if (loadRatio > .2):
            #print "ratio >.2 so quading"
            #print "Load Ratio: ", loadRatio, "hashTableSize: ", self.hashTableSize, " Load: ", self.load
            self.quadHashTable()
        return loadRatio


    def quadHashTable(self):
        print "quading"
        oldLength = int(self.hashTableSize)
        self.load = int(0)
        self.hashTableSize = (oldLength*4) + 1      #set new hash table size 
        myOldList = list(self.myList)                     #get old hashtable 
        self.myList = list([0]*self.hashTableSize)  #create a new blank list of that size
        self.insert(0) #want to add one zero
        for values in myOldList:
            if (values != 0):              #only want to insert values that aren't zero
                self.insert(values)
                #print(values)
        


def moves(pegs):
    moves = list()
    pegsList = list(pegs)
    
    for idx, peg in enumerate(pegsList):
        cpPegsList = list(pegsList)
        currentPeg = int(pegsList[idx])

        if (currentPeg == 0): #can't move a double peg
            if (idx - 3 >= 0): ## not out of bounds to the left
                if (int(pegsList[idx-3]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx-1]) + int(pegsList[idx-2]) == 0): # jumped over 2 single pegs peg to the direct left
                        #print "jumped over two single pegs to the left", idx
                        del cpPegsList[idx]
                        cpPegsList[idx-3]= int(cpPegsList[idx-3])+1
                        moves.append(cpPegsList)
                        cpPegsList = list(pegsList)

            if (idx - 2 >= 0): ## not out of bounds to the left
                if (int(pegsList[idx-2]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx-1]) == 1): # jumped over the a double peg to the direct left
                        #print "jumped over double pegs to the left", idx
                        del cpPegsList[idx]
                        cpPegsList[idx-2]= int(cpPegsList[idx-2])+1
                        moves.append(cpPegsList)
                        cpPegsList = list(pegsList)
            #print len(pegsList)
            if (idx + 2 < len(pegsList)): ## not out of bounds to the right
                if (int(pegsList[idx+2]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx+1]) == 1): # jumped over the a double peg to the direct right
                        #print "jumped over double pegs to the right", idx
                        
                        cpPegsList[idx+2]= int(cpPegsList[idx+2])+1
                        del cpPegsList[idx]
                        moves.append(cpPegsList)
                        cpPegsList = list(pegsList)

            if (idx + 3 < len(pegsList)): ## not out of bounds to the right
                if (int(pegsList[idx+3]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx+1]) + int(pegsList[idx+2]) == 0): # jumped over 2 single pegs peg to the direct left
                        #print "jumped over two single pegs to the right", idx
                        
                        cpPegsList[idx+3]= int(cpPegsList[idx+3])+1
                        del cpPegsList[idx]
                        moves.append(cpPegsList)
                        cpPegsList = list(pegsList)
    
    #print "Moves: " + str(moves)
    return moves


def is_solved ( pegs, table, stack, hashOn):
    #print "Doing is_solved on: ", pegs 
    if (hashOn):
        if (table.search(pegs)):
            #print "table look up says false for: ", pegs
            return False, stack 
    for m in moves(pegs) :  #where moves p is an array that returns all possible moves
        board = ''.join(str(elem) for elem in m)
        #print m
        if (board == len(board)*'1'):
            stack.append(m)
            return True, stack

        result = is_solved(''.join(str(elem) for elem in m), table, stack, hashOn)
        stack1 = result[1]
        if (result[0]):
            #print "true:::", m      #//prints in reverse so would use a stack to print in reverse order
            if (stack1[0] == ""):
                stack1[0] = "11111"
            #print "stack1[0] ", stack1[0]
            stack1.append(m)
            return True, stack1
    if (hashOn):
        table.insert(pegs)
    return False, stack


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    filename = "none"

    parser.add_option("-f", "--file", dest="filename",
                      help="use FILENAME as a board", default="True")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    parser.add_option("-o", "--hashoff",
                      action="store_true", dest="hashOff", default="False")
    
    (options, args) = parser.parse_args()
    hashOff = True
    if (options.hashOff == True):
        hashOff = True
    else:
        hashOff = False
    hashOn = not hashOff
    if (options.filename == "True"):
        converted_board = getInput()
    else:
        f = open(options.filename, 'r')
        numberOfPegs = f.readline().rstrip()
        converted_board = f.readline().strip().upper().replace('X', '1').replace('|', '0').replace(" ", "")
        if options.verbose: 
            print "reading %s..." % options.filename
            print "number of Pegs: ", numberOfPegs
            

    print "Board =", converted_board
    
    #moves(converted_board)
    if (hashOn):
        print "Hashing On"
    else: 
        print "Hashing Off"

    t = HashTable()
    stack = list()
    results = is_solved(converted_board, t, stack, hashOn)
    if (results[0]):
        print "Solvable"
        print "Initial Board: "
        print "        ", ' '.join(converted_board)
        stack = results[1]
        stack = reversed(stack)
        for index, item in enumerate(stack):
            print "Step", index + 1,":", ' '.join(str(elem) for elem in item)
    else:
        print "Not Solvable"
    
 


if __name__ == "__main__":
    main()