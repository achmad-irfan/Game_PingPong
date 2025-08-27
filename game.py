# # class character:
# #     _total=[]
    
# #     def __init__(self, name, hp, attack):
# #         self.name=name
# #         self.hp=hp
# #         self.attack=attack
# #         character._total.append(self)
    
# #     def __str__(self):
# #         return f"Nama : {self.name} | Hp : {self.hp} | Attack : {self.attack}"
    

# # irfan = character("irfan",89,22)
# # laras = character("laras",66,33)
# # cinta = character("cinta",88,22)
# # dana = character("dana",88,10)
# # ani = character("ani",99,18)

# print(len(character._total))

class A:
    def __init__(self, name,saldo):
        self.name=name
        self.__saldo=saldo
    
    def __str__(self):
        return f"nama pemilik {self.name}"
    
    @property
    def getSaldo(self):
        return self.__saldo
    
    @getSaldo.setter
    def ubah(self,jumlah):
        self.__saldo += jumlah
        print(f"{self.__saldo}")
# class B:
#     pass

# class C(B,A):
#     pass

Ob1= A("Iga",2000)


class MathHelper:
    def tambah(a, b):   # ga pakai self
        return a + b

print(Ob1.name)