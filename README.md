# SIMKOST Pro

> **SIMKOST Pro — Aplikasi Manajemen Kost, Kontrakan & Kamar Sewa Modern**  
> Sistem Pembukuan & Manajemen Kamar Kost Otomatis

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Theme: Emerald & Teal](https://img.shields.io/badge/Theme-Emerald%20&%20Teal-informational)](https://ram.ai.id)
[![Architecture: Standalone%20SPA](https://img.shields.io/badge/Architecture-Standalone%20SPA-success)](https://ram.ai.id)

---

## 🌟 Ikhtisar Aplikasi

**SIMKOST Pro** adalah software SaaS manajemen dan kasir modern yang dirancang khusus untuk mempermudah operasional harian bisnis Anda. Dilengkapi dengan antarmuka yang bersih (*Light Theme modern*), responsif di semua perangkat (Desktop, Tablet, dan Smartphone), serta modul **Smart Nota Otomatis** dengan upload logo toko dan cetak printer thermal (58mm/80mm).

### ✨ Fitur Utama
1. **Shell SaaS Terstandarisasi:**
   - Sidebar navigasi modern & responsif (drawer otomatis di mobile).
   - Topbar dengan pencarian instan (`Ctrl + K`), tombol aksi cepat, dan status toko.
   - 4 Kartu KPI Metrik Utama dengan indikator pertumbuhan real-time.
2. **Smart Nota & Kuitansi Otomatis (Highlight Feature):**
   - **Upload Logo Toko Kustom:** Unggah logo bisnis Anda langsung dari browser (tersimpan permanen di memori lokal).
   - **Kalkulasi Otomatis Real-time:** Hitung subtotal, diskon (Rp), sakelar pajak PPN 11%, dan kembalian tunai secara otomatis tanpa repot kalkulator.
   - **Dukungan Printer Kasir Thermal:** Mode cetak 58mm roll, 80mm roll, serta format faktur A4.
   - **Kirim Nota via WhatsApp:** Format pesan kuitansi rapi dan kirim ke pelanggan dengan satu klik.
3. **Manajemen Data & Transaksi Interaktif:**
   - Tab filter dinamis (Semua, Aktif, Selesai, dll).
   - Pencarian real-time dan sorting data.
   - Tambah data transaksi baru dengan modal terintegrasi.
   - Export laporan keuangan & transaksi ke file **CSV / Excel**.
4. **Penyimpanan Lokal Persisten (LocalStorage):**
   - Data transaksi dan profil toko tetap tersimpan aman di browser Anda tanpa perlu konfigurasi database yang rumit.

---

## 📊 Indikator Metrik (KPI)
- **Pemasukan Bulan Ini**: Rp 18.750.000 (+8.2% vs target bulanan)
- **Okupansi Kamar**: 16 / 20 Kamar (80% kamar terisi)
- **Jatuh Tempo Minggu Ini**: 4 Kamar (Invoice siap kirim WA)
- **Kamar Kosong**: 3 Kamar Siap (1 Kamar proses cat/perbaikan)

---

## 🎨 Skema Desain & Warna
- **Aplikasi:** SIMKOST Pro
- **Aksen Warna:** Emerald & Teal (Primary: `#059669`, Accent: `#10b981`)
- **Tipografi:** Plus Jakarta Sans & JetBrains Mono (Receipt Typography)
- **Kompatibilitas:** Chrome, Safari, Edge, Firefox, Android WebView

---

## 🚀 Cara Menjalankan

Aplikasi ini dirancang fleksibel: dapat langsung dijalankan tanpa instalasi (*zero-dependency*), atau dijalankan menggunakan runtime development Node.js/Vite.

### Opsi 1: Jalankan Langsung (Zero Dependency)
Cukup buka file `index.html` langsung di browser favorit Anda (klik 2x pada file `index.html`). Tidak memerlukan server khusus!

### Opsi 2: Jalankan via Vite / Node.js
```bash
# 1. Masuk ke direktori
cd ram-kost

# 2. Install dependencies (opsional untuk live reload)
npm install

# 3. Jalankan server lokal
npm run dev
```

---

## 📁 Struktur Direktori
```
ram-kost/
├── index.html          # Aplikasi utama Standalone SPA (HTML5 + Tailwind + JS)
├── package.json        # Konfigurasi package & scripts Vite
├── vite.config.js      # Konfigurasi dev-server Vite
├── .gitignore          # Pengabaian file Git
├── LICENSE             # Lisensi Open Source (MIT)
└── README.md           # Dokumentasi lengkap
```

---

## 📄 Lisensi
Hak Cipta (c) 2026 **RAM.AI.ID** & **Arie Isnain**.  
Didistribusikan di bawah Lisensi **MIT**. Silakan lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
