def siber():
    print("""
    ======================
         ARE YOU ADMIN 
    ======================""")
    name_admin = "admin"
    parol_admin = "admin"

    main_admin = input("Buraya sadece admin panel gire bilir('Çünkü onun özelleri bu odada') (admin_isminiz):") 
    main_parol_admin = input("Buraya sadece admin panel gire bilir ('Çünkü onun özelleri bu odada') (admin_şifreniz):") 
    if (main_admin==name_admin and main_parol_admin==parol_admin):
        print("hello Mr.Admin or Ms.Admin")
    else:
        print("Buranın şifresini sadece admin bilir !!!")
        exit()


    
    def if_and_else():
        if ((ad1 == name and kod1==parola) or (ad2==name and kod2==parola) or (ad3==name and kod3==parola) or (a3==name and b==parola)):
            print("Hoşgeldiniz :)")
        elif ((ad1 != name and kod1==parola) or (ad2!=name and kod2==parola) or (ad3!=name and kod3==parola) or (a3!=name and b==parola)):
            print("isim hatası :(")
        elif((ad1 == name and kod1!=parola) or (ad2==name and kod2!=parola) or (ad3==name and kod3!=parola) or (a3==name and b!=parola)):
            print("kod hatası :(")
        else:
            exit()                
    print("""
    ======================
    HERE IS SYBER SECURITY 
    ======================""")
    ad1 = "passs"
    kod1 = "123"
#--------------------------
    ad2 = "passs1"
    kod2 = "1234"
#--------------------------
    ad3 = "python"
    kod3 = "12345"

    print("yeni nick istermisin? evet (e), hayır (h)")
    cvb = input("evetmi / hayırmı : ")

    if (cvb =="e"):
        print("sizin için yeni ad oluşturuluyorrr")
        a=input("Isminizi giriniz:")    
        if ((a == ad1) or (a == ad2) or (ad3 ==a)):
            print("bu adda nick name var")
            a1 = input("Isminizi giriniz:")      
            if ((a1 == ad1) or (a1 == ad2) or (ad3 ==a1)):
                print("bu addada nick name var:(")
                a2 = input("Isminizi giriniz:")
                if ((a2 == ad1) or (a2 == ad2) or (ad3 ==a2)):
                    print("Çok üzgünüm bu adda tanımlı")
                    a3 = input("Isminizi giriniz:")
                    b = input("Şifre giriniz:")
                    name = (input("Emineyyet için isminizi birdaha girin :"))
                    parola = (input("Emineyyet için şifrenizide birdaha girin :"))
                    if_and_else()              
                else:
                    a3 = input("Isminizi giriniz:")
                    b = input("Şifre giriniz:")
                    name = (input("Emineyyet için isminizi birdaha girin :"))
                    parola = (input("Emineyyet için şifrenizide birdaha girin :"))
                    if_and_else()              
            else:
                a3 = input("Isminizi giriniz:")
                b = input("Şifre giriniz:")
                name = (input("Emineyyet için isminizi birdaha girin :"))
                parola = (input("Emineyyet için şifrenizide birdaha girin :"))
                if_and_else()                
        else:
            a3 = input("Isminizi giriniz:")
            b = input("Şifre giriniz:")
            name = (input("Emineyyet için isminizi birdaha girin :"))
            parola = (input("Emineyyet için şifrenizide birdaha girin :"))
            if_and_else()          
    else:
        print("Siz bilirsiniz")
    
    
    name = (input("Giriç için username :"))
    parola = (input("Giriç için parola :"))

    if_and_else()
    exit()

siber()
