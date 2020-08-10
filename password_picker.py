import random
import string
print('Welcome to password picker!!')
print('Enter some Adjectives that you have in mind (With spaces): ')
Adjectives = list(map(str,input().strip().split()))
print('Enter some nouns that you have in mind (With spaces): ')
nouns = list(map(str,input().strip().split()))
print('Enter some numbers that you have in mind (With spaces): ')
numbers =list(map(int,input().strip().split()))
while True:
    adjective = random.choice(Adjectives)
    
    noun= random.choice(nouns)
    
    numb1= random.choice(numbers)
    
    numb2=random.randrange(0,100)
    
    special_char = random.choice(string.punctuation)


    password = adjective+noun +str(numb1)+special_char+str(numb2)

    print('Password generated is: %s'%password)
    

    response=input('would you like another password?(y/n)?')
    if(response is 'n'):
        break
    if response is not 'y':
    	break