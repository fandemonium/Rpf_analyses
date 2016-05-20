import sys

genecart = sys.argv[1]

query_id = genecart.split("_")[1]

for n, lines in enumerate(open(genecart, 'rU')):
	if n == 0:
		continue
	else:
		lexemes = lines.strip().split("\t")
		gene_id = lexemes[0]
		genome_id = lexemes[3]
		genome_name = lexemes[4]
		strand = lexemes[-2]
		print "%s\t%s\t%s\t%s\t%s" % (query_id, gene_id, genome_id, genome_name, strand)


