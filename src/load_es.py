import datetime


def dateConvert(dateString):
    """Convert a MM/dd/yyyy string to a datetime object."""
    x = dateString.split("/")
    
    month = int(x[0])

    date = int(x[1])

    year = int(x[2])

    return datetime.datetime(year, month, date, 0, 0)





def load_data(data,es,index='test index',doc_type='parking_tickets'):
	"""load data into ESearch"""
	for i in range(len(data)):
		# convert issue_date to datetime
		# data[i]["issue_date"] = ...
		data[i]["issue_date"]= dateConvert(data[i]["issue_date"])
		
		es.index(body=data[i], index=index, doc_type=doc_type, id=i)

	return es