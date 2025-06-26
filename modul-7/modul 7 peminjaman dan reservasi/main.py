from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def main():
    print("=== Sistem Peminjaman & Reservasi Buku ===")
    nama = input("Masukkan nama Anda: ")

    print("\nPilih jenis buku:")
    print("1. Buku Fiksi")
    print("2. Buku Referensi")
    pilihan = input("Pilihan (1/2): ")

    judul = input("Masukkan judul buku: ")

    if pilihan == "1":
        buku = BukuFiksi(judul)
        aksi = input("Apa yang ingin Anda lakukan? (pinjam/reservasi): ").lower()
        if aksi == "pinjam":
            print(buku.pinjam(nama))
        elif aksi == "reservasi":
            print(buku.reservasi(nama))
        else:
            print("Aksi tidak dikenali.")
    elif pilihan == "2":
        buku = BukuReferensi(judul)
        aksi = input("Apa yang ingin Anda lakukan? (pinjam/reservasi): ").lower()
        if aksi == "pinjam":
            print(buku.pinjam(nama))
        elif aksi == "reservasi":
            print(buku.reservasi(nama))
        else:
            print("Aksi tidak dikenali.")
    else:
        print("Jenis buku tidak valid.")

main()
