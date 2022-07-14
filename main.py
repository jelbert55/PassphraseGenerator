import random, colorama, math, sys, time, csv
from colorama import Fore, Back

colorama.init(autoreset=True) # reset style after every print statement

# Set external files which contain wordlists
Nou = 'nouns.txt'
Adj = 'adjectives.txt'
Ver = 'verbs.txt'
Adv = 'adverbs.txt'
Art = 'articles.txt'
Prp = 'prepositions.txt'
Ppn = 'propernouns.txt'
Prn = 'pronouns.txt'
Det = 'determiners.txt'

# Possible sentence structures for each passphrase length. Add potential structures to this list in the form you see.
structures_3 = ['AdjNouVer','NouVerAdv','VerNouAdj']
structures_4 = ['AdjAdjNouVer','NouVerAdjNou','AdjNouVerNou']
structures_5 = ['NouVerAdjAdjNou','AdjNouVerAdjNou']
structures_6 = ['AdjAdjNouVerAdvNou']

########################################
# Tense Information - see link for examples and descriptions
# https://englishstudyhere.com/tenses/12-types-of-tenses-with-examples-pdf/
# We may not want to use all of these, but here they are in a list

# Opted to be simple and use present, preterite, future, and continous tenses, 
# these match the conjugator conjugator.reverso.net
# present, preterite, and continous are in the Ver.csv, future simply needs "will" concatenated behind it
########################################
# List of possible verb tenses
#tenses = ['Simple Present','Present Progressive','Simple Past','Past Progressive','Present Perfect','Present Perfect Progressive','Past Perfect','Past Perfect Progressive','Future Will','Future Going To','Future Progressive','Future Perfect']
tenses = ['Present', 'Preterite', 'Future', 'Continous']

# Charset for fancy printing
charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

# Funtion to calculate entropy
def calculate_entropy(r,l):
  entropy = l * math.log(r,2)
  return entropy

# Function to print fancily, sort of like the matrix. Just for fun.
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
    roll = str(random.randint(0,9)) #simulate rolling a 10 sided dice
    all_rolls += roll
    
  return all_rolls

# Takes the part of speech 3 char block, creates an index, and grabs the correct part of speech from the associated wordlist
def grab_POS(POS,num_rolls,roll_count):
  index = int(roll_dice(num_rolls)) #roll the dice to get the word index
  print('Word index ' + str(roll_count) + ': ', end='')                   #base index is now an int, use index_str if needed
  index_str = str(index)
  for char in index_str: # display ints one at a time for coolness
    sys.stdout.write(Fore.GREEN + Back.BLACK + char)
    time.sleep(0.25)
  print()

  file_name = POS + ".csv" #changed to only csv file reading

  '''
  if POS == "Nou":
    file_name = "Nou.csv"
  else:
    file_name = POS + ".txt"
  '''

  file_length = 0
  with open(file_name) as f:
      file_length = sum(1 for row in f)  #stores the length of the csv file

  with open(file_name,'r') as csv_file:
    csv_reader = csv.reader(csv_file) #initialize the reader object
    
    if file_length < index:         
      index = int(index) % file_length #if index is out of range mod it to put it back in range.

    word = ""
    for i,line in enumerate(csv_reader):
      if i == index:
        word = line[0]
        # Use the below print statement to check the index and the word from the list
        #print('TEST ' + file_name + ': ' + str(i)) # I CANNOT FIGURE OUT HOW TO ACCESS LINE 1. I = 0 PRINTS LINE 2 FOR SOME REASON. SET INDEX TO 0 TO SEE WHAT I MEAN
        #word = line[0]
    word = word.strip() + " "
  return word,file_length

# Generates passphrase and entropy.
def generate_pp(pp_length):
  
  passphrase = ''
  entropy_list = []
  
  # Pick a random sentence structure given number of words in the desired passphrase. Also, calculate the entropy for the given sentence structure list.
  if pp_length == '3':
    structure_list = structures_3
  elif pp_length == '4':
    structure_list = structures_4
  elif pp_length == '5':
    structure_list = structures_5
  elif pp_length == '6':
    structure_list = structures_6

  temp_struct = random.choice(structure_list)
  print("tempstruct",temp_struct)
  struct_entropy = calculate_entropy(len(structure_list),1)

  # Add the entropy from the random sentence structure choice
  entropy_list.append(struct_entropy)

  # Loop that separates sentence structure string into 3 char blocks which represent parts of speech
  sentence_parts = [temp_struct[i:i+3] for i in range(0,len(temp_struct),3)]

  roll_count = 1
  
  # Get desired number of rolls
  number_of_rolls = int()
  while number_of_rolls not in [3,4,5,6]:
    number_of_rolls = int(input('How many 10 sided "dice" would you like to roll? (3-6) '))

  # For loop that takes a part of speech and finds the relevant random word
  for part_of_speech in sentence_parts:

    # Will call each function needed and concat the passphrase generated
    word,file_length = grab_POS(part_of_speech,number_of_rolls,roll_count)

    passphrase += word

    entropy = math.log(file_length)/math.log(2) #calculate the entropy for the word
    entropy_list.append(entropy)
    roll_count+=1
  
  #sum entropies for each word in the passphrase
  total_entropy = sum(entropy_list)
  
  return passphrase, total_entropy

# While loop to run all of the code and above functions
while True:
  # Allow user to pick passphrase length
  print('How many words between 3 and 6 would you like in your passphrase? Leave blank to select the default value of 6, or type "Exit" to quit. ')
  length = input()
  if not length:
    length = '6'

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