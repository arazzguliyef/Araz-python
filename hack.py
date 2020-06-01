import itertools as t
chars=input("chars here: ")
n1=int(input("starting legenth here "))
n2=int(input("ending legenth here "))
f=input("file to save you let it blanck ")
if f=="" or f is None:
    if n1==n2:
        for l in t.product(chars, repeat=n1):
            s="".join(l)
            print (s)
    elif n2>n1:
        for i in range(n1, n2+1):
            for l in t.product(chars, repeat=i):
                s="".join(l)
                print (s)
    else:
        print ("starting legenth is not greather than ending legenth ")
else:
    with open(f,"w") as file:
        if n1==n2:
            for l in t.product(chars, repeat=n1):
                s="".join(l)
                file.write(s+"\n")        
        elif n2>n1:
            for i in range(n1, n2+1):
                for l in t.product(chars, repeat=i):
                    s="".join(l)
                    file.write(s+"\n")        
        else:
            print ("starting legenth is not greather than ending legenth ")
