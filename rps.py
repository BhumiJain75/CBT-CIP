import random
l=["rock","paper","scissors"]
while True:
    ccount=0
    ucount=0
    uc=int(input("""
       1 | Play Game
       2 | Exit
       Enter your choice: """))
       
    if uc==1:
        for a in range(1,10):
            user_input=int(input("""
            1 Rock
            2 Paper                     
            3 Scissors
            4 Quit
            Enter your choice: """))

            cchoice=random.choice(l) 
            if user_input==1:
                uchoice="rock"
            elif user_input==2:
                uchoice="paper"
            elif user_input==3:
                uchoice="scissors"
            else:
                print("Thank you for playing the game..I hope you enjoyed playing")
                break
            

            if cchoice==uchoice:
                print("Computer choice is:",cchoice)
                print("User choice is:",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and cchoice=="scissors") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissors" and cchoice=="paper"):
                print("Computer choice is:", cchoice)
                print("User choice is:",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer choice is:",cchoice)
                print("User choice is:",uchoice)
                print("Computer Win")
                ccount=ccount+1

        if ucount==ccount:
            print("Final Game Draw")
            print("User score:",ucount)
            print("Computer score:",ccount)
        elif ucount>ccount:
           print("Congrats You Win The Game ")
           print("User score:",ucount)
           print("Computer score:",ccount)
        else:
            print("Alas! You lost the Game...  Computer Win The Game ")
            print("User score:",ucount)
            print("Computer score:",ccount)
    else:
        print("Game exit...")
        break