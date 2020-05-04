import random

container=[1,2,3]
resolvers=['Rock','Paper','Scissors']
#print(random.choice(container))
val=0
score=[0,0]
while True:
    g = input("Enter 1.Rock 2.Paper 3.Scissor: ")
    g = g.lower()
    if g=='rock':
        val=1
    elif g=='paper':
        val=2
    else:
        val=3

    compgen_Val=random.choice(container)
    #print("compgen value %2d" %(compgen_Val))
    #print("Entered value %2d" %(val))
    if val==3 and compgen_Val==1:
        score[1]=score[1]+1
        print("You lose this round. Rock beats Scissors")
    elif val==1 and compgen_Val==3:
        score[0]=score[0]+1
        print("You win this round. Rock beats Scissors")
    elif compgen_Val>val:
        score[1]=score[1]+1
        print("You lose this round. %s beats %s" %(resolvers[compgen_Val-1],resolvers[val-1]))
    elif val>compgen_Val:
        score[0]=score[0]+1
        print("You win this round. %s beats %s" %(resolvers[val-1] ,resolvers[compgen_Val-1]))
    else:
        print("you both played the same hand sign. Its a draw")
        continue

    if score[0]==5 or score[1]==5:
        break
print("\nThe final score is computer: %2d player: %2d" %(score[1],score[0]))
if score[0]>score[1]:
    print("\nPlayer Wins. Good job")
else:
    print("\nComputer Wins. Better luck next time")
