b=20 #fonksiyon ışında olduğundan global değişkendir
def fonksiyon():
    global b
    a=10  #fonksiyonun içinde olduğu için yerel değişkendir
    b=4
fonksiyon()
print(b)
