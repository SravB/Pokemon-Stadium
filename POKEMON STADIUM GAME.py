#POKEMON BATTLE
#BY: SOURAV B.


#imports

from tkinter import *
from random import *
from time import *
import winsound


root = Tk()
screen = Canvas(root, width = 900, height = 800, background = "white")
screen.pack()

#background

imageA = PhotoImage(file="pokemon stadium.gif")
createImageA = screen.create_image(458, 410, image=imageA)

#setting up data

CharizardHP = 315
BlastoiseHP = 330

fireChoices = ["red","orange","orange red","gold"]
waterChoices = ["cyan","aquamarine","blue","royal blue"]

Charizard = []
Blastoise = []

firedots = []
waterdots = []

ChHP = []
BlHP = []

ChHPtag = []
BlHPtag = []

CharCenX = 200
CharCenY = 400

BlasCenX = 700
BlasCenY = 400

#health bars

ChHP.append(screen.create_rectangle(CharCenX-158,80,CharCenX+157,130,fill = "green")) #health bars
BlHP.append(screen.create_rectangle(BlasCenX-165,80,BlasCenX+165,130,fill = "green"))

screen.create_text(CharCenX,50,text = "Charizard HP",fill = "white",font = "arial 20") #name labels
screen.create_text(BlasCenX,50,text = "Blastoise HP",fill = "white",font = "arial 20")

ChHPtag.append(screen.create_text(CharCenX+105,150,text = str(CharizardHP) + "/315",fill = "white",font = "arial 17")) #health labels
BlHPtag.append(screen.create_text(BlasCenX+120,150,text = str(BlastoiseHP) + "/330",fill = "white",font = "arial 17"))

#pokemon images

image1 = PhotoImage(file="charizard good.gif")
createImage1 = screen.create_image(CharCenX, CharCenY, image=image1)
Charizard.append(createImage1)

image2 = PhotoImage(file="blastoise good.gif")
createImage2 = screen.create_image(BlasCenX, BlasCenY, image=image2)
Blastoise.append(createImage2)

screen.update()

def CharHP(damage): #Charizard's health bar animation
    
    for f in range(0,3):
        
        screen.delete(Charizard[0]) #damage animation
        Charizard.remove(Charizard[0])
        screen.update()
        sleep(0.15)
        createImage1 = screen.create_image(CharCenX, CharCenY, image=image1)
        Charizard.append(createImage1)
        screen.update()
        sleep(0.15)
        
    for i in range(1,damage+1): #actual health bar animation
        
        screen.delete(ChHP[0])
        ChHP.remove(ChHP[0])
        CHP = CharizardHP - i
        start = CharCenX-158
        
        screen.delete(ChHPtag[0])
        ChHPtag.remove(ChHPtag[0])
        
        if len(ChHPtag) == 1:
            screen.delete(ChHPtag[0])
            ChHPtag.remove(ChHPtag[0])

        if CHP <= 0:
            h = ChHPtag.append(screen.create_text(CharCenX+105,150,text = "0/315",fill = "white",font = "arial 17"))
        else:
            h = ChHPtag.append(screen.create_text(CharCenX+105,150,text = str(CHP) + "/315",fill = "white",font = "arial 17"))

        if CHP >= 200:
            a = screen.create_rectangle(start,80,start+(CHP),130,fill = "green")
        elif CHP >= 100:
            a = screen.create_rectangle(start,80,start+(CHP),130,fill = "yellow")
        elif CHP > 0:
            a = screen.create_rectangle(start,80,start+(CHP),130,fill = "red")
        else:
            a = screen.create_rectangle(start,80,start,130,fill = "",outline = "")
        ChHP.append(a)
        
        ChHPtag.append(h)
        screen.update()
        sleep(0.025)
    

