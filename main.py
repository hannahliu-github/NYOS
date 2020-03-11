# import list of command line arguments
from sys import argv
from elasticsearch import   Elasticsearch


# import interface to API
from src.get_data import get_parking_tickets
# import interface to elasticsearch
from src.load_es import load_data

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
    data = get_parking_tickets(page_size,num_pages,output)

    # create Elasticsearch and load data
    es = Elasticsearch()

    """def load_data(data,es,index='test index',doc_type='parking_tickets')"""
    es = load_data(data,es,index='haha',doc_type='hey')

    # test query by id
    #res = es.get(id=1,index='haha',doc_type='hey')
    #print(res['_source'])
