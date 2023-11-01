"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.

"""
def dubultot(skaitlis):
    return skaitlis * 2
 
saraksts = [1, 2, 3, 4, 5]
 
rezultats = map(dubultot, saraksts)
 
# Pārveidojam rezultātu sarakstā, lai to pārbaudītu
rezultata_saraksts = list(rezultats)
 
print(rezultata_saraksts)
