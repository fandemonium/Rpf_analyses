import sys

d = {}
for lines in open(sys.argv[1]):
	lexemes=lines.strip().split("\t")
	query_id = lexemes[0]
	hit_id = lexemes[1]
	percent_identity = float(lexemes[3])
	if hit_id not in d:
		d[hit_id] = {query_id: percent_identity}
	else:
		d[hit_id].update({query_id: percent_identity})

for hit in d:
	if len(d[hit]) > 1:
#		print d[hit]
		best_query = max(d[hit], key=d[hit].get)
		print best_query + "\t" + hit + "\t" + str(d[hit][best_query]) 	
	else:
		for query in d[hit]:
			print query + "\t" + hit + "\t" + str(d[hit][query])	
