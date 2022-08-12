def ortalama_oku():
    with open("sınav_notları.txt", "r", encoding="utf-8")as file:
        for satir in file:
            print(not_hesapla(satir))

def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    adı=liste[0]
    notlar=liste[1].split(',')
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not3+not2+not1)/3
    if ortalama<=100 and ortalama>=90:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    else:
        harf="FF"

    return  adı+":"+harf+"\n"

def not_gir():
    ad=input("ad:")
    soyad=input("Soyad:")
    not1=input("not1:")
    not2=input("not2:")
    not3=input("not3:")
    with open("sınav_notları.txt", "a", encoding="utf-8") as file:
        file.write(ad+' '+ soyad+":"+ not1+","+ not2+","+not3+"\n")


def kayit_et():
    with open("sınav_notları.txt", "r", encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuçlar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem=input('1-Not Oku\n2-Not Girişi\n3 Not Kayıt Et\n4-Cıkıs\n')
    if islem=='1':
        ortalama_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        kayit_et()
    else:
        break