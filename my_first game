import  random
class Dusman:
    
    def __init__(self,isim = "Dusman",kalan_can = "500",saldiri_gucu = "200",mermi_sayisi = "10"):
         self.isim = isim
         self.kalan_can = kalan_can
         self.saldiri_gucu = saldiri_gucu
         self.mermi_sayisi = mermi_sayisi
         
    def saldir(self):
        print(self.isim + ":  Saldiriyor.")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi)+ "-  Mermi harcandi")
        self.mermi_sayi =-  harcanan_mermi

        return (harcanan_mermi, self.saldiri_gucu)
    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print(self.isim +":   VURULDUM...")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)
    def mermi_bitti_mi(self):
        if (self.mermi_sayisi <=0):
            print(self.isim + "Konusuyor:  Mermi bitti oyunu terk ediyorum...")
            return True
        return False
    def hayatta_mi(self):
        if (self.kalan_can <=0):
            print("Oluyorummmmm....")
        
    def print(self):
        print("basiliyorrrrrrrrr...........")
        print("Isim:",self.isim,'   Kalan can:',self.kalan_can,'    Saldiri gucu:',self.saldiri_gucu,'    Mermi sayisi:',self.mermi_sayisi)
        

dusmanlar =[]

i= 0
while (i<10):
    rastgelecan = random.randrange(10,20)
    rastgelesaldirigucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu, rastgelemermi )
    dusmanlar.append(yenidusman)

    i+=1

i=0
while (i<3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir()

    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])

    print("Raund Bitdi....." )
    
    i +=1
