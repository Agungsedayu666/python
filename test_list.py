# Membuat List Python
print("\n====MEMBUAT LIST PYTHON====")
list1 = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 2010, 2013, 2016, 2019, 2022 ]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("data : ",list1)
print("data : ",list2)
print("data : ",list3)

# Akses Nilai Dalam List Python
print("\n====AKSES NILAI DALAM LIST PYTHON====")
print("list1[0]  : ",list1[0])
print("list2[1:5]: ",list2[1:5])
print("list3[3]  : ",list3[3])

# Update Nilai Dalam List Python
print("\n====UPDATE NILAI DALAM LIST PYTHON====")
print("Nilai awal pada index 2 : ", list1[2])

list1[2] = 2023
print("Nilai baru pada index 2 : ", list1[2])

# Hapus Nilai Dalam List Python
print("\n====HAPUS NILAI DALAM LIST PYTHON====")

del(list2[-1]) # hapus nilai terakhir dari list python
print('List sekarang adalah ', list2 )

# Operasi Dasar Pada List Python
print("\n=====OPERASI DASAR PADA LIST PYTHON======")
# Menghitung Jumlah Elemen dalam List Python
jumlah_elemen=len(list1)
print ("Jumlah elemen yang ada pada list1 :", jumlah_elemen)

# Indexing, Slicing dan Matrix Pada List Python
# Karena list adalah urutan, pengindeksan dan pengiris bekerja dengan cara yang sama untuk list seperti yang mereka lakukan untuk String
print("\n======INDEXING,SLICING DAN MATRIX PADA LIST PYTHON========")
# Indexing (Mencari data berdasarkan indeksnya)
print("Data ke-2 di list3          :", list3[1])
# Slicing (Memotong data dengan cara menentukan batasnya)
print("Data antara index 2 sampai 5:", list3[2:5])
# Slicing (mendapatkan beberapa data dengan menggunakan rentang indeks)
print("Dua sampai tiga di list3    :", list3[:3])
# Matrix (memasukan multi dimensi array atau matriks)
matrik=[
    ['A','B'],
    ['C','D']
    ];
print('Matrixnya adalah\n', matrik);















