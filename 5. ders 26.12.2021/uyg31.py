#verilen sayı akdar klasör oluşturan fonksiyon yaznınız
import os

def klasor(x):
    for i in range(x):
        os.chdir("C:/Users/egitim.sinif2/Desktop")
        os.mkdir("spider"+str(i+1))
sayi=int(input("klasör syısını giriniz: "))
klasor((sayi))