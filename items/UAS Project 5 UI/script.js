// 1. Ambil semua elemen tombol
const buttons = document.querySelectorAll('.login-submit, .register-submit, .btn-submit, .btn-report');

// 2. Pasang fungsi ke setiap tombol
buttons.forEach(function(button) {
    
    // Efek saat tombol ditekan (Mengecil)
    button.addEventListener('mousedown', function() {
        this.style.transform = "scale(0.95)";
    });

    // Efek saat tombol dilepas (Kembali Normal)
    button.addEventListener('mouseup', function() {
        this.style.transform = "scale(1)";
    });

    // Efek Ripple (Ombak Putih) saat diklik
    button.addEventListener('click', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        
        this.appendChild(ripple);

        // Hapus elemen ripple setelah animasi selesai
        setTimeout(function() {
            ripple.remove();
        }, 600);
    });
}); // <--- Ini penutup forEach yang benar