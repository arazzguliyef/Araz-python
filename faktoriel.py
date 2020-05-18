faktoriel =  1
while True:
    sayi=int(input("lutfen pozitif bir sayi giriniz:"))
    if(sayi <=0):
        print("???neqatif olmayan sayi giriniz???")
    else:
        for i in range(1, sayi + 1):
            faktoriel=faktoriel*i
        print("faktoriel",faktoriel)
        break
