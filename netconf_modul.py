#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
netconf_modul.py
Tujuan: Membangun (bukan menulis manual) string pesan NETCONF <rpc><edit-config>
        untuk membuat VLAN baru, menggunakan xml.etree.ElementTree.
        Modul ini TIDAK terhubung ke perangkat NETCONF sungguhan; fokusnya
        adalah membuktikan pemahaman struktur NETCONF (messages/operations/content).
Dibuat oleh: Muhammad Ilma Yusrian Fahmi | NIM: 2409106079
"""
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from identitas import kode_cabang

VLAN_ID = int(kode_cabang)

def buat_pesan_netconf():
    """
    Membangun string XML lengkap untuk permintaan NETCONF <rpc><edit-config>
    yang membuat VLAN baru dengan ID = kode_cabang.
    Mengembalikan string XML yang sudah di-format rapi (pretty-printed).

    Catatan lapisan NETCONF (ditandai lewat komentar di bawah):
    - Transport layer  : SSH (di luar cakupan XML ini, dijalankan terpisah
                          lewat protokol SSH ke perangkat NETCONF sungguhan)
    - Messages layer   : elemen <rpc> pembungkus, dengan atribut message-id unik
    - Operations layer : elemen <edit-config> beserta <target>, yaitu operasi
                          NETCONF yang diminta untuk dijalankan
    - Content layer    : isi <config> di dalamnya, yaitu data konfigurasi VLAN
                          yang sebenarnya ingin diterapkan ke perangkat
    """

    rpc = ET.Element("rpc", attrib={
        "message-id": "101",
        "xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0",
    })

    edit_config = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit_config, "target")
    ET.SubElement(target, "running")

    config = ET.SubElement(edit_config, "config")

    vlans = ET.SubElement(config, "vlans", attrib={
        "xmlns": "urn:example:params:xml:ns:yang:vlan-config"
    })
    vlan = ET.SubElement(vlans, "vlan")
    ET.SubElement(vlan, "vlan-id").text = str(VLAN_ID)
    ET.SubElement(vlan, "name").text = f"VLAN_CABANG_{kode_cabang}"
    ET.SubElement(vlan, "operation").text = "create"

    xml_mentah = ET.tostring(rpc, encoding="unicode")
    xml_rapi = minidom.parseString(xml_mentah).toprettyxml(indent="  ")

    baris = [b for b in xml_rapi.split("\n") if b.strip()]
    return "\n".join(baris)

if __name__ == "__main__":
    print(buat_pesan_netconf())
