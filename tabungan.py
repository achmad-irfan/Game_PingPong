class akun:
    def __init__(self, nama,rekening, saldo=0):
        self.pemilik=nama
        self.rekening= rekening
        self.__saldo=saldo # Private
    
    def __repr__(self):
        return f"Pemilik {self.pemilik} dengan nomer {self.rekening}"
    
    @property
    def info(self):
        return self.__saldo
    
    def setor(self,setor):
        if setor>0:
            self.__saldo +=setor
        else:
            print("Masukan uang dengan benar")
            
    def tarik(self,tarik):
        if 0 < tarik <= self.__saldo:
            self.__saldo -= tarik
        else:
            print("Uang Tidak Cukup")
            
    def tambah_saldo(self,nominal):
        self.__saldo += nominal
    
    def transfer(self, tujuan,nominal):
        if 0< nominal <= self.__saldo:
            self.__saldo-=nominal
            tujuan.tambah_saldo(nominal)
        else:
            print("Uang tidak cukup")
        

# class tabungan(akun):
#     def __init__(**kwargs):
#         super().init()
        
#     def buat_akun(self,nama,nomer,saldo_awal):
#         akun=tabungan(nama,nomer,saldo_awal)
#         self.list_nasabah.append(akun) 
#         return akun   
    
#     def cari_nama(self,nomer_rekening):
#         for nomer in self.list_nasabah:
#             if nomer.rekening==nomer_rekening:
#                 return nomer


akun1= akun("Irfan",2230987,100000)
akun2= akun("Tessa",2230933,400000)   
akun3= akun("Mikki",2235666,50000)
akun4= akun("Santi",2230912,900000)
akun5= akun("Ratna",2230944,30000)  
                

print(akun1)

