# UTS Jaringan Komputer Lanjut — Integration Network with Python

**NIM:** 2409106079
**Nama:** Muhammad Ilma Yusrian Fahmi
**Kelas:** B 2024 — Informatika

## Struktur Project
 
```
2409106079_MuhammadIlmaYusrianFahmi_UTS_JKL/
├── .gitignore
├── README.md
├── identitas.py        # Bagian A - identitas cabang & buat_id_perangkat()
├── ssh_modul.py         # Bagian B - cek_ssh() lewat Paramiko
├── snmp_modul.py        # Bagian C - cek_snmp() lewat PySNMP (SNMPv2c)
├── netconf_modul.py      # Bagian D - buat_pesan_netconf() (ElementTree)
├── telemetry_modul.py    # Bagian E - klasifikasi_telemetry()
└── main.py               # Bagian F - integrasi akhir & LaporanCabang
```

## Cara Menjalankan

1. Pastikan Python 3 dan virtual environment sudah disiapkan:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   pip install paramiko pysnmp
   ```
2. Pastikan VM cabang (dari Tugas Pertemuan 2) sudah menyala dengan:
   - SSH aktif, user `admin_<kode_cabang>` sudah dibuat di VM
   - SNMP aktif dengan community string `comm_<kode_cabang>`
   - Port forwarding VirtualBox untuk SSH dan SNMP sudah dikonfigurasi
3. Isi kredensial (`pass_ssh`) di `ssh_modul.py` sesuai VM.
4. Jalankan program utama:
   ```
   python main.py
   ```
5. Program akan mencetak hasil SSH, SNMP, pesan NETCONF yang dibangun, hasil
   klasifikasi telemetry, dan satu laporan akhir gabungan di akhir eksekusi.

## Ringkasan Personalisasi

- Kode cabang diambil dari 3 digit terakhir NIM.
- Username SSH mengikuti format `admin_<kode_cabang>`.
- Community string SNMP mengikuti format `comm_<kode_cabang>`.
- VLAN ID pada modul NETCONF memakai angka dari kode_cabang secara langsung.
- Data sampel telemetry diturunkan dari pasangan digit NIM (lihat komentar
  di `telemetry_modul.py` untuk rincian penurunan nilainya).

*(Nilai kode_cabang, password, dan kredensial lain sengaja tidak dicantumkan
di README ini sesuai ketentuan tugas.)*

## Catatan Teknis

Modul `snmp_modul.py` dan `ssh_modul.py` memakai library PySNMP dan Paramiko
sesuai ketentuan tugas. Pada environment Windows dengan Python versi terbaru
(3.12+), ditemukan beberapa kendala kompatibilitas yang sudah diperbaiki:

- `pysnmp` versi terbaru (5.x/6.x) menghapus struktur `pysnmp.hlapi` versi lama,
  sehingga perlu di-pin ke versi lama: `pysnmp==4.4.12`, `pyasn1==0.4.8`,
  `pyasn1-modules==0.2.8`.
- Modul bawaan `asyncore` sudah dihapus dari Python 3.12+, sehingga perlu
  menambahkan `pip install pyasyncore` sebagai pengganti.
- `pysnmp` versi lama memiliki bug saat memeriksa `importlib.util.MAGIC_NUMBER`
  jika dijalankan sebagai modul tunggal (tanpa diimpor lewat modul lain
  terlebih dahulu). Ditangani dengan menambahkan `import importlib.util`
  secara eksplisit di baris paling atas `snmp_modul.py`, sebelum
  `from pysnmp.hlapi import ...`.

Dengan ketiga penyesuaian ini, setiap modul (termasuk `snmp_modul.py`) bisa
dijalankan sendiri (`python snmp_modul.py`) maupun lewat `main.py` tanpa error.
