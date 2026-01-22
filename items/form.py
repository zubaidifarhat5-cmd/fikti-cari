from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama_barang', 'jenis', 'lokasi', 'deskripsi', 'foto', 'kontak_wa']
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Kunci Motor Honda'}),
            'jenis': forms.Select(attrs={'class': 'form-select'}),
            'lokasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Parkiran Gedung B'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'kontak_wa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0812xxxx'}),
        }


