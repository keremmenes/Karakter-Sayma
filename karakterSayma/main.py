metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez."""

harf = str(input("Sorgulatmak istediğiniz harfi girin"))

sayı=[]
for i in metin:
    if harf==i:
        sayı+=i
print(len(sayı))


def bol(x, y, bolum=0, kalan=0, ondalik=0, s="", b=""):
    if x < y:
        x = x * 10
        b = ""
        for i in range(5):
            while (x - y >= 0):
                x = x - y
                ondalik += 1
            b = b + str(ondalik)
        return (x, y, bolum, kalan, ondalik, b)

    else:
        bolum += 1
        return bol(x - y, y, bolum, kalan, ondalik, s="", b="")


sonuc = bol(10, 5)
s = str(sonuc[2]) + "." + str(sonuc[5])
print("sonuc=", s)
