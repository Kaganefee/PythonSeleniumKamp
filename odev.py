# string = Metin veri tipleridir.
# İnt (integer)= Tamsayı veri tipleri için kullanılır.
# float = Ondalıklıklı sayı veri tipleri için kullanılır.
# complex = reel ve imajiner sayı tipleri için kullanılır. (aşırı büyük sayı değerleri için)
# list = Veri tiplerinin birlikte bir küme halinde tutulması için kullanılır."[]"
# tuple = list ile aynı işlevi görür fakat içindeki elemanlar değiştirilemez."()"
# dict (dictionaries) = adresleme tipidir. Sözlük gibi bir kelime ve anlam tanımlar.
# bool(bolean) = Mantıksal veri tipidir. True ve False olmak üzere iki adet dönüş türü vardır.

# -----------------------------------------------------------------------------------------------------


# Kategori seçimi = string (filtrelemek için)
# eğitmen seçimi = string
# kurs bul bölümüne yazılan yazı = string 
# katılmış olduğumuz kurslarda yazan yüzdelik bölüm = int 
# kurs isimleri = string
# açıklamalar = string

# ----------------------------------------------------------------------------------------------------

kursaKatildiMi = True
kacBolumYaptı = 2

if  kursaKatildiMi == True:
    if  kacBolumYaptı == 1 :
        print("%25 tamamlandı")
    elif kacBolumYaptı == 2 : 
        print("%50 tamamlandı")
    elif kacBolumYaptı == 3 :
        print("%75 tamamlandı")
    else : 
        print("%100 tamamlandı")
else :
    print("ÜCRETSİZ")             

