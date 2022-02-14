import yfinance as yf
import matplotlib as plt

class fund:

    """
    fund - The class fund is a parent for the stock, bond, index and similar classes. 

    Attributes: 3 - string self.name, string self.code, string self.source, string self.info, yfinance.Ticker self.ticker, * self.history
    
    string self.name - user generated name
    string self.code - code for fund (ISIN, yahoo, etc...)
    string self.source - where to get data from (yahoo, etc...  see list for more details)
    string self.info - info about the fund
    yfinance.Ticker self.ticker =  an optional value for a yfinance yahoo ticker
    dict self.history - the history of the fund {date: price}
    """

    def __init__(self, name, code, source):
        """
        __init__ - Initializer function for fund
        
        Arguments: 3 - string name, string code, string source

        string name - user generated name
        string code - code for fund (ISIN, yahoo, etc...)
        string source - where to get data from (yahoo, etc...  see list for more details)
        """

        self.name = name                            ## Assign variables
        self.code = code
        self.source = source

        if (source == "yahoo"):                     ## If the source is yahoo
            self.ticker = yf.Ticker(code)           ## Create the ticker
            self.info = self.ticker.info            ## Get the information about the ticker
            self.history = [float(x) for x in self.ticker.history(period="max", interval="1d")["Open"] if str(x) != "nan"]      ## Get the history of the fund