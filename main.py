import subprocess
import sys


def menu_utama():
    while True:
        print("\n" + "=" * 42)
        print(" APLIKASI PORTOFOLIO CRYPTO & UANG ".center(42, "="))
        print("=" * 42)
        print("1. Tambah Transaksi")
        print("2. Tampilkan Portofolio")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            subprocess.run([sys.executable, "tambah_transaksi.py"])
        elif pilihan == "2":
            subprocess.run([sys.executable, "tampil_portofolio.py"])
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()