def BlasHP(damage): #Blastoise's health bar animation
    
    for f in range(0,3):
        
        screen.delete(Blastoise[0]) #damage animation
        Blastoise.remove(Blastoise[0])
        screen.update()
        sleep(0.15)
        createImage2 = screen.create_image(BlasCenX, BlasCenY, image=image2)
        Blastoise.append(createImage2)
        screen.update()
        sleep(0.15)
        
    for i in range(1,damage+1): #actual health bar animation
        
        screen.delete(BlHP[0])
        BlHP.remove(BlHP[0])
        BHP = BlastoiseHP - i
        start = BlasCenX-165

        screen.delete(BlHPtag[0])
        BlHPtag.remove(BlHPtag[0])
        
        if len(BlHPtag) == 1:
            screen.delete(BlHPtag[0])
            BlHPtag.remove(BlHPtag[0])

        if BHP <= 0:
            h = BlHPtag.append(screen.create_text(BlasCenX+120,150,text = "0/330",fill = "white",font = "arial 17"))
        else:
            h = BlHPtag.append(screen.create_text(BlasCenX+120,150,text = str(BHP) + "/330",fill = "white",font = "arial 17"))
        
        if BHP >= 200:
            b = screen.create_rectangle(start,80,start+(BlastoiseHP - i),130,fill = "green")
        elif BHP >= 100:
            b = screen.create_rectangle(start,80,start+(BlastoiseHP - i),130,fill = "yellow")
        elif BHP > 0:
            b = screen.create_rectangle(start,80,start+(BlastoiseHP - i),130,fill = "red")
        else:
            b = screen.create_rectangle(start,80,start,130,fill = "",outline = "")
        BlHP.append(b)
        
        screen.update()
        sleep(0.025)



t = 1 #time used to recreate old fashioned style of pokemon in the early generations

#allows multiplayer!


#Blastoise is slightly overpowered... but it would be too easy if he wasn't :)


player2 = input("Would you like to play against another player? (y/n) ") #INPUT

playAgain = "y"

if player2 == "y":
    score1 = 0
    score2 = 0

else:
    score = 0

