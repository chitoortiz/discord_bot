import random

Person1 = Name1
Person2 = Name2
Person3 = Name3
Person4 = Name4
Person5 = Name5
Person6 = Name6
Person7 = Name7
Person8 = Name8

players = [Name1, Name2, Name3, Name4, Name5, Name6, Name7, Name8]

while Person1 == Name1:
    Person1 = random.choice(players)
    
players.remove(Person1)
print("Player1: " + Person1)

while Person2 == Name2:
    Person2 = random.choice(players)

players.remove(Person2)
print("Player2: " + Person2)

while Person3 == Name3:
    Person3 = random.choice(players)

players.remove(Person3)
print("Player3: " + Person3)
