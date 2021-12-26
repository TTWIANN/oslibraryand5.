def cevre(kisa,uzun):
    print("dikdörtgenin çevresi:",(kisa+uzun)*2)
def alan(kisa,uzun):
    print("dikdörtgenin alanı:",kisa*uzun)
# def sorgula(kisa,uzun):
#     if kisa>uzun:
#         print("değeleri doğru giriniz")
print("dikdörtgen hesabı")
secim=input("hesapalama türünü seçiniz: (çevre/alan)").lower()
kisa=int(input("kısa kenarı giriniz: "))
uzun=int(input("uzun kenarı giriniz: "))

if secim=="çevre":
    cevre(kisa,uzun)
elif secim == "alan":
    alan(kisa,uzun)
