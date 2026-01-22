# fikti-cari

#FiktiCari - Sistem Informasi Lost & Found Kampus

FiktiCari adalah aplikasi berbasis web untuk membantu mahasiswa melaporkan dan mencari barang yang hilang di lingkungan Fakultas. Aplikasi ini menggantikan cara manual (grup chat) dengan sistem terpusat yang terintegrasi.

## Demo Tampilan
![Halaman Beranda](link_gambar_beranda.png)

##  Fitur Utama
* **Lapor Temuan:** User bisa upload foto barang, lokasi, dan deskripsi.
* **Pencarian Cerdas:** Filter barang berdasarkan nama atau lokasi.
* **Integrasi WhatsApp:** Tombol "Hubungi" langsung mengarah ke chat WA penemu.
* **Autentikasi:** Sistem Login/Register dan proteksi halaman lapor.
* **Status Barang:** Label otomatis untuk barang Hilang vs Ditemukan.

## Teknologi yang Digunakan
* **Backend:** Python, Django Framework
* **Frontend:** HTML5, CSS3, JavaScript (Custom Design)
* **Database:** SQLite
* **Styling:** Responsive UI dengan Dark Mode Support

## Cara Instalasi (Local)
1. Clone repository ini.
2. Buat virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Jalankan migrasi: `python manage.py migrate`
5. Jalankan server: `python manage.py runserver`
