def load_data(data,es,index='test index',doc_type='parking_tickets'):
	"""load data into ESearch"""
	for i in range(len(data)):
		es.index(body=data[i], index=index, doc_type=doc_type, id=i)

	return es