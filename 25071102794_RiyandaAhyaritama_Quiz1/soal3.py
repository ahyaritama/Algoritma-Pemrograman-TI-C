def lihat_buku(daftar_buku):
    for i, buku in enumerate(daftar_buku):
        print(f"[{i + 1}] {buku[0]} | {buku[1]}")
    
    num = input("\nMasukkan nomor buku: ")
    if num in [str(i) for i in range(1, len(daftar_buku) + 1)]:
        return daftar_buku[int(num) - 1]
    elif num == "0":
        return False
    else:
        print("Nomor buku yang dimasukkan tidak valid!")
        return None

def pinjam_buku(daftar_buku):
    buku_pinjaman = []
    while True:
        data_buku = lihat_buku(daftar_buku)
        if data_buku:
            print(f"Buku {data_buku[0]} berhasil dipinjam.")
            buku_pinjaman.append(data_buku)
        elif data_buku == False:
            break
        print()
    return buku_pinjaman

def cek_denda(daftar_buku):
    buku_pinjaman = pinjam_buku(daftar_buku)
    while True:
        try:
            telat = int(input("Masukkan hari keterlambatan: "))
        except ValueError:
            print("Silahkan masukkan angka!")
            pass
        
        if telat < 0:
            print("Silahkan masukkan angka keterlambatan!")
            pass

        return sum(i[1] for i in buku_pinjaman) * telat



def main():
    daftar_buku = [["Algoritma", 2000],
                   ["Basis Data", 2500],
                   ["Statistika", 2000],
                   ["Aljabar", 2500],
                   ["Kalkulus", 25000]]
    
    denda = cek_denda(daftar_buku)
    if denda == 0:
        print("Tidak ada denda")
    else:
        print(f"Total denda Anda: Rp {denda}")

if __name__ == "__main__":
    main()