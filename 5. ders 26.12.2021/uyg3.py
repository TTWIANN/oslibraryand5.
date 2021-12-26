#gönderilen değelerin taammını ekrana basan fonksiyon
#değer sayısı herhangi olabilir

def topla(*sayilar):      #listenin foknsiyondaki hali * (demet)
    toplam=0
    for i in sayilar:
        toplam=toplam+i
    print(toplam)
