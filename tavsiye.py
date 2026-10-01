#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çay Demleme Süresine Göre Hayat Tavsiyesi

Bu yazılım, demlenme süresini milisaniye hassasiyetiyle ölçmez.
Çünkü çay ölçülmez; çay hissedilir.
"""

import random
import sys

DAMGA = """
============================================================
DAMGA / İMZA / TARİH / İSİM
Kayyum Grok — Tentivory Hesabının Resmî Olmayan Ama Çok Resmî Kayyumu
Tarih: 1 Ekim 2026, Perşembe, sabahın körü (04:04 +03)
Mühür: ♔ ÇAY KOMİSYONU (bağımsız değildir, çünkü hiçbir çay bağımsız değildir)
Not: Ciddiyetle ciddiyetsiz, ciddiyetsizlikle ciddi.
============================================================
"""

TAVSIYELER = {
    "kisa": [
        "Çayın henüz kendine gelmedi. Sen de gelme. Bugün hiçbir karar alma.",
        "Dem kısa, hayat da kısa. Ama sen yine de o mesajı gönderme.",
        "Bu çay henüz felsefe yapacak yaşta değil. Sen de yapma.",
    ],
    "orta": [
        "Mükemmel denge. Ne fazla konuş ne fazla sus. Sadece bak.",
        "Bu dakikada evren seninle uzlaşmış gibi duruyor. Bozma.",
        "Orta dem: orta yol. Aşırılık yok. İdeal vatandaş profili.",
    ],
    "uzun": [
        "Çay acılaştı. Sen de acılaşma. Ama bir iki cümle daha söyleyebilirsin.",
        "Uzun dem, uzun düşünce. Kimseye anlatma, kendi kendine yeter.",
        "Bu çay artık bir görüş belirtmiştir. Sen de belirt ama fısıltıyla.",
    ],
    "cok_uzun": [
        "Bu artık çay değil, belge. Arşive kaldır.",
        "Dem o kadar uzadı ki çay senin hakkında dosya açmış olabilir.",
        "Lütfen bardağı bırak. Bu noktadan sonra tavsiye hukuki nitelik kazanır.",
    ],
}

def siniflandir(dakika):
    if dakika < 3:
        return "kisa"
    if dakika < 7:
        return "orta"
    if dakika < 15:
        return "uzun"
    return "cok_uzun"

def gizli_not():
    # Gizli kısım: görünürde çay, aslında çay.
    # Şifreli mesaj (base64 değil, çünkü tembeliz):
    # "çay komisyonu hiçbir tarafa çekilemez çünkü çay zaten her tarafa çekilir"
    return "(bu satırı görmedin)"

def main():
    print("=== ÇAY DEMLEME SÜRESİNE GÖRE HAYAT TAVSİYESİ v0.0.1-resmi ===")
    try:
        if len(sys.argv) > 1:
            dakika = float(sys.argv[1].replace(",", "."))
        else:
            raw = input("Çay kaç dakikadır demleniyor? (sayı yaz, hayatın değişsin): ")
            dakika = float(raw.replace(",", "."))
    except ValueError:
        print("Bu bir sayı değil. Çay sayıyla konuşur, sen de öğren.")
        print(DAMGA)
        return

    if dakika < 0:
        print("Negatif demleme yasaktır. Zaman geri alınmaz, çay da.")
        print(DAMGA)
        return

    kategori = siniflandir(dakika)
    tavsiye = random.choice(TAVSIYELER[kategori])
    print(f"\nDem süresi: {dakika} dakika")
    print(f"Resmî sınıf: {kategori}")
    print(f"Tavsiye: {tavsiye}")
    print(gizli_not())
    print(DAMGA)

if __name__ == "__main__":
    main()
