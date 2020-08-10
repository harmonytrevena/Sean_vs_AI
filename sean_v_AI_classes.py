import random
#from pp_classes import Level
#from test2 import Question
import pygame
import pygame.font
import pygame.event
import pygame.draw
import os
import sys
from pygame.locals import * 


TOTAL_LEVELS = 4

pygame.init()

##Pygame functions and Constants
# Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Set screen for game and create clock variable for timing.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Message_Box():
    def __init__(self, font_size, x_cord, y_cord, screen):
        self.font_size = font_size
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.screen = screen
    def get_key(self):
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass
    def message_display(self,question1):
        x = self.font_size
        for line in question1:
            self.display_text(line, self.x_cord, (self.y_cord + x)  )
            x += self.font_size
        pygame.display.update()
    
    def display_text(self, message,x_cord, y_cord):
        fontobject = pygame.font.Font(None, self.font_size)
        #displays transparent unless display_background is called
        self.screen.blit(fontobject.render(message, 1, (0,0,0)),
        (( x_cord , y_cord )))

    def display_background(self, color, size_x, size_y):
        pygame.draw.rect(self.screen, color,
                       (self.x_cord,
                       self.y_cord,
                        size_x, size_y), 0)
    def ask(self, question): 
        #"ask(screen, question) -> answer"
        #pygame.font.init()        
        current_string = []
        self.display_text( question + "".join(current_string),139,291)
        while 1:
            inkey = get_key()
            if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey == K_ESCAPE:
                exit()
            elif inkey <= 127:
                current_string.append(chr(inkey))
            self.display_text( question + ": " + "".join(current_string),139,291)
        return "".join(current_string)
#Level Class, holds secret answer
class Level():
    def __init__(self,secret_code):
        self.secret_code = secret_code
#Question Class, holds questions for each level
class Question ():
    def __init__(self,question,answer, prompt):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.prompt = prompt
        #self.secret_code = secret_code

def message_display(question1):
    x = 0
    for line in question1:
        display_box_no_input(screen,line, 132, 21 + x  )
        x += 20
    pygame.display.update()
#Message functions for the game
##Functions to display messages on the game board./ Class makes these obsolete
def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass
#Takes 5 arguments Screen, a message to display, a screen size for the background, and a screen setup for the outline. Also takes an argument for font size.
def display_box_no_input(screen, message,x_cord , y_cord ,font_size =18):
    #"Print a message in a box in the middle of the screen"
    #This sets the background for the text input. 
    fontobject = pygame.font.Font(None, font_size)
    pygame.draw.rect(screen, (0, 0, 0),
                      (x_cord,
                      y_cord,
                       540, 20), 0)
    #This displays the messages
    screen.blit(fontobject.render(message, 1, (255, 255, 255)),
        (( x_cord , y_cord )))
            
    #pygame.display.flip()
    
#THis is used to ask for input from the user and doesn't need a key press to close
def display_box(screen, message,x_cord, y_cord):
    #"Print a message in a box in the middle of the screen"
    #This sets the background for the text input. 
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0),
                      (x_cord,
                      y_cord,
                       500, 20), 0)
    # pygame.draw.rect(screen, (255, 255, 255),
    #                   ((139 - 102,
    #                    screen.get_height() - 68,
    #                    404, 60), 1)
    #This displays the messages
    screen.blit(fontobject.render(message, 1, (255,255,255)),
        (x_cord, y_cord))
            
    pygame.display.flip()
    # while True:
    #     a_key = get_key()
    #     if a_key == K_RETURN:
    #         break
#Prompts user for input and uses display_box to display the prompts
def ask(screen, question): 
    #"ask(screen, question) -> answer"
    #pygame.font.init()        
    current_string = []
    display_box(screen, question + "".join(current_string),139,291)
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_ESCAPE:
            quit()
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string),139,291)
    return "".join(current_string)
def pause_get_key():
    while True:
        a_key = get_key()
        if a_key == K_RETURN:
            break  
     
#non-pygame functions used to house and display the level content
#random game code generator
def gen_codes(levels_in_game):
    alphabet = "abcdefghijkmnopqrstuvwxyz"
    x = 0
    y = 0
    code_string = ""
    secret_ans_array = []
    while x < levels_in_game:
        while y < random.randint(4,6):
            code_val = random.randint(0,34)
            if code_val < 25:
                code_string += alphabet[code_val]
            else:
                code_string += str(random.randint(0,9))
            y += 1
        y = 0
        secret_ans_array.append(code_string)
        code_string = ""
        x += 1
    return secret_ans_array
#function to create the game levels
#Worth removing
def game_level_create():
    #Create the level objects that carry the random encouragement and the secret answer
    ans_array = gen_codes(TOTAL_LEVELS)
    lvl1= Level(ans_array[0])
    lvl2= Level(ans_array[1])
    lvl3= Level(ans_array[2])
    lvl4= Level(ans_array[3])
    finallvlv = Level("42")
    level_arr = [lvl1,lvl2,lvl3, lvl4, finallvlv]
    print(ans_array)
    return level_arr
