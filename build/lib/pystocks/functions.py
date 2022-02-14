def testFunction(printOutput, successString="") -> bool:
    """
    testFunction - A test function to check everything in the library is working. If it returns false, their are problems with the library setup
    
    Arguments: 2 - bool printOutput, string successString

    bool printOutput - should the function output anything to STDOUT
    string successString - the inputted stirng that will be displayed when the testFunction runs, if printOUtput is True
    """

    if printOutput:                                 ## If the printOutput is true
        print("Success - " + successString)         ## Output the successString, along with a Success predefiner
    
    return True                                     ## Return True, for programatical uses