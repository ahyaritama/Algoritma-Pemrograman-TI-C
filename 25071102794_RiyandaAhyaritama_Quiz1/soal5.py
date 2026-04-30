class Buku:
    def __init__(self, judul, denda):
        self.judul = judul
        self.denda = denda

    def tampilkan(self):
        print(f"{self.judul} - Denda Rp {self.denda}/hari")

class Peminjaman:
    total_denda = 0
    
    def tambah(self, buku, terlambat):
        self.denda_total += terlambat * buku.denda

    def ringkasan(self):
        print(self.denda_total)


def main():
    buku = [Buku("Aljabar", 2500), Buku("Kalkulus", 3000), Buku("Pemrograman", 2000)]

    for i in buku:
        print(i)

    pinjam = Peminjaman()
    print("[1] Aljabar\n[2] Kalkulus\n[3] Pemrograman")
    judul = input("Masukkan pilihan buku: ")
    terlambat = input("Masukkan keterlambatan: ")
    pinjam.tambah(buku[judul - 1], terlambat)
    pinjam.ringkasan()

main()