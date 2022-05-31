# Rename file to main.py to use. Probably an easier way but whatever.

# For experimentation on csv reading.

import random, csv

def read():
    with open('Nou.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        index = random.randint(0,1000)
        print('index:',index)

        for i,line in enumerate(csv_reader):
            if i == index:
                return line[0]

pp = read() + ' ' + read() + ' ' + read()

print('pp:',pp)
