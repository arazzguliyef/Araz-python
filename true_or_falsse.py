keyname="ad"
keycode="1234"
while(True):
    name=input("nick name please:")
    code=input("code please:")
    if((keyname==name) and (code==keycode)):
        print("wellcome",name)
        break
    elif((keyname!=name) and (code==keycode)):
         print("your nick name is not true")
         print('do you want to change? (Y/N)')
         answer=input()
         if(answer=="Y"):
             newnickname=input("new nick name please")
             print("just wait")
             keyname=newnickname
             print("your nick was cheinged")
    elif((keyname==name) and (code!=keycode)):
                 print("your code is not true")
                 print('do you want to change? (Y/N)')
                 answer=input()
                 if(answer=="Y"):
                     newcode=input("new code please")
                     print("just wait")
                     keycode=newcode
                     print("your code was cheinged")
    else:
        print("please try again")
