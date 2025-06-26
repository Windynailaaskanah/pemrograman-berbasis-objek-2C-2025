from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def pilih_kendaraan():
    print("\n=== Pilih Jenis Kendaraan ===")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    if pilihan == "1":
        return Mobil()
    elif pilihan == "2":
        return Motor()
    elif pilihan == "3":
        return Sepeda()
    else:
        print("Pilihan tidak valid.")
        return None

def main():
    print("=== Sistem Pemesanan Kendaraan ===")
    nama = input("Masukkan nama Anda: ")
    try:
        usia = int(input("Masukkan usia Anda: "))
        durasi = int(input("Masukkan durasi sewa (jam): "))
    except ValueError:
        print("Usia dan durasi harus berupa angka.")
        return

    kendaraan = pilih_kendaraan()
    if kendaraan is None:
        return

    print("\n" + kendaraan.proses_pemesanan(nama, usia))
    if "berhasil" in kendaraan.proses_pemesanan(nama, usia):
        asuransi_input = input("Apakah Anda ingin menambah asuransi? (y/n): ").lower()
        biaya = kendaraan.hitung_biaya(durasi)
        if asuransi_input == 'y':
            biaya += kendaraan.tambah_asuransi()
            print("Asuransi ditambahkan.")
        print(f"Total biaya sewa: Rp{biaya}")
    print("Terima kasih telah menggunakan layanan kami.")

main()
