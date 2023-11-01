"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""



"""# Funkcija, kas atgriež atšķirību starp diviem elementiem
def find_difference(a, b):
    return a - b
 
# Sākotnējie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 4, 5, 6, 7]
 
# Izmantojot map(), izveidojam jaunu sarakstu ar atšķirībām
atšķirības = list(map(find_difference, saraksts1, saraksts2))
 
# Izdrukājam rezultātu
print(atšķirības)"""

# Funkcija, kas atgriež atšķirību starp divām virknēm
def find_string_difference(a, b):
    return f"Atšķirība starp '{a}' un '{b}': {a} - {b}"
 
# Sākotnējie saraksti ar virknēm
saraksts1 = ["apple", "banana", "cherry", "date", "elderberry"]
saraksts2 = ["banana", "date", "fig", "grape", "honeydew"]
 
# Izmantojot map(), izveidojam jaunu sarakstu ar atšķirībām
atšķirības = list(map(find_string_difference, saraksts1, saraksts2))
 
# Izdrukājam rezultātu
for atšķirība in atšķirības:
    print(atšķirība)