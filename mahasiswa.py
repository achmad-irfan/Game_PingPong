class mahasiswa:
    list_mhs=[]
    def __init__ (self,nama,nim, jurusan,nilai):
        self.nama=nama
        self.nim=nim
        self._jurusan=jurusan
        self.__nilai=nilai
        mahasiswa.list_mhs.append(self)
        
    def get_nilai(self):
        return self.__nilai
    
    def grades(self):
        if self.nilai >= 85:
            grade= "A"
        elif self.nilai >= 70:
            grade= "B"
        elif self.nilai >=60:
            grade= "C"
        else:
            grade= "D"
        
        return grade
        
arhan = mahasiswa("Arhan","16003","Kedokteran",77)    
bella = mahasiswa("Bella","16004","Akutansi",50)    
cika = mahasiswa("Cika","16005","Matematika",97) 
dani = mahasiswa("Dani","16006","Psikologi",71) 
evan = mahasiswa("Evan ","16007","Sipil",47)   


# def statistic_class():
#     for mhs in mahasiswa.list_mhs:
#         status= "Lulus" if mhs.grades() in ["A","B"] else "Tidak Lulus"
#         print(f"Nama: {mhs.nama} | Nilai: {mhs.nilai} | Status: {status} | Grade: {mhs.grades()}")
#     jumlah_mhs= len(mahasiswa.list_mhs)
#     nilai= [point.nilai for point in mahasiswa.list_mhs]
#     rata_rata= sum(nilai)/len(nilai)
#     lulus= []
#     for n in nilai:
#         if n>60:
#             lulus.append(n)
#     tidak_lulus= jumlah_mhs-len(lulus)
    
#     # Summary
#     print(f"Jumlah Mahasiswa = {jumlah_mhs}")
#     print(f"Rata-rata = {rata_rata} ")
#     print(f"Jumlah lulus : {len(lulus)}")
#     print(f"Jumlah lulus : {tidak_lulus}")
    
#     # Ranking
#     ranking_list = sorted(mahasiswa.list_mhs, key=lambda m: m.nilai, reverse=True)
#     print("Ranking | Nama | Nilai | Grade")
#     for i, mhs in enumerate(ranking_list, start=1):
#         print(f"{i} | {mhs.nama} | {mhs.nilai} | {mhs.grades()}")
        

# statistic_class()
print(arhan.get_nilai())

