"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""

class Dati:
    def __init__(self, vards, vecums, summa):
       self.vards=vards
       self.vecums=vecums
       self.summa=summa

mans_dati = Dati('janis',30,500)


