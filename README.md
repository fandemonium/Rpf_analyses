# Rpf_analyses

Scripts for Rpf analyses

1. combining_genome_blast_results.py
```
for i in genomeBlast_*_results.xls; do python ~/Documents/repos/Rpf_analyses/combining_genome_blast_results.py $i > $i.new; done

cat *.xls.new > all_genome_balst_results.txt
```

2. combining gene card information (linking gene hits to genomes)
```
for i in GeneCart_*_results.xls; do python ~/Documents/repos/Rpf_analyses/combining_gene_carts.py $i; done >> all_gene_cart_results.txt 
```
