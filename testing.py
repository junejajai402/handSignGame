import random
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
#client = MongoClient('localhost', 27017)


client = MongoClient('mongodb://localhost:27017')

db = client['pymongo_test']
posts = db.dataCollection

container=[1,2,3]
resolvers=['Rock','Paper','Scissors']
#print(random.choice(container))
val=0
score=[0,0]

g = input("Welcome to Rock Paper Scissors. Do you want to 1.See History or 2.Play the game: ")
g = int(g)
if g==1:
    print("You have chosen to see a history of all your plays")
    posts_data=list(posts.find())
    #print(posts_data)
    totNum = len(posts_data)
    print("Number of games played: %2d" %(totNum))
    numWins = len(list(posts.find({"playWin":1})))
    #list has some in memory issues. A more succinct approach would be to use loops to shave the data down
    print("Number of won games: %d" %(numWins))
    print("Number of lost games: %d" %(totNum-numWins))
    print()
    count=1
    for x in posts_data:
        winString = ""
        if x['playWin']==1:
            print("game %d: You won this game on %s with a score of %d to the computers score of %d" %(count,x['date'],x['playScore'],x['compScore']))
        else:
            print("game %d: You lost this game on %s with a score of %d to the computers score of %d" %(count,x['date'],x['playScore'],x['compScore']))
        count=count+1
elif g==2:
    print("Welcome to the Rock Paper Scissors game. First to 5 points wins")
    while True:
        g = input("Enter 1.Rock 2.Paper 3.Scissor: ")
        g = g.lower()
        if g=='rock':
            val=1
        elif g=='paper':
            val=2
        elif g=='scissor':
            val=3
        else:
            print("please enter rock, paper or scissor")
            continue
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
    winner=0
    if score[0]>score[1]:
        print("\nPlayer Wins. Good job")
        winner=1
    else:
        print("\nComputer Wins. Better luck next time")

    now=datetime.now()
    posts_data={
    'compScore': score[1],
    'playScore': score[0],
    'playWin': winner,
    'date': now.strftime("%m/%d/%Y, %H:%M:%S")
    }
    posts.insert_one(posts_data)
else:
    print("We have not developed beyond this yet. Thank You for your continued support and patience")
