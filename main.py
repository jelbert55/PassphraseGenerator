import random, colorama, math, sys, time
from colorama import Fore, Back

colorama.init(autoreset=True) # reset style after every print statement

# Set external files which contain wordlists
nouns = 'nouns.txt'
adjectives = 'adjectives.txt'
verbs = 'verbs.txt'
adverbs = 'adverbs.txt'
articles = 'articles.txt'
prepositions = 'prepositions.txt'
propernouns = 'propernouns.txt'
pronouns = 'pronouns.txt'

# Possible sentence structures for each passphrase length. Add potential structures to this list in the form you see.
structures_3 = ['AdjNouVer','NouVerAdv','VerNouAdj']
structures_4 = ['AdjAdjNouVer','NouVerAdjNou','AdjNouVerNou']
structures_5 = ['NouVerAdjAdjNou','AdjNouVerAdjNou']
structures_6 = ['AdjAdjNouVerAdvNou']

charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def fancy_print(str):
  for letter in str:
    for i in range(5):
      print(random.choice(charset),end='\b')
      time.sleep(.02)
    print(letter, end='')
  print()

# Generate random number to pick word from wordlists. Simulates user specified number of dicerolls.
def roll_dice(number_of_rolls):
  all_rolls =  ''
  
  for i in range(number_of_rolls): 
    roll = str(random.randint(1,6)) #simulate rolling a dice
    all_rolls += roll
    
  return all_rolls

# Read from files, return corresponding word
def read_file(file_name,index):
  with open(file_name,'r') as file:
    file_length = len(file.readlines())
    file.seek(0) #put the scanner/cursor thing back at the beginning of the file. 
    if file_length < int(index):         
      index = str(int(index) % file_length) #if index is out of range mod it to put it back in range.
    for i, line in enumerate(file):
      if i == int(index):
        file.seek(0)
        
        # Use the below print statement to check the index and the word from the list
        #print('TEST ' + file_name + ': ' + str(i)) # I CANNOT FIGURE OUT HOW TO ACCESS LINE 1. I = 0 PRINTS LINE 2 FOR SOME REASON. SET INDEX TO 0 TO SEE WHAT I MEAN
        word = file.readlines()[i-1].strip() + ' '
        return word,file_length






        

# Generates passphrase and entropy.
def generate_pp(pp_length):
  
  passphrase = ''
  entropy_list = []
  
  # Pick a random sentence structure given number of words in the desired passphrase. Also, calculate the entropy for the given sentence structure list.
  if pp_length == '3':
    temp_struct = random.choice(structures_3)
    struct_entropy = math.log(len(structures_3))/math.log(2)
  if pp_length == '4':
    temp_struct = random.choice(structures_4)
    struct_entropy = math.log(len(structures_4))/math.log(2)
  if pp_length == '5':
    temp_struct = random.choice(structures_5)
    struct_entropy = math.log(len(structures_5))/math.log(2)
  if pp_length == '6':
    temp_struct = random.choice(structures_6)
    struct_entropy = math.log(len(structures_6))/math.log(2)

  # Add the entropy from the random sentence structure choice
  entropy_list.append(struct_entropy)

  # Loop that separates sentence structure string into 3 char blocks which represent parts of speech
  sentence_parts = [temp_struct[i:i+3] for i in range(0,len(temp_struct),3)]

  roll_count = 1
  number_of_rolls = int()

  # For loop that takes a part of speech and finds the relevant random word
  for part_of_speech in sentence_parts:

  # Will call each function needed and concat the passphrase generated
    
  #For sake of demo, no changes. Later, we can make this its own function and have functions that find the word we want from the given part of speech list, honestly we could probaly make that a single function that takes in a parameter called something like desiredWordType and that will tell the function what list to search under to find the word, just a thought though. ~ Sean
 
    
################## Make this a function before adding other parts of speech #######



    # NOUNS
    if part_of_speech == 'Nou':
      while number_of_rolls not in [3,4,5,6]:
        number_of_rolls = int(input('How many "dice" would you like to roll? (3-6) '))
      index = roll_dice(number_of_rolls) #roll the dice to get the word index
      print('Word index ' + str(roll_count) + ': ', end='')
      for char in index: # display ints one at a time for coolness
        sys.stdout.write(Fore.GREEN + Back.BLACK + char)
        time.sleep(0.25)
      print()

      # Read from the nouns file
      word,file_length = read_file(nouns,index)
      passphrase += word

      entropy = math.log(file_length)/math.log(2) #calculate the entropy for the word
      entropy_list.append(entropy)
      roll_count+=1

  
    # VERBS
    elif part_of_speech == 'Ver':
      while number_of_rolls not in [3,4,5,6]:
        number_of_rolls = int(input('How many \"dice" would you like to roll? (3-6)  '))
      index = roll_dice(number_of_rolls) #roll the dice to get the word index
      print('Word index ' + str(roll_count) + ': ', end='')
      for char in index:
        sys.stdout.write(Fore.GREEN + Back.BLACK + char)
        time.sleep(0.25)
      print()

      # Read from the verbs file
      word,file_length = read_file(verbs,index)
      passphrase += word
      
      entropy = math.log(file_length)/math.log(2)
      entropy_list.append(entropy)
      roll_count+=1


  
    # ADJECTIVES
    elif part_of_speech == 'Adj':
      while number_of_rolls not in [3,4,5,6]:
        number_of_rolls = int(input('How many \"dice" would you like to roll? (3-6)  '))
      index = roll_dice(number_of_rolls) #roll the dice to get the word index
      print('Word index ' + str(roll_count) + ': ', end='')
      for char in index:
        sys.stdout.write(Fore.GREEN + Back.BLACK + char)
        time.sleep(0.25)
      print()

      # Read from the adjectives file
      word,file_length = read_file(adjectives,index)
      passphrase += word
      
      entropy = math.log(file_length)/math.log(2)
      entropy_list.append(entropy)
      roll_count+=1

    # ADVERBS
    elif part_of_speech == 'Adv':
      while number_of_rolls not in [3,4,5,6]:
        number_of_rolls = int(input('How many \"dice" would you like to roll? (3-6)  '))
      index = roll_dice(number_of_rolls)
      print('Word index ' + str(roll_count) + ': ', end='')
      for char in index:
        sys.stdout.write(Fore.GREEN + Back.BLACK + char)
        time.sleep(0.25)
      print()

      # Read from the adverbs file
      word,file_length = read_file(adverbs,index)
      passphrase += word
            
      entropy = math.log(file_length)/math.log(2)
      entropy_list.append(entropy)
      roll_count+=1

 #sum entropies for each word in the passphrase
  total_entropy = sum(entropy_list)
  
  return passphrase, total_entropy


############################################################  ######
      

  

# While loop to run all of the code and above functions
while True:
  # Allow user to pick passphrase length
  print('How many words between 3 and 6 would you like in your passphrase? Or type "Exit" to quit. ')
  length = input()

  # If valid input, generate the passphrase
  if length in ['3','4','5','6']:
    passphrase, pp_entropy = generate_pp(length)

    #print the passphrase and entropy
    print('Your passphrase is:  ' + Fore.CYAN + Back.BLACK, end='')
    fancy_print(passphrase)
    print('The entropy for the given passphrase is:  ' + Fore.MAGENTA + Back.BLACK + '{:.4f}'.format(pp_entropy) + '\n')

  # If user wants to exit
  elif length.lower() == "exit":
    break
    
  # If invalid user input
  else:
    print('Please enter a number in the specified range, or type "Exit" to quit ')