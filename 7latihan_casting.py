# latihan konversi satuan temperature

# program konversi satuan suhu ke satuan suhu lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

print("====CELCIUS====")
celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu dalam celcius adalah",celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

print("====REAMUR====")
reamur = float(input('Masukan suhu dalam reamur : '))
print("suhu dalam reamur adalah",reamur, "Reamur")

# celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah",celcius, "Celcius")

# fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

print("====FAHRENHEIT====")
fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# celcius
celcius = 5/9 * (fahrenheit - 32)
print("suhu dalam celcius adalah",celcius, "Celcius")

# reamur
reamur = 4/9 * (fahrenheit - 32)
print("suhu dalam reamur adalah",reamur, "Reamur")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

print("====KELVIN====")
kelvin = float(input('Masukan suhu dalam kelvin : '))
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

# celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius, "Celcius")

# reamur
reamur = 4/5 * (kelvin - 273)
print("suhu dalam reamur adalah",reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")