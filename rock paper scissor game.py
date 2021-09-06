import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False

    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False

    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False



print("Welcome to rock paper and scissor game")
print("comp turn:rock(r) paper(p) scissor(s)?")
randno = random.randint(1,3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
elif randno == 3:
    comp = "s"

you = input("your turn:rock(r) paper(p) scissor(s)?")
a = gamewin(comp,you)
print(f"computer choose :{comp}")
print(f"you choose :{you}")

if a is None:
    print("tie")
elif a is True:
    print("you win")
elif a is False:
    print("you lose")