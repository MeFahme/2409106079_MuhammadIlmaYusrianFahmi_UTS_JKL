#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
telemetry_modul.py
Tujuan: Menyimpan data sampel cpuUsage (menyerupai hasil decode telemetry GPB)
        yang diturunkan dari digit-digit NIM, lalu mengklasifikasikannya
        menjadi KRITIS / WASPADA / NORMAL.
Dibuat oleh: Muhammad Ilma Yusrian Fahmi | NIM: 2409106079
"""
from identitas import nim

_digit = [int(c) for c in nim]

# --- Data sampel cpuUsage, masing-masing diturunkan dari pasangan digit NIM ---
# router_utama       : digit[0], digit[1]  -> 2,4  -> 24  (NORMAL)
# switch_akses       : digit[6], digit[7]  -> 6,0  -> 60  (WASPADA)
# server_monitoring  : digit[8], digit[9]  -> 7,9  -> 79  (WASPADA)
# ap_wifi_lantai2    : 90 + digit[2]       -> 90+0 -> 90  (KRITIS)
data_telemetry = {
    "router_utama": {
        "cpuUsage": _digit[0] * 10 + _digit[1],
        "waktu": "2026-09-30T08:00:00Z",
    },
    "switch_akses": {
        "cpuUsage": _digit[6] * 10 + _digit[7],
        "waktu": "2026-09-30T08:00:05Z",
    },
    "server_monitoring": {
        "cpuUsage": _digit[8] * 10 + _digit[9],
        "waktu": "2026-09-30T08:00:10Z",
    },
    "ap_wifi_lantai2": {
        "cpuUsage": 90 + _digit[2],
        "waktu": "2026-09-30T08:00:15Z",
    },
}

def klasifikasi_telemetry():
    """
    Meng-iterasi data_telemetry, mengklasifikasikan setiap sampel cpuUsage:
    > 80        -> "KRITIS"
    50 - 80     -> "WASPADA"
    < 50        -> "NORMAL"
    Mencetak dan mengembalikan hasil klasifikasi sebagai dictionary.
    """
    hasil = {}
    for nama_perangkat, sampel in data_telemetry.items():
        cpu = sampel["cpuUsage"]
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"

        hasil[nama_perangkat] = {"cpuUsage": cpu, "status": status}
        print(f"[TELEMETRY] {nama_perangkat}: cpuUsage={cpu}% -> {status}")

    return hasil

if __name__ == "__main__":
    klasifikasi_telemetry()
