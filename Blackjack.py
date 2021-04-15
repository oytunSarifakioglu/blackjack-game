import copy
import random

def dogru_girdi(a=[],str=""):
    girdi = input(str)
    while girdi not in a:
       girdi = dogru_girdi(a,"Lütfen belirtilmiş değerler arasından bir değer giriniz:")
    else:
        return girdi


def kart_degeri(liste = []):
    as_var_mi = False
    for i in range(len(liste)):
        if "As" in list(liste[i].keys())[0]:
            as_var_mi = True
    deger = 0
    deger_listesi = []
    for j in range(len(liste)):
        deger += list(liste[j].values())[0]
    deger_listesi.append(deger)
    if as_var_mi:
        deger_listesi.append(deger - 10)
    if len(deger_listesi) > 1:
        if max(deger_listesi) > 21:
            deger_listesi = [min(deger_listesi)]
    return deger_listesi

def kart_cek(liste):
    cekilen = liste.pop(0)
    return cekilen, liste

def deger_ayarla(oyuncu_el_deger):
    if len(oyuncu_el_deger) > 1:
        if max(oyuncu_el_deger) > 21:
            oyuncu_el_deger = [min(oyuncu_el_deger)]
            return oyuncu_el_deger

def kart_göster(oyuncu_el,oyuncu_el_deger,str="Oyuncunun"):
    print(str,"kağıtları: ", end="")
    for i in range(len(oyuncu_el)):
        print(list(oyuncu_el[i].keys())[0], end=" ")
    print("(Toplam ", end="")
    if len(oyuncu_el_deger) > 1:
        print(oyuncu_el_deger[1], " ya da ", oyuncu_el_deger[0],") ", sep="")
    else:
        print(oyuncu_el_deger[0], ")",sep="")

