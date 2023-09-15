# Tipe data adalah suatu media atau memori pada komputer yang digunakan untuk menampung informasi
# a = 10, a adalah variabel dengan nilai 10

# integer (Menyatakan bilangan bulat)
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# float (Menyatakan bilangan yang mempunyai koma)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# string (Menyatakan karakter/ kalimat bisa berupa huruf angka, dll (diapit tanda " atau '))
data_string = "camvhell 666"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# boolean (Menyatakan benar = True yang bernilai 1, atau salah = False yang bernilai 0)
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

# complex (Menyatakan pasangan angka real dan imajiner)
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# list (Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah)
data_list = ['kimia', 'fisika', 1993, 2017]
print("data : ",data_list)
print("- bertipe : ",type(data_list))
# tipe data dari bahasa C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))