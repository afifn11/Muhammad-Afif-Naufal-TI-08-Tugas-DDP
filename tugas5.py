print("Buatlah program python dengan list, dengan nilai (kode kendaraan, nama kendaraan, cc kendraan, warna kendaraan")
a = ["B 444 U", "xmax", "250 cc", "Biru"]

a.append("Rp 35000000")
a.append("roda 2")
a.insert(2,"yamaha")
a.insert(3,"motor")

print(a)

#Buat program dengan bahasa python dengan match case untuk menghitung luas bangun datar

print("Buat program dengan bahasa python dengan match case untuk menghitung luas bangun datar")
import math

pilihan = input("Masukkan nomor atau nama bangun datar: ")

match pilihan:
    case "1" | "persegi":
        s = int(input("Masukkan panjang sisi: "))
        l_persegi = s * s
        print(f"Luas persegi adalah {l_persegi}")
    case "2" | "lingkaran":
        r = int(input("Masukkan jari-jari: "))
        l_lingkaran = math.pi * r * r
        print(f"Luas lingkaran adalah {l_lingkaran}")
    case "3" | "segitiga":
        a = int(input("Masukkan alas: "))
        t = int(input("Masukkan tinggi: "))
        l_segitiga = 0.5 * a * t
        print(f"Luas segitiga adalah {l_segitiga}")
    case _:
        print("Pilihan tidak valid.")