def blackjack():
    while True:

        black_jack_oyuncu = False
        black_jack_dagitici = False
        oyun_devam = True
        oyun_sonuc = ""

        kart_destesi = [{"Maça As" : 11}, {"Maça ikili" : 2}, {"Maça üçlü" : 3}, {"Maça dörtlü" : 4},
                        {"Maça beşli" : 5}, {"Maça altılı" : 6}, {"Maça yedili" : 7}, {"Maça sekizli" : 8},
                        {"Maça dokuzlu" : 9}, {"Maça onlu" : 10}, {"Maça vale" : 10}, {"Maça kız" : 10}, {"Maça papaz" : 10},
                        {"Kupa As" : 11}, {"Kupa ikili" : 2}, {"Kupa üçlü" : 3}, {"Kupa dörtlü" : 4},
                        {"Kupa beşli" : 5}, {"Kupa altılı" : 6}, {"Kupa yedili" : 7}, {"Kupa sekizli" : 8},
                        {"Kupa dokuzlu" : 9}, {"Kupa onlu" : 10}, {"Kupa vale" : 10}, {"Kupa kız" : 10}, {"Kupa papaz" : 10},
                        {"Sinek As" : 11}, {"Sinek ikili" : 2}, {"Sinek üçlü" : 3}, {"Sinek dörtlü" : 4},
                        {"Sinek beşli" : 5}, {"Sinek altılı" : 6}, {"Sinek yedili" : 7}, {"Sinek sekizli" : 8},
                        {"Sinek dokuzlu" : 9}, {"Sinek onlu" : 10}, {"Sinek vale" : 10}, {"Sinek kız" : 10}, {"Sinek papaz" : 10},
                        {"Karo As" : 11}, {"Karo ikili" : 2}, {"Karo üçlü" : 3}, {"Karo dörtlü" : 4},
                        {"Karo beşli" : 5}, {"Karo altılı" : 6}, {"Karo yedili" : 7}, {"Karo sekizli" : 8},
                        {"Karo dokuzlu" : 9}, {"Karo onlu" : 10}, {"Karo vale" : 10}, {"Karo kız" : 10}, {"Karo papaz" : 10}]

        # Deste Karılır

        deste = random.sample(kart_destesi, len(kart_destesi))

        # İlk kartlar dağıtılır

        oyuncu_el = [] ; dagitan_el = []
        for i in range(2):
            cekilen, deste = kart_cek(deste)
            oyuncu_el.append(cekilen)
            cekilen, deste = kart_cek(deste)
            dagitan_el.append(cekilen)

        # İlk el için kart değeri hesaplanır

        oyuncu_el_deger = kart_degeri(oyuncu_el)
        dagitan_el_deger = kart_degeri(dagitan_el)

        if max(dagitan_el_deger) == 21:
            black_jack_dagitici = True

        # Dağıtıcının açık kağıdı gösterilir

        print("Dağıtıcının açık kağıdı: ", list(dagitan_el[0].keys())[0] )

        # Oyuncunun kartları gösterilir

        kart_göster(oyuncu_el,oyuncu_el_deger)

        if max(oyuncu_el_deger) == 21:
            black_jack_oyuncu = True
            print("BLACKJACK!!")

        if black_jack_oyuncu:
            if black_jack_dagitici:
                kart_göster(dagitan_el,dagitan_el_deger,"Dağıtanın")
                print("Masa da BLACKJACK yaptı!!")
                oyun_sonuc = "Oyun BERABERE!"
                oyun_devam = False
            else:
                kart_göster(dagitan_el, dagitan_el_deger, "Dağıtanın")
                oyun_sonuc = "Kazandınız!!!"
                oyun_devam = False


        while oyun_devam and min(oyuncu_el_deger) <= 21:
            girdi = dogru_girdi(["K","k","P","p"], "(K)ağıt mı (P)as mı? ")
            if girdi in ["K","k"]:
                print("Kart çekiliyor...")
                cekilen, deste = kart_cek(deste)
                oyuncu_el.append(cekilen)
                oyuncu_el_deger = kart_degeri(oyuncu_el)
                kart_göster(oyuncu_el, oyuncu_el_deger)

            else:
                break

        else:
            if oyun_devam:
                print("Oyuncu battı.")
                oyun_sonuc = "Kaybettiniz!!"
                oyun_devam = False

        if oyun_devam and black_jack_dagitici:
            kart_göster(dagitan_el, dagitan_el_deger, "Dağıtanın")
            print("Dağıtan BLACKJACK yaptı!!")
            oyun_sonuc = "Kaybettiniz!!"
            oyun_devam = False

        if oyun_devam:
            kart_göster(dagitan_el, dagitan_el_deger, "Dağıtanın")

        while oyun_devam and max(dagitan_el_deger) < 17:
            print("Dağıtıcı kart çekiyor...")
            cekilen, deste = kart_cek(deste)
            dagitan_el.append(cekilen)
            dagitan_el_deger = kart_degeri(dagitan_el)
            if max(dagitan_el_deger) > 21:
                dagitan_el_deger = [min(dagitan_el_deger)]
            kart_göster(dagitan_el, dagitan_el_deger, "Dağıtanın")
        else:
            if oyun_devam and min(dagitan_el_deger) > 21:
                print("Dagitici battı.")
                oyun_sonuc = "Kazandınız!!"
                oyun_devam = False

        if oyun_devam:

            #kart_göster(dagitan_el, dagitan_el_deger, "Dağıtanın")
            kart_göster(oyuncu_el, oyuncu_el_deger)
            if max(oyuncu_el_deger) > max(dagitan_el_deger):
                print("Eliniz dağıtaninkinden büyük.")
                oyun_sonuc = "Kazandınız!!"
                oyun_devam = False
            elif max(oyuncu_el_deger) < max(dagitan_el_deger):
                print("Dağıtıcının eli sizin elinizden büyük.")
                oyun_sonuc = "Kaybettiniz!!"
                oyun_devam = False
            else:
                print("Sizin elinizle dağıtıcının eli eşit değerde.")
                oyun_sonuc = "Berabere!"
                oyun_devam = False

        print(oyun_sonuc)

        girdi = dogru_girdi(["E", "e", "H", "h"], "Tekrar oynamak istiyor musunuz? (E,e/H,h)")
        if girdi in ["h", "H"]:
            break



blackjack()