"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.

map()

"""


saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
#sarakts2=[]

def pievienot(uzvards):
    return 'Dr. '+uzvards

saraksts2=list(map(pievienot,saraksts1))
print(saraksts2)