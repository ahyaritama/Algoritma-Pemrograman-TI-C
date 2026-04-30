# === BAGIAN A ===


"""
Menentukan pemenang berdasarkan pilihan
dari pemain dan komputer
"""
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    hasil = ""
    if pilihan_pemain == pilihan_komputer:
        hasil = "seri"
    else:
        if ((pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or
            (pilihan_pemain == "kertas" and pilihan_komputer == "batu") or
            (pilihan_pemain == "batu" and pilihan_komputer == "gunting")
        ):
            hasil = "pemain"
        else:
            hasil = "komputer"
    
    return hasil


"""
Memainkan giliran dalam satu ronde, mengembalikan
hasil berupa "pemain", "seri", "komputer"
"""
def main_satu_giliran(nomor_giliran):
    DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    pilihan_pemain = ""

    while True:
        pilihan_pemain = input("Masukkan pilihanmu (batu | gunting | kertas): ")
        if pilihan_pemain.lower() not in ["batu", "gunting", "kertas"]:
            print("Pilihan tidak valid!")
            pass
        else:
            break
    
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print(f"\nPilihan Komputer: {pilihan_komputer}\nHasil: {hasil + " menang" if hasil != "seri" else hasil}\n")

    return hasil


"""
Memainkan satu ronde permainan yang akan
berhenti saat ada tiga kemenangan diraih
"""
def main_satu_ronde(nama, nomor_ronde):
    pemain_menang = 0
    komputer_menang = 0
    nomor_giliran = nomor_ronde

    while (pemain_menang < 3 and komputer_menang < 3):
        hasil = main_satu_giliran(nomor_giliran)
        if hasil == "pemain":
            pemain_menang += 1
        elif hasil == "komputer":
            komputer_menang += 1
        nomor_giliran += 1
    
    return [nama, pemain_menang * 10]


# === BAGIAN B ===

"""
Menampilkan riwayat dari permainan
"""
def tampilkan_riwayat(riwayat):
    if len(riwayat) == 0:
        print("Belum ada riwayat")
        return
    
    print("Riwayat Permainan")
    print("+-------+--------------+----------+")
    print("| Nomor |     Nama     |   Skor   |")
    print("+-------+--------------+----------+")

    for i in range(len(riwayat)):
        print(f"| {f"{i + 1}.":<5} | {riwayat[i][0]:<12} | {riwayat[i][1]:<8} |")
    
    print("+-------+--------------+----------+")



# === BAGIAN C ===

"""
Melakukan pengurutan poin dari yang
terbesar ke yang terkecil
"""
def bubble_sort_riwayat(riwayat):
    riwayat_copy = riwayat.copy()
    n = len(riwayat_copy)

    for i in range(n):
        for j in range(n - 1 - i):
            if riwayat_copy[j][1] < riwayat_copy[j + 1][1]:
                riwayat_copy[j], riwayat_copy[j + 1] = riwayat_copy[j + 1], riwayat_copy[j]
    
    return riwayat_copy


"""
Menampilkan leaderboard yang sudah
diurutkan dari poin terbesar hingga
poin terkecil
"""
def tampilkan_leaderboard(riwayat):
    new_riwayat = bubble_sort_riwayat(riwayat)
    
    print("Leaderboard")
    print("+-------+--------------+----------+")
    print("| Nomor |     Nama     |   Skor   |")
    print("+-------+--------------+----------+")

    for i in range(len(new_riwayat)):
        print(f"| {f"{i + 1}.":<5} | {new_riwayat[i][0]:<12} | {new_riwayat[i][1]:<8} |{" *" if i == 0 else ""}")
    
    print("+-------+--------------+----------+")


# === PROGRAM UTAMA ===

def main():
    nomor_ronde = 0
    riwayat = []
    
    while True:
        nama_pemain = input("Masukkan nama pemain: ")
        hasil = main_satu_ronde(nama_pemain, nomor_ronde)
        riwayat.append(hasil)
        nomor_ronde += 1
        main_lagi = input("Main lagi? (y/n): ")
        print("========================================")
        if main_lagi.lower() != "y":
            break
    
    tampilkan_riwayat(riwayat)
    print()
    tampilkan_leaderboard(riwayat)


if __name__ == "__main__":
    main()