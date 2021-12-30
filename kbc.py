print("                    !!!1WELCOME TO OUR GAME!!! ")
co=["red","blue","black","yellow","green"]
money=500
guess_co=["blue","black","pink"]
level=0
i=0
while i>=0:             
    j=1
    while j<=3:
        guess=input("guess the colour:")
        if guess in guess_co:
            print("you win the",money,"$","\U0001F917","\U0001F44F")
            # print("!!!welcome to",level+1, "level!!")
            mco=["orange","pink","purple","white","navy blue",]
            co.extend(mco)
            money=money+500
            level=level+1
            if level>3:
                break
            l=["hara","lightpink","orange"]
            guess_co.clear()
            guess_co.extend(l)
            if level>3:
                break
        else:
            if j+1==4:
                break
            print("wrong answer",j+1,"chance")
            # print("Do you want to play this game again!! nmru")
        j=j+1
    # print("Do you want to play this game again!! nmru")
    s= input("Do you want to play again enter yes/no:")
    if s=="yes":
        i=i+1
    else:
        print("GAME OVER{0_0}")
        break

