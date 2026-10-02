#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.py
Tujuan: Mengintegrasikan seluruh modul (identitas, ssh_modul, snmp_modul,
        netconf_modul, telemetry_modul), menjalankannya secara berurutan,
        lalu mencetak satu laporan akhir gabungan lewat class LaporanCabang.
NIM: 2409106079 | Nama: Muhammad Ilma Yusrian Fahmi
"""
import identitas
from ssh_modul import cek_ssh
from snmp_modul import cek_snmp
from netconf_modul import buat_pesan_netconf
from telemetry_modul import klasifikasi_telemetry

class LaporanCabang:
    """Merangkum seluruh hasil pengecekan cabang virtual menjadi satu laporan."""

    def __init__(self, nim, nama, kode_cabang):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        print("\n" + "=" * 60)
        print(" LAPORAN AKHIR CABANG VIRTUAL")
        print("=" * 60)
        print(f"NIM          : {self.nim}")
        print(f"Nama         : {self.nama}")
        print(f"Kode Cabang  : {self.kode_cabang}")

        print("\n--- Hasil SSH ---")
        print(f"Status   : {hasil_ssh['status']}")
        if hasil_ssh["status"] == "BERHASIL":
            print(f"Hostname : {hasil_ssh['hostname']}")
            print(f"Uptime   : {hasil_ssh['uptime']}")
        else:
            print(f"Error    : {hasil_ssh['pesan_error']}")

        print("\n--- Hasil SNMP ---")
        print(f"Status   : {hasil_snmp['status']}")
        if hasil_snmp["status"] == "BERHASIL":
            print(f"sysName  : {hasil_snmp['sys_name']}")
        else:
            print(f"Error    : {hasil_snmp['pesan_error']}")

        print("\n--- Pesan NETCONF (edit-config VLAN) ---")
        print(pesan_netconf)

        print("\n--- Hasil Klasifikasi Telemetry ---")
        for perangkat, info in hasil_telemetry.items():
            print(f"{perangkat:20s} : {info['cpuUsage']:3d}% -> {info['status']}")

        print("=" * 60)
        print(" Laporan selesai.")
        print("=" * 60 + "\n")

def main():
    print(">> Menjalankan pengecekan SSH...")
    hasil_ssh = cek_ssh()

    print("\n>> Menjalankan pengecekan SNMP...")
    hasil_snmp = cek_snmp()

    print("\n>> Membangun pesan NETCONF...")
    pesan_netconf = buat_pesan_netconf()

    print("\n>> Menjalankan klasifikasi telemetry...")
    hasil_telemetry = klasifikasi_telemetry()

    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan(hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry)

if __name__ == "__main__":
    main()
