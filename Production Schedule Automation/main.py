dosya = open("C:\pyt\üretimÇizelge.txt","w")
# "C:\\aylar\\nisan\\toplam masraf\\masraf.txt"
dosya.close()
i=0

def Asil_Menü():
    print("----------Işık Holding----------")
    print("1) İstenen Üretim")
    print("2) Üretim Güncelleme")
    print("3) Üretim Arama")
    print("4) Üretim Listeleme")
    print("5) Üretim Silme")
    print("6) Üretim Maaliyet")
    print("7) Denetimci Maaliyet")
    print("8) Çıkış")
    istek = int(input("Seçiminiz:"))
    return istek

def  Kosullu_Üretim_Olusturma(i):
    üretim = {}
    üretim_No = int(input("Üretim Numarası:"))
    üretim["Üretim Numarası:"] =üretim_No
    Tedarikci_Firma=input("Tedarikçi Firmanın Adı:")
    üretim["Tedarikçi Firmanın Adı:"]=Tedarikci_Firma
    Talep_Miktari=int(input("Talep Miktarı(Adet):"))
    üretim["Talep Miktarı:"]=Talep_Miktari
    Denetimci=input("Denetimci Firma:")
    üretim["Denetimci Firma:"]=Denetimci
    Denetim_Türü=input("Denetim Türü:")
    üretim["Denetim Türü:"]=Denetim_Türü
    Denetim_Tarihi=input("Denetim Tarihi(GG-AA-YYYY):")
    üretim["Denetim Tarihi:"]=Denetim_Tarihi
    Denetim_Yeri=input("Denetim Yeri:")
    üretim["Denetim Yeri:"]=Denetim_Yeri
    dosya=open("üretimÇizelge.txt","a")
    dosya.write(str(üretim)+"\n")
    dosya.close()
    i=i+1
    print("Üretim Çizelgesi Başarı ile oluşturuldu")


def çizelgeListele():
    dosya = open("C:\pyt\üretimÇizelge.txt","r")
    for tlm in dosya:
        print(tlm)


def çizelgeArama():
    Üretim_No =input("Üretim Numarası:")
    sosis=[]
    dosya=open("C:\pyt\üretimÇizelge.txt","r")
    for s in dosya:
        sosis.append(s)
    dosya.close()
    tutamac = 0
    for i in sosis:
        tutamac += 1
        if Üretim_No == i[21:25]:
            break
    print(sosis[tutamac-1])

def Üretim_Silme():
    Üretim_No = input("Silinecek Üretimin Numarası:")
    sucuk = []
    dosya = open("C:\pyt\üretimÇizelge.txt","r")
    for s in dosya:
        sucuk.append(s)
    dosya.close()
    tutucu = 0
    for i in sucuk:
        tutucu +=1
        if Üretim_No == i[13:17]:
            break
    saklı = ""
    d = open("C:\pyt\üretimÇizelge.txt","r")
    saglam = d.read().splitlines()
    for n,s in enumerate(saglam,1):
        if n == tutucu:
            continue
        saklı = saklı + s + "\n"
    d.close()
    with open("C:\pyt\üretimÇizelge.txt","w") as d:
        d.write(saklı)
    print("Üretim Çizelgesi Başarıyla Silindi..")


def Maaliyet_Üretim():
    dosya = open("C:\pyt\üretimÇizelge.txt", "r")

    liste = [];
    for satir in dosya.readlines():
        liste.append(satir)

    for x in range(0,i):
        newList = liste[x].split(",")[2]
        print(newList[18:])



def Üretim_Guncelle():
    üretim_No = input("Güncellenecek Çizelgenin Numarası:")
    dosya = open("C:\pyt\üretimÇizelge.txt", "r")
    sucuk = []  # Dosyadaki satırları diziye eklemek için boş dizi
    for i in dosya:
        sucuk.append(i)  # satirları ekleme
    dosya.close()
    tutucu = 0
    for i in sucuk:
        tutucu = tutucu + 1  # girilen numaranın hangi satırda olduğunu bulma
        if üretim_No == i[21:25]:
            break

    helö = ""
    k = open("C:\pyt\üretimÇizelge.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == tutucu:
            continue
        helö = helö + s + "\n"
    k.close()
    with open("C:\pyt\üretimÇizelge.txt", "w") as k:
        k.write(helö)
    k.close()

    üretim = {}
    üretim_No = int(input("Üretim Numarası:"))
    üretim["Üretim Numarası:"] = üretim_No
    Tedarikci_Firma = input("Tedarikçi Firmanın Adı:")
    üretim["Tedarikçi Firmanın Adı:"] = Tedarikci_Firma
    Talep_Miktari = int(input("Talep Miktarı(Adet):"))
    üretim["Talep Miktarı:"] = Talep_Miktari
    Denetimci = input("Denetimci Firma:")
    üretim["Denetimci Firma:"] = Denetimci
    Denetim_Türü = input("Denetim Türü:")
    üretim["Denetim Türü:"] = Denetim_Türü
    Denetim_Tarihi = input("Denetim Tarihi(GG-AA-YYYY):")
    üretim["Denetim Tarihi:"] = Denetim_Tarihi
    Denetim_Yeri = input("Denetim Yeri:")
    üretim["Denetim Yeri:"] = Denetim_Yeri
    dosya = open("C:\pyt\üretimÇizelge.txt", "a")
    dosya.write(str(üretim) + "\n")
    dosya.close()
    print("Üretim Çizelgesi Başarı ile oluşturuldu")




while 1:
    ö = Asil_Menü()

    if ö == 1:
        Kosullu_Üretim_Olusturma(i)
    elif ö ==2:
        Üretim_Guncelle()
    elif ö == 3:
        çizelgeArama()
    elif ö == 4:
        çizelgeListele()
    elif ö == 5:
        Üretim_Silme()
    elif ö == 6:
        Maaliyet_Üretim()

    elif ö == 8:
        print("iyi günler!!")
        break

    else:
        print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")
        Asil_Menü()
