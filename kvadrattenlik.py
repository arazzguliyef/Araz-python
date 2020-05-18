def tenlik():
    a = int(input("a parametresni girin:"))
    b = int(input("b parametresni girin:"))
    c = int(input("c parametresni girin:"))
    
    D = b**2 - (4 * a * c)
    x1= (-b + (D**0.5)) / (2*a)
    x2= (-b - (D**0.5)) / (2*a)
    print(a, b, c)
    print(x1, x2)
tenlik()

(#python language)
