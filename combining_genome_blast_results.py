import sys

gblast = sys.argv[1]
query_id = gblast.split("_")[1]
for n, lines in enumerate(open(gblast, 'rU')):
	if n == 0:
		continue
	else:
		lexemes = lines.strip().split("\t")
		hit_id = lexemes[0]
		product_name = lexemes[2]
		percent_identity = lexemes[3]
		genome_name = lexemes[-1]
		domain = lexemes[-3]
		bit_score = lexemes[-4]
		e_value = lexemes[-5]
		gene_len = lexemes[-6]
		print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(query_id, hit_id, product_name, percent_identity, gene_len, e_value, bit_score, genome_name, domain) 
	
