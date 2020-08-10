
import pygame
import random
import math
from sean_v_AI_classes import Message_Box
from sean_v_AI_classes import message_display
from sean_v_AI_classes import level_arr
from sean_v_AI_classes import questions_array
from sean_v_AI_classes import pause_get_key
from sean_v_AI_classes import ask

#Intialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load("./music/2015-09-25_-_Old_Video_Game_Music_1_-_David_Fesliyan.wav")
pygame.mixer.music.play(loops=-1)
#Create the screen W,H
screen = pygame.display.set_mode((800,600))

narration_box = Message_Box(20, 445, 50, screen )    
#Background 
# background = pygame.image.load('bg.jpg')
#Title and Icon 
pygame.display.set_caption("Sean vs AI!")

#Player and initial player position
playerX = 175
playerY= 345
playerX_change = 0
playerY_change = 0

#Black background for screen
BLACK_BACKGROUND = (0,0,0)

#Image file variables
computerImg = pygame.image.load('./images/laptop.png')
computerImg_Comp = pygame.image.load('./images/Computer_Completed.png')
bossImg = pygame.image.load('./images/Final_Computer.png').convert_alpha()
text_box_image = pygame.image.load('./images/Text_Box.png').convert_alpha()
screenImg = pygame.image.load("./images/Game_Board.png").convert()
playerImg = pygame.image.load("./images/Sean_Front.png").convert_alpha()
computer_screen_Img = pygame.image.load("./images/computer_screen.png")
introImg = pygame.image.load("./images/Game_Opening_Screen.png").convert()
credit_screen = pygame.image.load("./images/Credit_Screen.png")
end_game_screen = pygame.image.load("./images/End_Game_Screen.png")

#computer flag
c1 = 0
c2 = 0
c3 = 0 
c4 = 0
c5 = 0

# computer position arrays
compx = [72,80,400,650,400]
compy = [113,368,368,368,108]

def computer (end_game):
    
    if c1 != 1 : 
        screen.blit(computerImg,(compx[0],compy[0])) 
    else:
        screen.blit(computerImg_Comp,(compx[0],compy[0]))  
    if c2 != 1 :
        screen.blit(computerImg,(compx[1],compy[1]))
    else:
        screen.blit(computerImg_Comp,(compx[1],compy[1]))
    if c3 != 1:
        screen.blit(computerImg,(compx[2],compy[2]))
    else:
        screen.blit(computerImg_Comp,(compx[2],compy[2]))
    if c4 != 1:
        screen.blit(computerImg,(compx[3],compy[3]))
    else:
        screen.blit(computerImg_Comp,(compx[3],compy[3]))
    #add endgame computer image only when endgame is triggered.
    if end_game: screen.blit(bossImg,(compx[4],compy[4]))

#player draw and coordinates 
def player(x,y):
    #Drawing image to screen
    screen.blit(playerImg,(x,y))

#Test to see if the computer is touched by player
def iscollision(alienX, alienY, bulletX, bulletY):
        #distance between two coordinates
        distance = math.sqrt(math.pow(alienX-bulletX,2)+math.pow(alienY-bulletY,2))
        if distance < 40:
            return True 
        else:
            return False

#Game Loop tests
running = True
end_game = False
first_run = True
first_comp = False
second_comp = False
third_comp = False
fourth_comp = False
flag = 0 #DON"T EVER CHANGE THIS

#Display opening card
screen.blit(introImg,(0,0))
#narration_box.message_display([""])
pygame.display.update()
pause_get_key()


