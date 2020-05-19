import random
import re
from os import system, name
from time import sleep


def l1():
	print("________")
	print("|      |")
	print("|     \o/")
	print("|      |")
	print("|     / \\")
	print("|      ")
def l2():
	print("________")
	print("|      |")
	print("|     \o/")
	print("|      |")
	print("|      ")
	print("|      ")
def l3():
	print("________")
	print("|      |")
	print("|     \o/")
	print("|      ")
	print("|      ")
	print("|      ")
def l4():
	print("________")
	print("|      |")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
def l5():
	print("________")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
def l6():
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")

#Game Setup
print("Welcome to Hangman Game")
print("Choose Level")
print("\t1- Beginner Level(10 Lives)")
print("\t2- Intermediate Level(8 Lives)")
print("\t3- Expert Level(6 Lives)")
print("\t4- Advance Level(4 Lives)")
print("\t5- Insane Level(2 Lives)")
print("Please Choose Difficulty Level by typing it's Number::")

#taking Input For Difficulty Level
lev=input()

#taking word file as a word list
word_list=open("word.txt").read().splitlines()

#Display About user Choice
if(str(lev)=="1"):
	no_of_lives=10
	print("\nYou have choosen %s and will receive %d lives." %("Beginner",no_of_lives))
elif(str(lev)=="2"):
	no_of_lives=8
	print("\nYou have choosen %s and will receive %d lives." %("Intermediate",no_of_lives))
elif(str(lev)=="3"):
	no_of_lives=6
	print("\nYou have choosen %s and will receive %d lives." %("Advance",no_of_lives))
elif(str(lev)=="4"):
	no_of_lives=4
	print("\nYou have choosen %s and will receive %d lives." %("Expert",no_of_lives))
elif(str(lev)=="5"):
	no_of_lives=2
	print("\nYou have choosen %s and will receive %d lives." %("Insane",no_of_lives))
else:
	no_of_lives=10
	print("\nYou have choosen invalid selection and will receive %d lives by default." %no_of_lives)

#pick a random word from the list
random_num=random.randint(0,len(word_list)-1)
word_choosen=word_list[random_num]

#encode the word
encoded_word=re.sub('[0-9a-zA-Z]','*',word_choosen)

#define function for handling guesses
def guess(letter,word,encoded):
	#does the letter exist in the word
	found=False
	if letter in word:
		found=True
		#replace the Astricks with letter
		for i in range(0,len(word)):
			if word[i]==letter:
				encoded=encoded[0:i] + letter + encoded[i+1:len(encoded)]
	return(found,encoded)

#define a function to Initiate the game and prompt the user for their first selection
def initiate():
	sleep(1)
	system('cls')
	print("\nTime to guess a letter you have %d lives remaining." %no_of_lives)
	print(encoded_word,"\n")
	#level animation
	if(no_of_lives==10 or no_of_lives==9):
		l6()
	elif(no_of_lives==8 or no_of_lives==7):
		l5()
	elif(no_of_lives==6 or no_of_lives==5):
		l4()
	elif(no_of_lives==4 or no_of_lives==3):
		l3()
	elif(no_of_lives==2 or no_of_lives==1):
		l2()
	else:
		l1()
		print("\n Sorry! You are no more")
		
while(no_of_lives>0):
	initiate()
	guessed_letter=input("Your guess: ")[:1]
	
	letter_found,encoded_word = guess(guessed_letter,word_choosen,encoded_word)

	if not letter_found:
		no_of_lives-=1
		if no_of_lives == 0:
			print("\nGame over, you lost! :(The word or phrase was '%s')" %word_choosen)
			#break
		else:
			print("\nwhoops! that letter was not found. You have %d lives remaining."%no_of_lives)
			print(encoded_word)
	else:
		if '*' not in encoded_word:
			print("\nHooray! You won with %d lives remaining. The word or phrase was '%s'"%(no_of_lives,word_choosen))
			#break
		else:
			print("\n Great Job! That letter was found. You still have %d lives remaining."%no_of_lives)	
			print(encoded_word)
sleep(3)





