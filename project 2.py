import random
#stone paper sissors
a=["stone","sissors","paper"]
b=random.choice(a)
input_play=input("Enter Stone,Paper or sissors withour=t spelling mistakes: ")
input_play.lower()
if b=="stone" and input_play=="stone":
    print("Computer Chose",b,"You Chose",input_play)
    print("Its a draw")
elif b=="stone" and input_play=="paper":
    print("Computer Chose",b,"You Chose",input_play)
    print("You Win")
elif b=="stone" and input_play=="sissors":
    print("Computer Chose",b,"You Chose",input_play)
    print("You Lose")
elif b=="paper" and input_play=="stone":
    print("Computer Chose",b,"You Chose",input_play)
    print("You Lose")
elif b=="paper" and input_play=="paper":
    print("Computer Chose",b,"You Chose",input_play)
    print("Its a Draw")
elif b=="paper" and input_play=="sissors":
    print("Computer Chose",b,"You Chose",input_play)
    print("You Win")
elif b=="sissors" and input_play=="stone":
    print("Computer Chose",b,"You Chose",input_play)
    print("You Win")
elif b=="sissors" and input_play=="paper":
    print("Computer Chose",b,"You Chose",input_play)
    print("You lose")
elif b=="sissors" and input_play=="sisssors":
    print("Computer Chose",b,"You Chose",input_play)
    print("Its a Draw")