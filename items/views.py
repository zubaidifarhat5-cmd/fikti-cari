from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout # <--- Import baru
from django.contrib.auth.models import User # <--- Import baru
from django.contrib import messages # <--- Untuk pesan error/sukses
from .models import Barang
from .form import BarangForm
from django.db.models import Q
# Create your views here.

def beranda(request):
    query = request.GET.get('q')
    data_barang = Barang.objects.all().order_by('-tanggal_posting')
    if query:
        data_barang = data_barang.filter(
            Q(nama_barang__icontains=query) |
            Q(lokasi__icontains=query) 
            

        )

    context = {
        'data_barang' : data_barang,
        'query' : query
    }

    return render(request, 'items/beranda.html', context)
    # return render(request, 'items/webuas.html', context)

@login_required(login_url='/admin/login/') # Jika belum login, lempar ke login admin dulu
def lapor_barang(request):
    if request.method == 'POST':
        # Jika user klik tombol Submit
        form = BarangForm(request.POST, request.FILES) # request.FILES wajib untuk upload gambar
        if form.is_valid():
            barang = form.save(commit=False) # Tahan dulu, jangan simpan ke DB
            barang.user = request.user       # Isi kolom user dengan user yang sedang login
            barang.save()                    # Baru simpan permanen
            return redirect('beranda')       # Kembali ke halaman depan
    else:
        # Jika user baru membuka halaman (GET)
        form = BarangForm()

    return render(request, 'items/form_lapor.html', {'form': form})

# --- LOGIKA REGISTER ---
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username'] # NPM
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password'] # Sesuaikan name di HTML

        # Cek apakah password cocok
        if password != confirm_password:
            messages.error(request, 'Password tidak cocok!')
            return redirect('register')
        
        # Cek apakah username sudah ada
        if User.objects.filter(username=username).exists():
            messages.error(request, 'NPM / Username sudah terdaftar!')
            return redirect('register')

        # Buat User Baru
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, 'Registrasi berhasil! Silakan login.')
        return redirect('login')

    return render(request, 'items/register.html')

# --- LOGIKA LOGIN ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('beranda')
        else:
            messages.error(request, 'Username atau Password salah!')
            return redirect('login')

    return render(request, 'items/login.html')

# --- LOGIKA LOGOUT ---
def logout_view(request):
    logout(request)
    return redirect('beranda')