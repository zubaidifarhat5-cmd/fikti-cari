from django.contrib import admin
from .models import Barang

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    # Menampilkan kolom-kolom ini di tabel list (halaman depan admin)
    list_display = ('nama_barang', 'jenis', 'lokasi', 'tanggal_posting', 'sudah_selesai')
    
    # Menampilkan tanggal di dalam form detail sebagai "hanya baca"
    readonly_fields = ('tanggal_posting',)

admin.site.register(Barang, BarangAdmin)