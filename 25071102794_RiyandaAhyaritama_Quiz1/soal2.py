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


def main():
    daftar_buku = [["Algoritma", 2000],
            ["Basis Data", 2500],
            ["Statistika", 2000],
            ["Aljabar", 2500],
            ["Kalkulus", 25000]]

    buku_pinjaman = pinjam_buku(daftar_buku)
    denda = 0
    print("Daftar Buku:")
    for i in buku_pinjaman:
        print(i[0])
        denda += i[1]
    print(f"Total denda keterlambatan satu hari: {denda}")


if __name__ == "__main__":
    main()