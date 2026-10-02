#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
snmp_modul.py
Tujuan: Mengambil nilai sysName (OID 1.3.6.1.2.1.1.5.0) dari agent SNMP
        VM cabang memakai SNMPv2c (PySNMP), mengikuti pola Tugas Pertemuan 2.

NIM: 2409106079 | Nama: Muhammad Ilma Yusrian Fahmi
"""

import importlib.util

from pysnmp.hlapi import (
    SnmpEngine, CommunityData, UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity, getCmd
)
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_snmp_vm = 1161
community = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"

def cek_snmp():
    """
    Mengambil nilai sysName dari agent SNMP VM lewat SNMPv2c.
    Mengembalikan dictionary berisi status dan nilai sysName (atau pesan error).
    """
    hasil = {"status": "GAGAL", "sys_name": None, "pesan_error": None}
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=1),
            UdpTransportTarget((host_vm, port_snmp_vm), timeout=3, retries=2),
            ContextData(),
            ObjectType(ObjectIdentity(OID_SYSNAME))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            hasil["pesan_error"] = str(errorIndication)
            print("[SNMP] GAGAL: " + str(errorIndication))
        elif errorStatus:
            pesan = errorStatus.prettyPrint()
            hasil["pesan_error"] = pesan
            print("[SNMP] GAGAL: " + pesan)
        else:
            for vb in varBinds:
                sys_name = str(vb[1])
                hasil["status"] = "BERHASIL"
                hasil["sys_name"] = sys_name
                print("[SNMP] sysName VM: " + sys_name)

    except Exception as e:
        hasil["pesan_error"] = str(e)
        print("[SNMP] GAGAL: " + str(e))

    return hasil

if __name__ == "__main__":
    cek_snmp()