while playAgain == "y": #first main boolean condition


    winsound.PlaySound("Pok_mon_-_Red_Blue_Champion_Battle_Music_",winsound.SND_ASYNC) #MAIN AUDIO


    CharizardHP = 315
    BlastoiseHP = 330

    ChHP.append(screen.create_rectangle(CharCenX-158,80,CharCenX+157,130,fill = "green")) #health bars
    BlHP.append(screen.create_rectangle(BlasCenX-165,80,BlasCenX+165,130,fill = "green"))

    for item in ChHPtag:
            screen.delete(item)
            ChHPtag.remove(item)

    for item in BlHPtag:
            screen.delete(item)
            BlHPtag.remove(item)

    ChHPtag.append(screen.create_text(CharCenX+105,150,text = str(CharizardHP) + "/315",fill = "white",font = "arial 17")) #health labels
    BlHPtag.append(screen.create_text(BlasCenX+120,150,text = str(BlastoiseHP) + "/330",fill = "white",font = "arial 17"))
    
    screen.update()

    #Welcome

    print("Welcome to Pokemon Stadium. It is the final battle between Ash's Charizard and Gary's Blastoise.")

    if player2 == "y":
        print("Player 1 is Ash. Player 2 is Gary.")
    else:
        print("You are Ash. Defeat Gary.")

    
    CharizardType = "Fire" #these pokemon types are mostly for show, but they may become of use in the future when more pokemon are introduced to the battle
    OppType = "Water"

    #Charizard

    CharizardMoves = ["Flamethrower","Seismic Toss","Fly","Slash"] #the functions are mostly "notes" used to help organize the code

    def Flamethrower():
        damage = randint(90,110) #miss = %85
        return damage
    def SeismicToss():
        damage = randint(85,95) #miss = %90
        return damage
    def Fly():
        damage = randint(72,88) #miss = %95
        return damage
    def Slash():
        damage = randint(70,83) #miss = %95
        return damage

    #Blastoise

    BlastoiseMoves = ["Hydro Pump","Skull Bash","Rapid Spin","Surf"]

    def HydroPump():
        damage = randint(95,115) #miss = %70
        return damage
    def SkullBash():
        damage = randint(90,110) #miss = %80
        return damage
    def RapidSpin():
        damage = randint(63,77) #miss = %95
        return damage
    def Surf():
        damage = randint(81,99) #miss = %85
        return damage

    #miss chance

    def miss(x):
        m = randint(1,100)
        if m > x:
            return "You missed!"
        else:
            return "Direct hit!"

    faint = False

    #Battle Sequence
    
    sleep(t)
    
    while faint == False: #second main boolean condition
        
        #the two conditions are seperated in order to improve gameplay
        
        print("Charizard has " + str(CharizardHP) + " HP and Blastoise has " + str(BlastoiseHP) + " HP.\n")
        
        #summarizes hp totals after every sequence of moves
        
        sleep(t)
        print("It is Charizard's move.")
        sleep(t)
        print(CharizardMoves)
        sleep(t)
        if CharizardHP < 100:
                    print("Charizard is low on HP! Charizard's special blaze ability is now in effect! Charizard's fire type moves are powered up!")
                    sleep(t)

        ##
        #checking for valid input
                    
        Chmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """) #INPUT
        sleep(t)
        while Chmove.isdigit() == True:
            if int(Chmove) > 0 and int(Chmove) < 5:
                break
            else:
                print("Sorry that's not a valid move. Please try again.")
                sleep(t)
                Chmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """)
                sleep(t)
        while Chmove.isdigit() == False:
            print("Sorry that's not a valid move. Please try again.")
            sleep(t)
            Chmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """)
            sleep(t)
            if Chmove.isdigit() == True:
                if int(Chmove) > 0 and int(Chmove) < 5:
                    break
                else:
                    Chmove = "a"
        Cmove = int(Chmove)
        
        ##
        
        Charmove = CharizardMoves[Cmove-1]
        if Charmove == "Flamethrower": #flame animation
            moveType = "Fire"
            damagethisTurn = Flamethrower()   
            missC = miss(85)
            if missC == "Direct hit!":
                for f in range(0,500,2):
                    fy = int(f/8)
                    fireColor = choice(fireChoices)
                    delta = randint(6,15)
                    x = randint(CharCenX-10+f,CharCenX+10+f)
                    y = randint(CharCenY-45+fy,CharCenY-30+fy)
                    firedots.append(screen.create_polygon(x,y,int(x+delta/2),int(y-delta/4),int(x+delta*2),int(y+delta/4),fill = fireColor,outline = fireColor,smooth = True))
                    screen.update()
                    sleep(0.004)

                for fire in range(0,250):
                    sleep(0.004)
                    screen.delete(firedots[0])
                    firedots.remove(firedots[0])
                    screen.update()
                sleep(t)


        if Charmove == "Seismic Toss":
            moveType = "Fighting" #these moveTypes are move for accessory than effect, only the water and fire ones matter
            damagethisTurn = SeismicToss()
            missC = miss(90) #toss animation
            if missC == "Direct hit!":
                BlasH = BlasCenY
                for f in range(0,200,2):
                    BlasH = BlasH - f
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasCenX, BlasH, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                for f in range(0,200,2):
                    BlasH = BlasH + f
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasCenX, BlasH, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                sleep(t)
                    
                    
        if Charmove == "Fly": #fly animation
            moveType = "Flying"
            damagethisTurn = Fly()
            missC = miss(95)
            if missC == "Direct hit!":
                CharH = CharCenY
                for f in range(0,200,2):
                    CharH = CharH - f
                    screen.delete(Charizard[0])
                    Charizard.remove(Charizard[0])
                    createImage1 = screen.create_image(CharCenX, CharH, image=image1)
                    Charizard.append(createImage1)
                    screen.update()
                    sleep(0.01)
                for f in range(0,200,2):
                    CharH = CharH + f
                    screen.delete(Charizard[0])
                    Charizard.remove(Charizard[0])
                    createImage1 = screen.create_image(BlasCenX, CharH, image=image1)
                    Charizard.append(createImage1)
                    screen.update()
                    sleep(0.01)
                for f in range(0,200,2):
                    CharH = CharH - f
                    screen.delete(Charizard[0])
                    Charizard.remove(Charizard[0])
                    createImage1 = screen.create_image(BlasCenX, CharH, image=image1)
                    Charizard.append(createImage1)
                    screen.update()
                    sleep(0.01)
                for f in range(0,200,2):
                    CharH = CharH + f
                    screen.delete(Charizard[0])
                    Charizard.remove(Charizard[0])
                    createImage1 = screen.create_image(CharCenX, CharH, image=image1)
                    Charizard.append(createImage1)
                    screen.update()
                    sleep(0.01)
                sleep(t)
                    
        if Charmove == "Slash": #slash animation
            moveType = "Normal"
            damagethisTurn = Slash()
            missC = miss(95)
            if missC == "Direct hit!":
                slAA = screen.create_line(BlasCenX-30,BlasCenY-60,BlasCenX+60,BlasCenY+30,fill = "grey", width = 7)
                slBB = screen.create_line(BlasCenX-50,BlasCenY-50,BlasCenX+50,BlasCenY+50,fill = "grey", width = 7)
                slCC = screen.create_line(BlasCenX-60,BlasCenY-30,BlasCenX+30,BlasCenY+60,fill = "grey", width = 7)
                slA = screen.create_line(BlasCenX-30,BlasCenY-60,BlasCenX+60,BlasCenY+30,fill = "black", width = 3)
                slB = screen.create_line(BlasCenX-50,BlasCenY-50,BlasCenX+50,BlasCenY+50,fill = "black", width = 3)
                slC = screen.create_line(BlasCenX-60,BlasCenY-30,BlasCenX+30,BlasCenY+60,fill = "black", width = 3)
                screen.update()
                sleep(1)
                screen.delete(slA,slB,slC,slAA,slBB,slCC)
                sleep(t)
                
        print(missC)
        sleep(t)
        if missC == "Direct hit!":
            if moveType == "Fire":
                print("It wasn't very effective.")
                sleep(t)
                damagethisTurn = int(damagethisTurn * 0.7)
                if CharizardHP < 100:
                    print("Charizard's special blaze ability came into effect! Charizard's fire type moves are powered up!")
                    sleep(t)
                    damagethisTurn = int(damagethisTurn * 1.8)
            if player2 == "y":
                message = "Player 1"
            else:
                message = "You"
                
            ###
            BlasHP(damagethisTurn)
            ###
            
            print(message + " dealt " + str(damagethisTurn) + " damage!")
            sleep(t)
            BlastoiseHP = BlastoiseHP - damagethisTurn
            if BlastoiseHP < 0:
                BlastoiseHP = 0
            print("Blastoise has " + str(BlastoiseHP) + " HP left.")
            sleep(t)
            if BlastoiseHP <= 0:
                winsound.PlaySound("pokemon_victory_theme",winsound.SND_ASYNC) #VICTORY AUDIO 
                print("Blastoise fainted.")
                sleep(t)
                if player2 == "y":
                    print("Player 1 won!")
                    sleep(t)
                    score1 = score1 + 1
                else:
                    print("You win!")
                    sleep(t)
                    score = score + 1
                break
        else:
            if player2 == "y":
                message = "Player 2"
            else:
                message = "Your opponent"
            print(message + " dodged your move!")
            sleep(t)
        if BlastoiseHP < 100:
                    print("Blastoise is low on HP! Blastoise's special torrent ability is now in effect! Blastoise's water type moves are powered up!")
                    sleep(t)
        if player2 == "y": #if the user wants to play against a friend, this code is used
            print("It is Blastoise's move.")
            sleep(t)
            print(BlastoiseMoves)
            sleep(t)

            ##
            #checking for valid input
            
            Blmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """) #INPUT
            sleep(t)
            while Blmove.isdigit() == True:
                if int(Blmove) > 0 and int(Blmove) < 5: #checking for valid input
                    break
                else:
                    print("Sorry that's not a valid move. Please try again.")
                    sleep(t)
                    Blmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """)
                    sleep(t)
            while Blmove.isdigit() == False:
                print("Sorry that's not a valid move. Please try again.")
                sleep(t)
                Blmove = input("""Choose your move. (1 for first move, 2 for second move, 3 for third move and 4 for fourth move) """)
                sleep(t)
                if Blmove.isdigit() == True:
                    if int(Blmove) > 0 and int(Blmove) < 5:
                        break
                    else:
                        Blmove = "a"
            Bmove = int(Blmove)
            
            ##
            
            Blasmove = BlastoiseMoves[Bmove-1]
        else:
            Bmove = randint(0,3) #if the user wants to play against a computer, this code is used
            Blasmove = BlastoiseMoves[Bmove]
            print("Blastoise used " + Blasmove + "!")
            sleep(t)
        if Blasmove == "Hydro Pump":
            moveType = "Water"
            damageTurn = HydroPump()
            missC = miss(70) #hydro pump animation
            if missC == "Direct hit!":
                for f in range(0,500,2):
                    fy = int(f/8)
                    waterColor = choice(waterChoices)
                    delta = randint(6,15)
                    x = randint(BlasCenX-50-f,BlasCenX-30-f)
                    y = randint(BlasCenY-42+fy,BlasCenY-27+fy)
                    waterdots.append(screen.create_polygon(x,y,int(x+delta/2),int(y-delta/4),int(x+delta*2),int(y+delta/4),fill = waterColor,outline = waterColor,smooth = True))
                    screen.update()
                    sleep(0.004)

                for water in range(0,250):
                    sleep(0.004)
                    screen.delete(waterdots[0])
                    waterdots.remove(waterdots[0])
                    screen.update()
                sleep(t)
             
        if Blasmove == "Skull Bash":
            moveType = "Normal"
            damageTurn = SkullBash()
            missC = miss(80) #skull bash animation
            if missC == "Direct hit!":
                for f in range(0,100):
                    BlasW = BlasCenX - f*5
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasW, BlasCenY, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                sleep(0.25)
                for f in range(0,100):
                    x1 = CharCenX - f
                    y1 = CharCenY - f
                    x2 = CharCenX + f
                    y2 = CharCenY + f
                    c = screen.create_oval(x1,y1,x2,y2,outline = "black",width = 3)
                    screen.update()
                    sleep(0.01)
                    screen.delete(c)
                sleep(0.25)
                for f in range(0,100):
                    BlasW = BlasCenX - 495 + f*5
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasW, BlasCenY, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                sleep(t)
                    
        if Blasmove == "Rapid Spin":
            moveType = "Normal"
            damageTurn = RapidSpin()
            missC = miss(95) #rapid spin animation
            if missC == "Direct hit!":
                for f in range(0,300,10):
                    BlasW = BlasCenX - f
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasW, BlasCenY, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                for f in range(0,300,10):
                    BlasW = BlasCenX - 299 + f
                    screen.delete(Blastoise[0])
                    Blastoise.remove(Blastoise[0])
                    createImage2 = screen.create_image(BlasW, BlasCenY, image=image2)
                    Blastoise.append(createImage2)
                    screen.update()
                    sleep(0.01)
                sleep(t)

        if Blasmove == "Surf":
            moveType = "Water"
            damageTurn = Surf()
            missC = miss(85)
            if missC == "Direct hit!": #surf animation
                for f in range(0,4000,2):
                    waterColor = choice(waterChoices)
                    delta = randint(6,15)
                    x = randint(BlasCenX-100-int(f/8),BlasCenX-75-int(f/8))
                    y = randint(BlasCenY-125,BlasCenY+125)
                    waterdots.append(screen.create_polygon(x,y,int(x+delta/2),int(y-delta/4),int(x+delta*2),int(y+delta/4),fill = waterColor,outline = waterColor,smooth = True))
                    screen.update()
                    sleep(0.0002)

                for water in range(0,2000):
                    sleep(0.0002)
                    screen.delete(waterdots[0])
                    waterdots.remove(waterdots[0])
                    screen.update()
                sleep(t)
                    
        if missC == "Direct hit!":
            print(missC)
            sleep(t)
            if moveType == "Water":
                print("It was super effective!")
                sleep(t)
                damageTurn = int(damageTurn * 1.25)
                if BlastoiseHP < 100:
                    print("Blastoise's special torrent ability came into effect! Blastoise's water type moves are powered up!")
                    sleep(t)
                    damageTurn = int(damageTurn * 1.3)
            if player2 == "y":
                message = "Player 2"
            else:
                message = "Blastoise"
                
            ###
            CharHP(damageTurn)
            ###
            
            print(message + " dealt " + str(damageTurn) + " damage!")
            sleep(t)
            CharizardHP = CharizardHP - damageTurn
            if CharizardHP < 0:
                CharizardHP = 0
            print("Charizard has " + str(CharizardHP) + " HP left.")
            sleep(t)
        else:
            if player2 == "y":
                print("Player 1 dodged your move!")
                sleep(t)
            else:
                print("You dodged your opponent's move!")
                sleep(t)
        if CharizardHP <= 0:
            print("Charizard fainted.")
            sleep(t)
            if player2 == "y":
                winsound.PlaySound("pokemon_victory_theme",winsound.SND_ASYNC) #VICTORY AUDIO
                print("Player 2 won!")
                sleep(t)
                score2 = score2 + 1
            else:
                print("You lose.")
                sleep(t)
                score = score - 1
            faint = True

    if player2 == "y": #summarizing the scores
        print("Player 1's score is " + str(score1) + " while Player 2's score is " + str(score2))
    else:
        print("Your current score is " + str(score))
    print("")
    playAgain = input("Would you like to play again? (y/n): ")#INPUT
    print("")

#Scoring System
    
#another quick summary for multiplayer

if player2 == "y": #deciding winner
    if score1 > score2:
        print("Player 1 is the pokemon champion!")
    elif score1 == score2:
        print("Player 1 tied Player 2!")
    else:
        print("Player 2 is the pokemon champion!")

else:

#Ranking System
    
#another quick summary for single player

    if score < 0:
        print("You can't be a pokemon trainer with those skills. You need to train harder!")
    elif score < 3:
        print("Not bad.. for a beginner. You are a pokemon rookie.")
    elif score < 10:
        print("You have been training... You are an expert trainer!")
    else:
        print("You are the very best, like no one ever was. Congratulations! You have achieved the rank of pokemon master! But the real question is, can you do it again? There's only one way to find out!")
        
