#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ssh_modul.py
Tujuan: Melakukan pengecekan akses jarak jauh ke VM cabang lewat SSH
        (memakai Paramiko), mengikuti pola pada Tugas Pertemuan 2.
NIM: 2409106079 | Nama: Muhammad Ilma Yusrian Fahmi
"""
import paramiko
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_ssh_vm = 2222
user_ssh = f"admin_{kode_cabang}"
pass_ssh = "123"

def cek_ssh():
    """
    Login ke VM lewat SSH, menjalankan minimal dua perintah diagnostik
    (hostname dan uptime), lalu mencetak dan mengembalikan hasilnya.
    Kegagalan koneksi ditangani dengan try/except agar program tidak berhenti.
    """
    hasil = {"status": "GAGAL", "hostname": None, "uptime": None, "pesan_error": None}
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            host_vm, port=port_ssh_vm,
            username=user_ssh, password=pass_ssh, timeout=5
        )

        _, stdout, _ = client.exec_command("hostname")
        hostname = stdout.read().decode().strip()

        _, stdout, _ = client.exec_command("uptime -p")
        uptime = stdout.read().decode().strip()

        client.close()

        hasil["status"] = "BERHASIL"
        hasil["hostname"] = hostname
        hasil["uptime"] = uptime
        print(f"[SSH] hostname VM : {hostname}")
        print(f"[SSH] uptime VM   : {uptime}")

    except Exception as e:
        hasil["pesan_error"] = str(e)
        print("[SSH] GAGAL: " + str(e))

    return hasil

if __name__ == "__main__":
    cek_ssh()
