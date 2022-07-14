# Rename file to main.py to use. Probably an easier way but whatever.

# For experimentation on csv reading.

import random, csv

def read():
    with open('Nou.csv') as f:
      lines = sum(1 for row in f)

    with open('Nou.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        index = random.randint(0, lines)
        print('index:',index)

        for i,line in enumerate(csv_reader):
            if i == index:
                return line[0]

pp = read() + ' ' + read() + ' ' + read()

print('pp:',pp)

'''
def grab_POS(POS,num_rolls,roll_count):
  index = roll_dice(num_rolls) #roll the dice to get the word index
  print('Word index ' + str(roll_count) + ': ', end='')
  for char in index: # display ints one at a time for coolness
    sys.stdout.write(Fore.GREEN + Back.BLACK + char)
    time.sleep(0.25)
  print()

  file_name = POS + ".csv"

  if POS == "Nou":
    file_name = "Nou.csv"   remove
  else:
    file_name = POS + ".txt"

  with open(file_name,'r') as csv:
    file_length = len(file.readlines())
    file.seek(0) #put the scanner/cursor thing back at the beginning of the file. 
    if file_length < int(index):         
      index = str(int(index) % file_length) #if index is out of range mod it to put it back in range.
    for i, line in enumerate(file):
      if i == int(index):
        file.seek(0)
        # Use the below print statement to check the index and the word from the list
        #print('TEST ' + file_name + ': ' + str(i)) # I CANNOT FIGURE OUT HOW TO ACCESS LINE 1. I = 0 PRINTS LINE 2 FOR SOME REASON. SET INDEX TO 0 TO SEE WHAT I MEAN
        #word = line[0]
        word = file.readlines()[i-1].strip() + ' '

  return word,file_length
'''