a = 4
b = 5

hasil = a <= b
print("lebih dari sama dengan : ",hasil)


x = 5
y = 6
print("nilai x = ",x, "id = ",hex(id(x)))
print("nilai y = ",y, "id = ",hex(id(y)))
hasil = x is y
print("hasil dari x is y = ",hasil)

c = 25
d = 25
print("nilai c = ",c, "id = ",hex(id(c)))
print("nilai d = ",d, "id = ",hex(id(d)))
hasil = c is not d
print("hasil dari c is not d = ",hasil)
