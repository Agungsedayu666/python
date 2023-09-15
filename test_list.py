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
matrix=[['A','B'],
        ['C','D']]
print("Matrix:\n", matrix)
# Matriks (Menampilkan semua isinya)
matrik = [[list3[3]], # Offset mulai dari nol
          [list2[6]],
          [list1[4]],
          [list3[9]],
          [list2[5:]], # Slicing mengambil bagian
          [list1[-4]], # Negatif: hitung dari kanan
          [list1[2]],
          [list2[-7]],
          [list3[8:]],
          [list1[1]]
          ]
for row in matrik:
    print(*row," ")

# Method dan Fungsi Build-in Pada List Python
print("\n========METHOD DAN FUNGSI BUILD IN PADA LIST PYTHON===========")
# Append() digunakan untuk memasukkan item setelah akhir daftar.
list1.append([1,2,[3]])
print("Setelah append():\t", list1)
# Extend() digunakan untuk meletakkan satu iterable object di belakang lainnya.
list1.extend(['b', 'c'])
print("Setelah extend()\t", list1)
# Insert() digunakan untuk memasukkan item di posisi tertentu.
list1.insert(-1,'d')
print("Setelah insert()\t", list1)
# Remove() digunakan untuk menghapus suatu objek dari list.
list2.remove((3))   ## Hapus element pertama yaitu angka 0
del list2[::]       ### Hapus seluruh element
print("Setelah remove()/del:\t", list2)
















