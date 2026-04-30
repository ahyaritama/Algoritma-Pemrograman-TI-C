def rekap_buku():
    minggu = int(input("Masukkan Jumlah Minggu: "))
    kategori = int(input("Masukkan Jumlah Kategori: "))
    rekap = [[0 for _ in range(kategori)] for _ in range(minggu)]
    for i in range(kategori):
        for j in range(minggu):
            rekap[i][j] = int(input(f"Masukkan total buku kategori {i + 1} minggu ke-{j + 1}: "))
    
    for i in range(len(rekap)):
        print(f"Jumlah Peminjaman Minggu ke-{i + 1}:", sum(rekap[i]))
    
    print("====================================")
    for i in range(len(rekap[0])):
        total = 0
        for j in range(len(rekap)):
            total += rekap[j][i]
        print(f"Jumlah Peminjaman Buku Kategori ke-{i + 1}:", total)



def main():
    daftar_buku = [["Algoritma", 2000],
                   ["Basis Data", 2500],
                   ["Statistika", 2000],
                   ["Aljabar", 2500],
                   ["Kalkulus", 25000]]
    rekap_buku()


if __name__ == "__main__":
    main()