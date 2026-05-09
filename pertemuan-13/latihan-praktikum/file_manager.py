import os

def read():
    txt_files = [x for x in os.listdir() if x.endswith(".txt")]
    print("File tersedia:")
    for i, file in enumerate(txt_files):
        print(f"[{i + 1}] {file}")
    
    try:
        index = int(input("Pilih file (nomor): "))
        print(f"--- Isi {txt_files[index - 1]} ---")
        with open(txt_files[index - 1], "r") as f:
            print(f.read())
        print("--------------------")
    except IndexError:
        print("File yang dipilih tidak tersedia!")
    except:
        print("Indeks yang dimasukkan tidak valid!")


def write():
    txt_files = [x for x in os.listdir() if x.endswith(".txt")]
    print("File tersedia:")
    for i, file in enumerate(txt_files):
        print(f"[{i + 1}] {file}")

    user_input = input("Pilih file atau ketik nama file baru: ")
    try:
        index = int(user_input)
        f = open(txt_files[index - 1], "w")
    except:
        f = open(user_input, "w")
    
    text = input("Masukkan teks: ")
    f.write(text)
    f.close()


def delete():
    txt_files = [x for x in os.listdir() if x.endswith(".txt")]
    if len(txt_files) == 0:
        print("Tidak ada file .txt ditemukan.")
        return

    print("File tersedia:")
    for i, file in enumerate(txt_files):
        print(f"[{i + 1}] {file}")
    
    try:
        index = int(input("Pilih file (nomor): "))
        os.remove(txt_files[index - 1])
    except IndexError:
        print("File yang dipilih tidak tersedia!")
    except:
        print("Indeks yang dimasukkan tidak valid!")


def append():
    txt_files = [x for x in os.listdir() if x.endswith(".txt")]
    print("File tersedia:")
    for i, file in enumerate(txt_files):
        print(f"[{i + 1}] {file}")

    try:
        user_input = int(input("Pilih file (nomor): "))
        f = open(txt_files[index - 1], "a")
        text = input("Masukkan teks: ")
        f.write(text)
        f.close()
    except IndexError:
        print("File yang dipilih tidak tersedia!")
    except:
        print("Indeks yang dimasukkan tidak valid!")


def main():
    print("============================")
    print("PYTHON FILE MANAGER v1.0")
    print("============================")

    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[4] Append")
    print("[0] Exit")
    print("------------------------------")
    
    try:
        menu = input("Pilih menu: ")
        int_menu = int(menu)
        if int_menu == 1:
            read()
        elif int_menu == 2:
            write()
        elif int_menu == 3:
            delete()
        elif int_menu == 4:
            append()
    except:
        print()
        return

if __name__ == "__main__":
    main()