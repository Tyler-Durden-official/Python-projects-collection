from os import system, name 
from time import sleep 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

print('Welcome to Guess the word!!\n')

print('RULES:\n')

print('1.There will be two teams - one team will enter the secret_words and the other team will guess')

print('2. You should either guess a letter at a time or the entire correct sentence at a time\n')

print('3. The answer is most likely a noun and it may include spaces\n')

print('4. For checking spaces just type a space and hit enter since a space is counted as a charecter in python3\n')

print('Enter No. of lives to be given:')

lives=int(input())

print('Enter the secret_words: (with spaces)')
words= list(map(str, input().strip().split()))
sleep(1)
clear()
from random import choice
secret_word=choice(words)
k=len(secret_word)
clue=[]
i=0
while i<k:
    clue.append('?')
    i+=1
heart_symbol = u'\u2764'+' '

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    i=0
    global k
    while(i<len(secret_word)):
        if guessed_letter.lower() == secret_word[i].lower():
            clue[i] = guessed_letter.lower()
            k=k-1
            """print(k)"""
        i+=1


while lives>0:
    print(clue)
    print('Lives left: '+heart_symbol*lives)
    guess = input('Guess a letter or the whole word:')
    
    if guess.lower() == secret_word.lower():
        guessed_word_correctly = True
        break

    if guess.lower() in secret_word.lower():
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives-=1
        
    if k==0:
        guessed_word_correctly = True
        break
    
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
    



