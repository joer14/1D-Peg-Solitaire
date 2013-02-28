# import sys, getopt
# from optparse import OptionParser

# #input_board = raw_input("Enter board:")
# #print "raw_input =", str1

from optparse import OptionParser
def getInput():
    input_board = raw_input("Enter board:")
    return input_board.upper().strip().replace('X', '1').replace('|', '0').replace(" ", "")

class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    

class HashTable:
    myList = list([0]*10)
    def __init__(self):
        self.myList = list([0]*10)

    def get(self,key):
        return self.myList[key]
        # call self.hash(key) for an index
        # return that key following collisions

    def set(self,key,value):
        self.myList[key] = value
        return self.myList
        
        # call self.hash(key) to get index
        # insert key value pair into table .

    def hash(self,key):
        hashkey=key #collisions much?
        return hashkey

        #  def hash(self,key):
        # # loop through the characters of the key
        # #     convert the character to a number  (use ord(c))
        # #     add this number to running total
        # # return (total modulo sizeOfHashTable)   modulo is '%' in Python.

    def printHash(self):
        for nums in self.myList:
            print self.myList[nums]

def moves(pegs):
    moves = list()
    pegsList = list(pegs)
    
    for idx, peg in enumerate(pegsList):
        cpPegsList = pegsList
        currentPeg = int(pegsList[idx])
        # print idx, peg
        # nextPeg = int(pegsList[idx+1])
        # if (idx+2 < len(pegsList)):
        #     nextnextPeg = int(pegsList[idx+2])
        # if (idx-2 >= 0):
        #     previousPreviousPeg = int(pegsList[idx+2])    

        # previousPeg = int(pegsList[idx-1])
        # previousPreviousPeg = int(pegsList[idx-1])


        if (currentPeg == 0): #can't move a double peg
            if (idx - 3 >= 0): ## not out of bounds to the left
                if (int(pegsList[idx-3]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx-1]) + int(pegsList[idx-2]) == 0): # jumped over 2 single pegs peg to the direct left
                        print idx, "jumped over two single pegs to the left"
                        del cpPegsList[idx]
                        cpPegsList[idx-3]= int(cpPegsList[idx-3])+1
                        moves.append(cpPegsList)
                        cpPegsList = pegsList

            if (idx - 2 >= 0): ## not out of bounds to the left
                if (int(pegsList[idx-2]) == 0):  # needs to land on a single peg
                    if (int(pegsList[idx-1]) == 1): # jumped over the a double peg to the direct left
                        print idx, "valid move, record this"
                        del cpPegsList[idx]
                        cpPegsList[idx-2]= int(cpPegsList[idx-2])+1
                        moves.append(cpPegsList)
                        cpPegsList = pegsList

        print idx, peg
    print "Moves: " + str(moves)
    return pegsList


# def is_solved ( pegs, hashtable T) 
#    # if (t.search(p)) return false 
#    for m in moves(p)){ //where moves p is an array that returns all possible moves
#         if (is_solved(m)) return true;
#         print (p);//prints in reverse so would use a stack to print in reverse order
#    }
#    t.insert(p)
#    return fasle


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
    
    (options, args) = parser.parse_args()
    
    if (options.filename == "True"):
        converted_board = getInput()
    elif options.verbose: 
            print "reading %s..." % options.filename
            f = open(options.filename, 'r')
            converted_board = f.read().strip().upper().replace('X', '1').replace('|', '0').replace(" ", "")

    print "board =", converted_board
    # print int(converted_board, 2)
    print moves(converted_board)
    # t = HashTable()
    # t.set(5,7)
    # t.printHash()
    # print "t.i:"
    # print t.myList
    # print "t.set_instance:"
    # print t.set_instance(5,"yo")
    # print t.get_instance_i()
    # print t.myList
    # t.set(6,"yo")
    # print t.myList
    # print t.get(5)


if __name__ == "__main__":
    main()