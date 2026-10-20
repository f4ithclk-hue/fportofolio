# Aplikasi Portofolio Crypto & Uang

Program sederhana untuk mencatat transaksi crypto dan uang menggunakan Python, PBO, dan CSV.

## File program
- `main.py`: menu utama.
- `models.py`: class `Transaksi` untuk menyimpan data transaksi.
- `tambah_transaksi.py`: memasukkan transaksi baru dan menyimpannya ke CSV.
- `tampil_portofolio.py`: menampilkan ringkasan dan riwayat transaksi.
- `transaksi.csv`: tempat penyimpanan data transaksi.

## Cara menjalankan
Buka folder ini di VS Code atau terminal, lalu jalankan:

```bash
python main.py
```

## Perbaikan
- Kolom tanggal memakai format `YYYY-MM-DD`, sehingga tahun ditampilkan juga.
- Tanggal boleh dikosongkan saat menambah transaksi; program akan memakai tanggal hari ini.
- Lebar kolom tabel dibatasi dan teks yang terlalu panjang dipotong agar tabel tetap rapi.

Data contoh di `transaksi.csv` bisa dihapus jika ingin mulai dari data kosong. Program ini hanya untuk pencatatan, tidak mengambil harga pasar real-time dan bukan saran investasi.
