struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for v in folder.values():
        if type(v) == int:
            total += v
        else:
            total += total_ukuran(v)

    return total

def hitung_file(folder: dict) -> int:
    total = 0
    for v in folder.values():
        if type(v) == int:
            total += 1
        else:
            total += hitung_file(v)

    return total

def cari_terbesar(folder: dict) -> tuple:
    terbesar = (0, 0)
    for k, v in folder.items():
        if type(v) == int:
            if v > terbesar[1]:
                terbesar = (k, v)
        else:
            terbesar = cari_terbesar(v)

    return terbesar

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    for k, v in folder.items():
        if type(v) == int:
            print(f"{" " * level}📄 {k} ({v} KB)")
        else:
            print(f"{" " * level}📁 {k}")
            tampilkan_tree(v, nama, level + 4)

def main():
    print(f"Total ukuran skripsi: {total_ukuran(struktur)} KB")
    print(f"Jumlah file: {hitung_file(struktur)} file")

    terbesar = cari_terbesar(struktur)
    print(f"File terbesar: {terbesar[0]} ({terbesar[1]} KB)")

    print()     
    tampilkan_tree(struktur)

if __name__ == "__main__":
    main()