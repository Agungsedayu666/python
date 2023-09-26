# Tugas komparasi dan logika


# -----0+++++5-----8+++++11-----
inputUser = float(input("Masukan angka yang bernilai\nLebih dari 0 \ndan \nKurang dari 5 \natau \nLebih dari 8 \ndan \nKurang dari 11 :"))

# -----0+++++
# Memeriksa angka lebih dari 0
isLebihDari = (inputUser > 0)
print("Lebih dari 0 =", isLebihDari)

# +++++5-----
# Memeriksa angka kurang dari 5
isKurangDari = (inputUser < 5)
print("Kurang dari 5 =", isKurangDari)

# -----8+++++
# Memeriksa angka lebih dari 8
isLebihDari = (inputUser > 8)
print("Lebih dari 8 =", isLebihDari)

# +++++5-----
# Memeriksa angka kurang dari 11
isKurangDari = (inputUser < 11)
print("Kurang dari 11 =", isKurangDari)

# -----0+++++5-----8+++++11-----
isCorrect = isLebihDari and isKurangDari
print("Angka yang anda masukan :", isCorrect)

print("\n",10*"=","\n")
# +++++0-----5+++++8-----11+++++
inputUser = float(input("Masukan angka yang bernilai\nKurang dari 0 \natau \nLebih dari 5 \ndan \nKurang dari 8 \natau \nLebih dari 11 :"))

# +++++0-----
# memeriksa angka kurang dari 0
isKurangDari = inputUser < 0
print("Kurang dari 0 =", isKurangDari)

# -----5+++++
# memeriksa angka Lebih dari 5
isLebihDari = inputUser > 5
print("Lebih dari 5 =", isLebihDari)

# +++++8-----
# memeriksa angka Kurang dari 8
isKurangDari = inputUser < 8
print("Kurang dari 8 =", isKurangDari)
# -----11+++++
# memeriksa angka Lebih dari 11
isLebihDari = inputUser > 11
print("Lebih dari 11 =", isLebihDari)

# +++++0-----5+++++8-----11+++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan :", isCorrect)


