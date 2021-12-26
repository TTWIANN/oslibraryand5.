#kendisine gönderilen kullanıcı adını ve şifreyi kondtrol ederek sonucunda true ya da false gönderen fonksiyon kodu
#kullanıcı adı: admin   şifre:123456

def kontrolet(kullanici, parola):
    if kullanici == "admin" and parola == "123456":
        return True

    else:
        return False
while True:
    kullanici=input("kullanıcı adı: ")
    parola=input("parola: ")
    sonuc=kontrolet(kullanici,parola)

    if sonuc==True:
        print("giriş başarılı")
    elif sonuc==False:
        print("tekrar deneyin")