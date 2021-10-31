import random

Nacho = "Nacho"
Sofía = "Sofía"
Alberto = "Alberto"
Andreu = "Andreu"
Jens = "Jens"
Luisa = "Luisa"
Queku = "Queku"
Susana = "Susana"

players = ["Nacho", "Sofía", "Alberto", "Andreu", "Jens", "Luisa", "Queku", "Susana"]

while Nacho == "Nacho":
    Nacho = random.choice(players)
    
players.remove(Nacho)
print("Nacho: " + Nacho)

while Sofía == "Sofía":
    Sofía = random.choice(players)

players.remove(Sofía)
print("Sofía: " + Sofía)

while Alberto == "Alberto":
    Alberto = random.choice(players)

players.remove(Alberto)
print("Alberto: " + Alberto)

while Andreu == "Andreu":
    Andreu = random.choice(players)

players.remove(Andreu)
print("Andreu: " + Andreu)

while Jens == "Jens":
    Jens = random.choice(players)

players.remove(Jens)
print("Jens: " + Jens)

while Luisa == "Luisa":
    Luisa = random.choice(players)

players.remove(Luisa)
print("Luisa: " + Luisa)

while Queku == "Queku":
    Queku = random.choice(players)

players.remove(Queku)
print("Queku: " + Queku)

while Susana == "Susana":
    Susana = random.choice(players)

players.remove(Susana)
print("Susana: " + Susana)
