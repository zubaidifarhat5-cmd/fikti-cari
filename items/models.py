from django.db import models
from django.contrib.auth.models import User

class Barang(models.Model):
    JENIS_LAPORAN_CHOICES =[
        ('KEHILANGAN', 'Saya Kehilangan Barang'),
        ('DITEMUKAN', 'Saya Menemukan Barang'), 
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    nama_barang = models.CharField(max_length=100)
    deskripsi = models.TextField(help_text="Ciri-ciri barang, warna, merek, dll.")
    lokasi = models.CharField(max_length=100, help_text="Lokasi hilang atau ditemukan (Cth: Gedung B, Kantin)")
    
    jenis = models.CharField(max_length=20, choices=JENIS_LAPORAN_CHOICES)
    
    # Foto bersifat opsional (blank=True)
    foto = models.ImageField(upload_to='gambar_barang/', blank=True, null=True)
    
    kontak_wa = models.CharField(max_length=20, help_text="Nomor WhatsApp yang bisa dihubungi")
    
    tanggal_posting = models.DateTimeField(auto_now_add=True)
    sudah_selesai = models.BooleanField(default=False, help_text="Centang jika barang sudah kembali/diambil")

    def __str__(self):
        return f"{self.get_jenis_display()} - {self.nama_barang}"
    
