#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
identitas.py
Tujuan: Menyimpan identitas cabang virtual (NIM, nama, kode_cabang) dan
        menyediakan fungsi pembuatan ID perangkat yang dipakai modul lain.
Dibuat oleh: Muhammad Ilma Yusrian Fahmi | NIM: 2409106079
"""

nim = "2409106079"
nama = "Muhammad Ilma Yusrian Fahmi"
kode_cabang = nim[-3:]


def buat_id_perangkat(jenis, nomor):
    """
    Membuat ID perangkat dengan format: <jenis>-<kode_cabang>-<nomor 3 digit>.
    Contoh: buat_id_perangkat("router", 1) -> "router-079-001"
    """
    return f"{jenis}-{kode_cabang}-{int(nomor):03d}"

if __name__ == "__main__":
    print(f"NIM         : {nim}")
    print(f"Nama        : {nama}")
    print(f"Kode Cabang : {kode_cabang}")
    print(f"Contoh ID   : {buat_id_perangkat('router', 1)}")
