##BAZI HATS BEZAN --------------------------
import os
os.system('clear')
from random import randint
from colorama import init
from termcolor import colored
init()
##-------------------------------List For Words----------------------------------
Words_list = ("Apple","Banana","Orange","Kiwi","Cucumber","Watermelon","Pear","Cherry"
,"Strawberry","Nectarine","Mango","Blueberry","Pomegranate","Pineapple","Lemon","Grapefruit","Melon","Coconut"
,"Peach","Avocado","Corn","Mushroom","Tomato","Carrot","Pumpkin")
##--------------------------------Start Code Game -------------------------------
print( colored("Welcome to the word Guessing game", 'blue'))
##--------------------------------------------------Step to Game -----------------
step = int(input("Please enter an step or level:"))
##--------------------------------------------------Word Specifications -----------------
print(colored("The words of the game are from fruits and vegetables",'green'))
print(colored('''This "*" form replaces the deleted professional''', 'red','on_white'))
Answer = 0
while step < 2:
    print(colored( "Please enter Number upper 1 ",'red','on_white'))
    step = int(input("Please enter an step or level:"))
for j in range(0,step):
    print(colored("The Level :",'blue'),colored(str(j+1),'red'))
    rand_text = randint(0,(len(Words_list)-1))
    text = Words_list[rand_text]
    A_text = text
    ln=len(text)
    if (ln >=3) : 
        for i in range (ln//2):
            rand_index = randint(0,ln-1)
            text = text.replace(text[rand_index], "*", i)
        print(text)
        print (colored("Please Guess the Word",'green'))
        print(colored("Please Guess",'blue','on_white'))
        word = input("Type Word:")
        word = word.lower()
        word=word.replace(word[0],word[0].upper(),1)
        cunt=1
        while cunt<=3:
            if (word == A_text) :
                cunt = 3
                print(colored("Very Goooood",'cyan'))
                Answer +=1
                break
            elif (word != A_text) :
                print(colored("Try Guess",'red','on_white'))
                word = input("Type Word:")
                word = word.lower()
                word=word.replace(word[0],word[0].upper(),1)
                cunt+=1
print (colored("End of The Game",'magenta'))
print(colored('You were able to answer','white'),colored(Answer,'red'),colored('of ' + str(step) +' questions','white'))