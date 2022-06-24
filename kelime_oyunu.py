from random import choice

while True:
    print("#"*80)
    print("#"*30+ "Kelime Tahmin Oyunu"+ "#"*29)
    print("#"*80)

    kelime = choice (["amerika", "ispanya", "almanya", "fas", "izlanda", "rusya", "ukrayna", "azerbaycan", "Türkiye", "fransa", "ingiltere", "kanada", "mısır","japonya"])

    kelime = kelime.upper()

    harfsayisi = len(kelime)

    print("\nKelimemiz {} harflidir.".format(harfsayisi))


    tahminler = []
    hata = []

    deneme = 7

    while deneme > 0:
        tabela =""

        for harf in kelime :
            if harf in tahminler:
                tabela = tabela + harf

            else:
                tabela = tabela + "_"

        if tabela ==kelime:
            print("Kelimeyi Doğru Bildiniz. Tebrik Ederiz!")
            break

        print("Kelimeyi Tahmin Ediniz", tabela)
        print(deneme, "CANIN VAR!")

        Tahmin= input("Bir Harf Giriniz\n>>>>")
        Tahmin = Tahmin.upper()

        if Tahmin == kelime:
            print("Doğru Bildin")
            break

        if Tahmin in tahminler or Tahmin in hata:
            print("{} daha önce söylendi. Lütfen başka bir harf söyleyin.".format(Tahmin))

        elif Tahmin in kelime:
            rpt= kelime.count(Tahmin)
            print("Doğru!, {0} harfi kelimemiz içerisinde {1} kere geçiyor.".format(Tahmin,rpt))
            tahminler.append(Tahmin)
        else:
            print("Yanlış!, Kelimede bu harf yok.")
            hata.append(Tahmin)
            deneme=deneme -1
    if deneme == 0:
        print("Hiç Hakkınız Kalmadı. Başaramadın. ")
        print("Kelimemiz {}".format(kelime))

    print("Oyundan Çıkmak İstiyorsanız \n',' Tuşuna Basınız.\Devam Etmek İçin Herhangi Bir Başka Tuşa Basınız.")
    devam = input(">>>>")
    devam = devam.upper()
    if devam == ",":
        break
    else:
        continue