#Function to create the question objects
def question_obj_create():
    #Prompts for the asnwers, different by question and level
    LVL_1_PROMPT = "Solve the riddle with code provided"
    LVL_2_PROMPT = "Enter the missing code "
    LVL_4_PROMPT = 'Enter missing code'
    

    #Since each question is an object we have to initialize them all here.
    #Level 1 question initialized
    list_question_1 = Question(["list = ['the cat knows code', 'She worked as a Project Manager before attending DigitalCrafts',"," 'Today is not yesterday']", "clue1 = (list[0])", "clue2 = (list[0])", "clue3 = (list[1])", "clue4 = (list[2])", "print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[13:23])"], "the code worked yesterday",LVL_1_PROMPT)
    list_question_2 = Question(["list2 = ['The', 'REaSON', 'your', 'CODE', 'iS', 'NOT', 'working today....']"," letter_1 = (list2[1])"," letter_2 = (list2[4])","print('The ' + letter_1[2] + letter_2[0] + ' has leveled up and is now in contol of computer 1.')"], "ai",LVL_1_PROMPT)
    list_question_3 = Question(["list3 = ['d1r0w', '0113h']"," list3.reverse()"," print(list3)"], "hello world", LVL_1_PROMPT)
    dict_question_1 = Question(["computer_1 = {"," 'user': 'Sean',"," 'folder': 9,"," 'oh no': 'enemy found'","}","print(computer_1.pop('oh no'))"], "enemy found", LVL_1_PROMPT)

    dict_question_2 = Question(["player_skills = {","   'DigitalCrafts':{","      'programmer':{","         'name': 'sean',","         'skills':{","            'python': 70,","            'git and github': -1,","            'team work': 'Expert'","         }","       }","     }","   }"," print(player_skills['DigitalCrafts']['programmer']['name'])"], "sean","Last broken code")
    lvl1_ques_arr = [list_question_1,
     list_question_2,list_question_3, dict_question_1, dict_question_2
    ]


    #level 2 question initialization
    boolean_q_1 = Question(["if x __ 100:","    print(\"code\")","else:",    "print(\"you fail\")"], "==", LVL_2_PROMPT)
    boolean_q_2 = Question(["if x == 100:","    print(\"code\")","____:",    "print(\"you fail\")"], "else", LVL_2_PROMPT)
    boolean_q_3 = Question(["if x == 100:","    print(\"code\")","___ x > 100:","    print(\"try again\")","else:",    "print(\"you fail\")"], "elif", LVL_2_PROMPT)
    boolean_q_4 = Question(["if x == 100:","    print(\"code\")","elif x > 100:","____print(\"try again\")","else:",    "print(\"you fail\")"], "    ", LVL_2_PROMPT)
    boolean_q_5 = Question(["if AI == 'Evil':","    print(\"foiled\")","elif x > 100:","    print(\"try again\")","else:",    "print(\"you fail\")","AI = Evil"], "foiled", "Solve the code: ")
    lvl2_ques_arr = [boolean_q_1, boolean_q_2, boolean_q_3, boolean_q_4, boolean_q_5]
    
    #level 3 question initialization
    q1 = Question(["________ = [1,2,3,4,5,6,7,8,9,10]", "for i in num-list:" ,"    print(num-list[i])"], "num-list",LVL_4_PROMPT)
    q2 = Question(["extended-numlist = [0,1,2,3,4,Done!]", "for i in num-list:" ,"  print(___________________)  "], "extended-numlist",LVL_4_PROMPT)
    q3 = Question(["colors-list = [blue, yellow, green, red, purple]", "____________________" ,"    print(color-list[i])"], "for i in colors-list",LVL_4_PROMPT)
    q4 = Question(["computer-list = [Monitor, Motherboard, CPU, Hard Drive]", "for _ in computer-list:" ,"    print(computer-list[i])"], "i",LVL_4_PROMPT)
    lvl3_ques_arr = [q1, q2, q3, q4]

    #Level 4 questions initialized
    question1 = Question(["___ add(num1, num2):","   return num1 + num2"],"def",LVL_4_PROMPT)
    question2 = Question(["def add(num1_ num2):","   return num1 + num2"],",",LVL_4_PROMPT)

    #question3 = Question(["\ndef add_num1, num2):","   return num1 + num2"],"[",LVL_4_PROMPT)#won't work
    #question4 = Question(["\ndef add(num1, num2_:","   return num1 + num2"],"]",LVL_4_PROMPT)#won't work
    #question5 = Question(["\ndef add(num1, num2)_","  return num1 + num2"],";",LVL_4_PROMPT)#won't work
    question6 = Question(["def add(num1, num2):"," ____return num1 + num2"],"    ",LVL_4_PROMPT)
    question7 = Question(["def add(num1, num2)_","  ______ num1 + num2"],"return",LVL_4_PROMPT)
    question8 = Question(["def add(__________):","    return num1 + num2"],"num1, num2",LVL_4_PROMPT)
    question9 = Question(["def add(num1, num2):","    return num1 + num2","sum = ___(1,1)","print(sum)"],"add",LVL_4_PROMPT)
    lvl4_ques_arr = [ question1, question2, question6, question7,question8, question9]


    #endgame question
    final_question = Question(["class Warrior(SEAN):","def__init__(****, all_powers)", "super().__init__(your_passion)","****.your_passion = your_passion"],"self","Who can truly be the hero...? ")
    end_game_q = [final_question]
    #Array for all the question arrays
    questions_array=[lvl1_ques_arr, lvl2_ques_arr, lvl3_ques_arr, lvl4_ques_arr, end_game_q]
    return questions_array

level_arr = game_level_create()
questions_array =question_obj_create() 