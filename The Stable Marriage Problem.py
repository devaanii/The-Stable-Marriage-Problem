# Nama          : Devani
# NIM           : 23343033
# Prodi         : Informatika (NK)
# Mata Kuliah   : Perancangan dan Analisis Algoritma

def pernikahan_stabil(preferensi_pria, preferensi_wanita):
    jumlah_pria = len(preferensi_pria)
    
    pria_lajang = list(preferensi_pria.keys())
    pasangan = {}
    pasangan_wanita = {wanita: None for wanita in preferensi_wanita}
    urutan_lamaran = {pria: 0 for pria in preferensi_pria}

    while pria_lajang:
        pria = pria_lajang[0]
        daftar_preferensi = preferensi_pria[pria]
        wanita_dilamar = daftar_preferensi[urutan_lamaran[pria]]
        urutan_lamaran[pria] += 1

        if pasangan_wanita[wanita_dilamar] is None:
            pasangan[pria] = wanita_dilamar
            pasangan_wanita[wanita_dilamar] = pria
            pria_lajang.remove(pria)
        else:
            pasangan_saat_ini = pasangan_wanita[wanita_dilamar]
            preferensi_wanita_dilamar = preferensi_wanita[wanita_dilamar]

            if preferensi_wanita_dilamar.index(pria) < preferensi_wanita_dilamar.index(pasangan_saat_ini):
                pasangan[pria] = wanita_dilamar
                pasangan_wanita[wanita_dilamar] = pria
                pria_lajang.remove(pria)
                pria_lajang.append(pasangan_saat_ini)

    return pasangan

preferensi_pria = {
    "Rudi": ["Dewi", "Siti", "Lina"],
    "Budi": ["Lina", "Dewi", "Siti"],
    "Andi": ["Dewi", "Lina", "Siti"]
}

preferensi_wanita = {
    "Dewi": ["Budi", "Rudi", "Andi"],
    "Siti": ["Rudi", "Budi", "Andi"],
    "Lina": ["Andi", "Budi", "Rudi"]
}

hasil = pernikahan_stabil(preferensi_pria, preferensi_wanita)

for pria, wanita in hasil.items():
    print(f"{pria} bertunangan dengan {wanita}")