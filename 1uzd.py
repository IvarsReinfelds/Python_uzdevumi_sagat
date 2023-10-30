"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.
tuksa vardnica dict()
"""

class AAA:
    def __init__(self):
        self.rom_cip={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'

        }
    def uz_romu(self,num):
        rezult=""
        for value, sk in sorted(self.rom_cip.items(),key=lambda x:x[0],reverse=True):
            while num>=value:
                rezult+=sk
                num-=value
        return rezult
skaitlis=1984
convertet=AAA()
romu_sks=convertet.uz_romu(skaitlis)
print(f"{skaitlis}romiesu ciparos ir {romu_sks}")                