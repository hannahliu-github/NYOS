# import list of command line arguments
from sys import argv

# import interface to API
from src.get_data import get_parking_tickets

if __name__ == "__main__":
    
    # read the command line inputs from argv
    num_pages = None
    output = None

    # store command line inputs as variables
    for a in argv[1:]:
        param, val = a.split('=')
        if param == '--page_size':
            page_size = int(val)
        if param == '--num_pages':
            num_pages = int(val)
        elif param == '--output':
            output = val
        else:
            pass
    
    # get data from the API
    get_parking_tickets(page_size,num_pages,output)
    