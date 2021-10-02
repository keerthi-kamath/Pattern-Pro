import tkinter as tk
from tkinter import *

import random
import time 
import requests
import json
import sys
from patterns import *
import pygame
import os
pygame.init()


#First interface with pygame
window= pygame.display.set_mode((500,500))

#Background image for pygame window
char = pygame.image.load(r"pattern.png")

#Defining all required colours
black = (0,0,0)
white = (255,255,255)
green = (127,197,163)
red = (211,78,78)
bright_red=(211,0,0)
bright_green=(0,197,102)

#Defining a clock if needed
clock = pygame.time.Clock()

#Function to load the image to the background
def bg(x,y):
    gamedisplay.blit(char,(x,y))

#Function to load text onto the buttons

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

#Defining screen parameters
x = (500*0.45)
y = (500*0.8)

x = 50
y= 440
width = 40
height = 60
vel =5

#Function to quit on pygame

def quitgame():
    pygame.quit()
    quit()

#Function to make the button active
def button(msg,x,y,w,h,ac,ic,action=None):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(window,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action == "Start":
                pygame.quit()
                game()
            if action == "Quit":
                quitgame()
    else:
        pygame.draw.rect(window,ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)
    clock.tick(15)
def reset():
        os.execl(sys.executable,r"C:\Users\ADMIN\Desktop\jop","GUI_08.py")


def redrawGameWindow():

    window.blit(char,(0,0))

#Main Game Programme
run = True
while run:

    for event in pygame.event.get():
        #Suppose the user wants to quit
        if event.type==pygame.QUIT:
            run = False
    #Draw two rectangles
    pygame.draw.rect(window, green,(100,425,80,50))
    pygame.draw.rect(window, red,(300,425,80,50))

    #Add texts to the rectangles and make them functional
    button("Start",100,425,80,50,bright_green,green,"Start")
    button("Quit",300,425,80,50,bright_red,red,"Quit")

    def closewidgets(self):
        self.quit()


    def game():
        root= tk.Tk()
        root.geometry("500x500+100+100")

        #Define the dimensions of first window
        canvas_width = 400
        canvas_height = 500

        #Define the position of the first icon in the first window
        one_firstx = 80
        one_firsty = 50


        #Create and place the first window and the labels

        canvas1 = tk.Canvas(root, width = canvas_width, height = canvas_height,  relief = 'raised')

        canvas1.pack()

        #Creating required labels in window 1
        label_welcome = tk.Label(root, text='WELCOME')
        label_welcome.config(font=('cambria', 15, 'bold'))
        canvas1.create_window((canvas_width/2), one_firsty, window=label_welcome)

        second_label = tk.Label(root, text='Enter number of players:')
        second_label.config(font=('cambria', 10))
        canvas1.create_window(one_firstx, one_firsty + 45, window=second_label)

        third_label = tk.Label(root, text='Enter Player1 Name:',font=('cambria', 10))

        entry1 = tk.Entry (root) 
        canvas1.create_window((one_firstx+150), one_firsty + 45, window=entry1)

        #Creating Required Entries in window 1

        entry_create = tk.Entry(root)

        #temporary list for player number updates
        numbers = [1]

        #temporary list for player name updates
        temp_list2 = [0]

        #Lists required for the game
        Players = []
        Guesses = []
        Incorrect = []
        All_answers = []

        #Temporary list to change turns
        PlayerChange = [0]

        #Message to display if there is no player name
        var = StringVar()
        no_playername = tk.Message(root, textvariable=var, relief=RAISED )
        var.set("Please enter a player name")

        #Function to end game on tkinter
        def end_game():
            exit()


        #Play Button
        def play_game():
            # root.destroy()
            root2= tk.Tk()
            root2.geometry("500x500+100+100")
            canvas2 = tk.Canvas(root2, width = canvas_width, height = canvas_height,  relief = 'raised')
            canvas2.pack()

            fourth_label = tk.Label(root2, text='PATTERN PRO!')
            fourth_label.config(font=('cambria',15,'bold'))
            canvas2.create_window((canvas_width/2),one_firsty, window=fourth_label)


            def pattern():
                patterns= ['animals','fruits','colors','birds','constellations','countries',"vehicles","tools","instruments","body parts","Planets","World famous palaces&monuments","Top Watch Company","Chocolate Brands"]
                pick = random.choice(patterns) 
                # pick=patterns[0]
                return pick 
            def method(pick):
                if pick=="animals":
                        a  = animal_list[random.randint(0,len(animal_list)-1)]
                        temp_patternlist = animal_list
                elif pick=='fruits':
                        a= fruit_list[random.randint(0,len(fruit_list)-1)]
                        temp_patternlist = fruit_list
                elif pick=='colors':
                        a= color_list[random.randint(0,len(color_list)-1)]
                        temp_patternlist = color_list
                elif pick=='birds':
                        a= bird_list[random.randint(0,len(bird_list)-1)]
                        temp_patternlist = bird_list
                elif pick=='constellations':
                        a= Constellation_list[random.randint(0,len(Constellation_list)-1)]
                        temp_patternlist = Constellation_list
                elif pick=='countries':
                        a= Country_list[random.randint(0,len(Country_list)-1)]
                        temp_patternlist = Country_list
                elif pick=="vehicles":
                        a= Vehicles_list[random.randint(0,len(Vehicles_list)-1)]
                        temp_patternlist = Vehicles_list
                elif pick=="tools":
                        a= Tools_list[random.randint(0,len(Tools_list)-1)]
                        temp_patternlist = Tools_list
                elif pick=="instruments":
                        a= Instruments_list[random.randint(0,len(Instruments_list)-1)]
                        temp_patternlist = Instruments_list
                elif pick=="body parts":
                        a= Body_parts_list[random.randint(0,len(Body_parts_list)-1)]
                        temp_patternlist = Body_parts_list
                elif pick=="Planets":
                        a= Planets_list[random.randint(0,len(Planets_list)-1)]
                        temp_patternlist = Planets_list
                elif pick=="World famous palaces&monuments":
                        a= P_M_list[random.randint(0,len(P_M_list)-1)]
                        temp_patternlist = P_M_list
                elif pick=="Top Watch Company":
                        a= Watch_list[random.randint(0,len(Watch_list)-1)]
                        temp_patternlist = Watch_list
                elif pick=="Chocolate Brands":
                        a= Choco_list[random.randint(0,len(Choco_list)-1)]
                        temp_patternlist =Choco_list

                                 
                return a, temp_patternlist

            comp_pattern = pattern()
            # print(comp_pattern)
            chosen_word = method(comp_pattern)[0]
            print(chosen_word)
            pattern_list = method(comp_pattern)[1]
            # print(pattern_list)


            label_x = 80
            label_y = 100

            computer_choice = tk.Label(root2, text=(f"I'll bring {chosen_word} to the table!"),font=('cambria', 10))
            canvas2.create_window((canvas_width/2),label_y, window=computer_choice)

            label_playername = tk.Label(root2, text=(f"{Players[0]}, Your Turn!:"),font=('cambria', 10))
            canvas2.create_window(label_x,label_y+50, window=label_playername)

            #Text Box to enter the answers
            player_choice = tk.Entry(root2)
            canvas2.create_window((label_x+150),label_y+50,window=player_choice)

            button5 = tk.Button(root2, text='Quit', command=end_game, bg='brown', fg='white', font=('cambria', 9, 'bold'))
            canvas2.create_window((canvas_width/2), (one_firsty + 220), window=button5)

            answer1 = tk.Message(root2, text="What do you want to bring?", relief=RAISED)
            canvas2.create_window((canvas_width/2), (one_firsty + 140), window=answer1)

            # def Goto(linenum):
            #     global line
            #     line = linenum


            def check_answer():

                #Defining all required messages
                # message1 = StringVar()



                i = Players[PlayerChange[0]]

                
                if len(Guesses)!=(2*len(Players)):
                    ans = str(player_choice.get())
                    word = ans[0].upper() + ans[1:].lower().strip()
                    All_answers.append(word)
                    # print(word)                      
                    if word in pattern_list:
                        # if All_answers.count(word) > 1:
                        #     answer1.destroy()
                        #     message1 = StringVar()
                        #     answer1 = tk.Message(root2, textvariable=message1, relief=RAISED)
                        #     message1.set(f"Sorry {word} was already brought to the table")
                        #     canvas2.create_window((canvas_width/2), (one_firsty + 140), window=answer1)
                        #     player_choice.delete(0, tk.END)
                        #     Goto(306)
                        # message1 = StringVar()
                        # answer1 = tk.Message(root2, textvariable=message1, relief=RAISED)

                        answer1.configure(text="")
                        answer1.configure(text=f"Yes, you can bring {word}")
                        if i not in Guesses:
                            Guesses.append(i)
                            if i in Incorrect:
                                Incorrect.remove(i)

                        else:
                            if word in pattern_list:
                                answer1.configure(text="")
                                answer1.configure(text=f"Yes, you can bring {word}")                                
                                if i in Incorrect:
                                    Incorrect.remove(i)
                                if Guesses.count(i) ==1:
                                    Guesses.append(i)
                            else:
                                for name in Guesses:
                                    if name == i:
                                        Guesses.remove(i)
                                    Incorrect.append(i)
                                    answer1.configure(text="")
                                    answer1.configure(text=f"No, you cannot bring {word}")                                    
                                    

                        player_choice.delete(0, tk.END)
                    else:
                        player_choice.delete(0, tk.END)
                        Incorrect.append(i)
                        if i in Guesses:
                            for person in Guesses:
                                if person == i:
                                    Guesses.remove(i)
                        answer1.configure(text="")
                        answer1.configure(text=f"No, you cannot bring {word}")
                        

                else:
                    button4.destroy()
                    label_playername.destroy()
                    player_choice.destroy()
                    answer1.configure(text="")
                    answer1.configure(text=f"Well done! The pattern was {comp_pattern}")
                    

                #Alternate between players

                if PlayerChange[0] != (len(Players)-1):
                    check_number = PlayerChange[0] + 1
                    PlayerChange.pop()
                    PlayerChange.append(check_number)

                    label_playername.configure(text=(f"{Players[PlayerChange[0]]}, Your Turn!:"),font=('cambria', 10))
                else:
                    check_number = 0
                    PlayerChange.pop()
                    PlayerChange.append(check_number)
                    label_playername.configure(text=(f"{Players[PlayerChange[0]]}, Your Turn!:"),font=('cambria', 10))
                    

                #Break the loop once everyone has got it correct twice

                if len(Guesses) == (2*len(Players)):

                    label_playername.destroy()
                    player_choice.destroy()
                    answer1.configure(text="")
                    answer1.configure(text=f"Well done! The pattern was {comp_pattern}")

                    button4.destroy()
                    button_restart = tk.Button(root2, text='Play Again', command=restart, bg='brown', fg='white', font=('cambria', 9, 'bold'))
                    canvas2.create_window((canvas_width-300), (one_firsty + 220), window=button_restart)

                    button_reset = tk.Button(root2, text='Main Menu',command=reset, bg='brown', fg='white', font=('cambria', 9, 'bold'))
                    canvas2.create_window((canvas_width-100), (one_firsty + 220), window=button_reset)

            def restart():
                Guesses.clear()
                Incorrect.clear()
                play_game()
               
          

            button4 = tk.Button(root2, text='Check Answer', command=check_answer, bg='brown', fg='white', font=('cambria', 9, 'bold'))
            canvas2.create_window((canvas_width-300), (one_firsty + 220), window=button4)


        #function to create player list

        def update_players():

            num = int(entry1.get())

            if numbers[0] == num:
                player_name = entry_create.get()
                Players.append(player_name)
                #closewidgets(button2)
                
                button3 = tk.Button(root, text='Play', command=play_game, bg='brown', fg='white', font=('cambria', 9, 'bold'))
                canvas1.create_window((canvas_width/2), (one_firsty + 220), window=button3)

            else:
                player_name = entry_create.get()

                if len(player_name) != 0:

                    third_label.destroy()

                    no_playername.destroy()
                    temp_number = numbers[0]

                    update_number = temp_number + 1

                    

                    update_text = "Enter Player" + str(update_number) + " Name:"

                    label_create = tk.Label(root, text=update_text,font=('cambria', 10))
                    canvas1.create_window(one_firstx, one_firsty + 80, window=label_create)

                    numbers.pop()
                    numbers.append(update_number)

                    # print(numbers)
                    
                    Players.append(player_name)
                    entry_create.delete(0, tk.END)

                else:
                    canvas1.create_window((canvas_width/2), (one_firsty + 300), window=no_playername)

        def game_start():
            a = 1

        #Function for Next Button in Window 1

        def intro():
            num = int(entry1.get())
            
            canvas1.create_window(one_firstx, one_firsty + 80, window=third_label)

            
            canvas1.create_window((one_firstx+150),one_firsty + 80,window=entry_create)
            button1.destroy()

            button2 = tk.Button(root, text='Update', command=update_players, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window((canvas_width/2), (one_firsty + 165), window=button2)

        button1 = tk.Button(root,text='Next', command=intro, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window((canvas_width/2), one_firsty + 125, window=button1)

        root.mainloop()
    pygame.display.update()
    redrawGameWindow()

pygame.quit()




