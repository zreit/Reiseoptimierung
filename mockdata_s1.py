from random import random, randrange

random_file_name = "mockdata_s1_" + str(randrange(4000)) + ".csv" 

s1_file = open(random_file_name, "x")
csv_text = "Departure Time; Delay (mins)"

def randomizer():
    x = random()

    if(x > 0.5):
        y = randrange(11)
        return y
    else:
        y = 0
        return y

for i in range(0, 300, 1):
    row_text = "\n14:10;" + str(randomizer()) + "\n14:25;" + str(randomizer()) + "\n14:40;" + str(randomizer()) + "\n14:55;" + str(randomizer())

    csv_text = csv_text + row_text

s1_file.write(csv_text)
s1_file.close()