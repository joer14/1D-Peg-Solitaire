# import sys, getopt
# from optparse import OptionParser

# #input_board = raw_input("Enter board:")
# #print "raw_input =", str1

from optparse import OptionParser
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
        getInput()
    elif options.verbose: 
            print "reading %s..." % options.filename
  
def getInput():
	input_board = raw_input("Enter board:")
	print "raw_input =", input_board
            

if __name__ == "__main__":
    main()