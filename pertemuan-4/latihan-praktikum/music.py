music_donwloaded = [
    "Twinkle Twinkle Little Star",
    "Counting Stars",
    "Badak dan Ikan",
    "Payphone",
    "Safe and Sound"
]

for x, y in enumerate(music_donwloaded):
    print(f"[{x + 1}] {y}")

try:
    song = int(input("\nPilih musik untuk diputar: "))
    print(f"Memutar {music_donwloaded[song - 1]}")
except ValueError:
    print("Masukkan angka!")
except IndexError:
    print(f"Lagu tidak ditemukan! Pilih 1-{len(music_donwloaded)}")
except KeyboardInterrupt:
    print()
    pass