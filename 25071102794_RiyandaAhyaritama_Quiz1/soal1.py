def lihat_buku(daftar_buku):
    for i, buku in enumerate(daftar_buku):
        print(f"[{i + 1}] {buku[0]} | {buku[1]}")
    
    num = input("\nMasukkan nomor buku: ")
    if num in [str(i) for i in range(1, len(daftar_buku) + 1)]:
        print(f"Nama Buku: {daftar_buku[int(num) - 1][0]}")
        print(f"Denda Keterlambatan/Hari: {daftar_buku[int(num) - 1][1]}")
    else:
        print("Nomor buku yang dimasukkan tidak valid!")
        
def main():
    daftar_buku = [["Algoritma", 2000],
            ["Basis Data", 2500],
            ["Statistika", 2000],
            ["Aljabar", 2500],
            ["Kalkulus", 25000]]
    lihat_buku(daftar_buku)


if __name__ == "__main__":
    main()