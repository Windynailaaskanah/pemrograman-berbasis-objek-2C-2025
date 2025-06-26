from tunai import PembayaranTunai
from kartukredit import PembayaranKartukredit
from Dompetdigital import EWallet

def main():
    print("=== Pembayaran ===")
    try:
        harga = float(input("Masukkan harga barang (Rp): "))
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    print("\nPilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. E-Wallet")
    
    metode = input("Masukkan pilihan (1/2/3): ")

    if metode == "1":
        pembayaran = PembayaranTunai(harga)
    elif metode == "2":
        pembayaran = PembayaranKartukredit(harga)
    elif metode == "3":
        pembayaran = EWallet(harga)
    else:
        print("Pilihan tidak valid.")
        return

    pembayaran.bayar()

main()