#Start the game
while running:    

    if flag != 1:
        #Background Color (RGB Values)
        screen.blit(screenImg,(0,0))

    #Gets events from inside the Pygame screen
    for event in pygame.event.get():
        #Checking if x quit button is pressed
        if event.type == pygame.QUIT:
            exit()
            running = False 
        #if a keystroke is pressed check whether right or left 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
                playerImg = pygame.image.load("./images/Sean_Walking_Left.png").convert_alpha()
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
                playerImg = pygame.image.load("./images/Sean_Walking_Right.png").convert_alpha()
            if event.key == pygame.K_UP:
                playerY_change = -4
                playerImg = pygame.image.load("./images/Sean_Float_Up.png").convert_alpha()
            if event.key == pygame.K_DOWN:
                playerY_change = 4
                playerImg = pygame.image.load("./images/Sean_Down.png").convert_alpha()
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerImg = pygame.image.load("./images/Sean_Walking_Right_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0
            if event.key == pygame.K_LEFT:
                playerImg = pygame.image.load("./images/Sean_Walking_Left_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0
            if event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0
            if event.key == pygame.K_DOWN:
                playerImg = pygame.image.load("./images/Sean_Front.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

    #Starts interaction with different computers
    collision1 = iscollision(compx[0],compy[0],playerX,playerY)
    if collision1 and c1 != 1:
        c1 = 1
        #used to make it easier to c/p the different comps 
        x = 0
        print(x)
        #screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        while True:
            message_display([f"D4v1d_AI: I got the first code, try {level_arr[x].secret_code}"])
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    # screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    break
            screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])
        first_comp = True    
        pause_get_key()
        screen.blit(screenImg,(0,0))

    collision2 = iscollision(compx[1],compy[1],playerX,playerY)
    if collision2 and c2 != 1:
        c2 = 1
        x = 1
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])    
        pause_get_key()
        second_comp = True
        screen.blit(screenImg,(0,0))

    collision3 = iscollision(compx[2],compy[2],playerX,playerY)
    if collision3 and c3 != 1:
        c3 = 1
        x = 2
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])    
        pause_get_key()
        third_comp = True
        screen.blit(screenImg,(0,0))

    collision4 = iscollision(compx[3],compy[3],playerX,playerY)
    if collision4 and c4 != 1:
        c4 = 1
        x = 3
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is 42","Enemy AI Brain revealed!!"])    
        pause_get_key()
        fourth_comp = True
        #end_game= True
        screen.blit(screenImg,(0,0))
    #End_game computer
    collision5 = iscollision(compx[4],compy[4],playerX,playerY)
    if collision5 and c5 != 1 and end_game:
        c5 = 1
        x = 4
        print(x)
        #Background Image
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!","For it is truly the answer to the universe", "Press [ENTER] to access the enemy AI Brain"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
                    break
            screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('./images/computer_screen.png'),(0,0))
        message_display(["You have defeated the evil AI and restored DigitalCrafts!!", "Press [ENTER] to destroy the AI!!"])
        pause_get_key()
        running = False
        flag = 1
    
    #drawing the player on the screen
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0 
    elif playerX >= 625: 
        playerX = 625
    if playerY <= 0:
        playerY = 0 
    elif playerY >= 345:
        playerY = 345




    #function to display computer and player if the player is not on the computer
    if flag != 1:
        computer(end_game)
        #function to display player
        player(playerX,playerY)
        
        if first_run:
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["Error Errror Error... Something is going wrong.", "This is DigitalCraft's AI D4v1D.....","If you can hear me press [ENTER]"])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: I am currently under attack.","Four of my databases have been compromised."])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: You will need to use your", "prework skills to get the system back up.","Proceed upstairs to fix the first computer."])
            pause_get_key()
            first_run = False
        if first_comp:
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: Well Done. ","You've unlocked the first computer.", "Head downstairs to unlock the second computer."])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["Keep your secret code.", "You will use it to unlock the next computer."])
            pause_get_key()
            first_comp = False
        if second_comp:
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: Amazing. ","You've unlocked the second computer.", "Head over to unlock the third computer."])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: The AI is messing with my code.","We will have to keep fixing it","to keep my systems running..."])
            pause_get_key()
            second_comp = False
        if third_comp:
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["David_AI: You're crushing it!!","You've unlocked the third computer!!"])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["The AI is hiding in another computer.", "Head to the fourth computer to continue."])
            pause_get_key()
            third_comp = False
        if fourth_comp:
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["D4v1d_AI: The evil AI database has appeared.","Let's head to the roof to shut it down."])
            pause_get_key()
            screen.blit(text_box_image,(0,0))
            narration_box.message_display(["You'll need to use all your skills.", "It is just one more computer to shut it down."])
            pause_get_key()
            fourth_comp = False
            end_game = True
    pygame.display.update()

while True:
    screen.blit(end_game_screen,(0,0))
    pygame.display.update()
    pause_get_key()
    screen.blit(credit_screen,(0,0))
    pygame.display.update()
    pause_get_key()
    break

