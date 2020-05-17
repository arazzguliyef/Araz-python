print("……….IELTS ACADEMIC READING SCORE………")
note=float(input('……..notunuzu girin lutfen:'))

def READING():
    if note>=40:
        print('9 Puan aldiniz')
    elif note>=37:    
        print(" 8.5 Puan aldiniz")
    elif note>=35:
        print('8 Puan aldiniz')
    elif note>=32:    
        print("7.5 Puan aldiniz")
    elif note>=30:
        print('7 Puan aldiniz')
    elif note>=26:    
        print("6.5 Puan aldiniz")
    elif note>=22:
        print('6 Puan aldiniz')
    elif note>=18:    
        print("5.5 Puan aldiniz")
    elif note>=15:
        print('5 Puan aldiniz')
    elif note>=14:   
        print("4.5 Puan aldiniz") 
    elif note>=10:
        print('4 Puan aldiniz')
    elif note>=8:    
        print("3.5 Puan aldiniz")
    elif note>=5:
        print('3 Puan aldiniz')
    elif note>=3:    
        print("2 Puan aldiniz")
    else:
        print("1 Puan aldiniz")
 
READING()
