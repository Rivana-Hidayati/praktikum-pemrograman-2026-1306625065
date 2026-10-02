5. Print-Out Coding

# Program Konversi Suhu Celcius - Reamur - Fahrenheit

# Header dan Input Identitas
print ("Program Konversi Suhu")
print ("Nama \t : Rivana Hidayati")
print ("NIM \t : 1306625065")
print ()

# Input Parameter Suhu
suhu_awal  = int(input("Suhu awal \t: "))
suhu_akhir = int(input("Suhu akhir \t: "))
selang     = int(input("Selang \t: "))
print ()

# Header Tabel
print("TABEL KONVERSI")
print('=' * 47)
print(f"| {'No.': <4} | {'Celcius':10} | {'Reamur': <10} | {'Fahrenheit': <10} |")
print('=' * 47)

# Insialisasi Variabel Perulangan
c  = suhu_awal
no = 1

# Perulangan while untuk Perhitungan & Cetak Format Tabel
while c <= suhu_akhir:
  r = 0.8 * c
  f = (1.8 * c) + 32

  # Cetak baris tabel dengan format rapi
  print(f"| {no:<4} | {c: <10.1f} | {r:<10.1f} | {f:<10.1f} |")

  c += selang
  no += 1

# Membuat Garis Penutup paling Bawah
print('=' * 47)

print()
print("Selesai")


