from sodapy import Socrata
import os

APP_KEY = os.environ['APP_KEY']
API_BASE = "data.cityofnewyork.us"
dataSetID = "nc67-uf89"

def get_parking_tickets(page_size, num_pages=None, output=None):
    """Request parking ticket data and save in output_folder."""

    # Start connection to data API
    client = Socrata(
    API_BASE,
    APP_KEY)
    
    # get the maximum number of rows in the data set
    max_rows = client.get(dataSetID, select = 'COUNT(*)')
    max_rows = int(max_rows[0]['COUNT'])
    
    # find the maximum number of pages required to read all of the data
    max_num_pages = max_rows / page_size
    if max_rows % page_size > 0:
        max_num_pages += 1
    
    # If num_pages is blank, read max_num_pages
    if num_pages == None:
        num_pages = max_num_pages
    
    data = []
    # for each page
    for i in range(num_pages):
        try:
            # we use a try except because of time out errors when the offset is very large
            data += client.get(dataSetID, limit=page_size, offset=i*page_size)
        except:
            break
    
    # Output the data
    if output == None:
        # print to stdout
        print(data)
    else:
        with open(output,'w') as outputFile:
            outputFile.write('[')
            for line in data[:-1]:
                outputFile.write(str(line)+',\n')
                
            # write the last line without a comma
            outputFile.write(str(data[-1])+']')
    
    return data