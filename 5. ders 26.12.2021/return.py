#3 sayı alıp ortalamsını bul sonra çağırıldığı yere geri götür

def ortalama(x,y,z):
    return (x+y+z)/3

x=int(input("sayı giriniz: "))
y=int(input("sayı giriniz: "))
z=int(input("sayı giriniz: "))

sonuc=ortalama(x,y,z)

print(sonuc)