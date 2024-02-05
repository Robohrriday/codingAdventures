''' s-w -> s wins
    w-g -> w wins
    g-s -> g wins
'''
rounds = int(input("********** Welcome to Snake, Water or Gun Game **********\nEnter the number of round(s) to be played: "))

def start():
    e = input("\nComputer's turn:\nPlayer Turn: Snake(s), Water(w) or Gun(g): ")
    return e

import random

def rand():
    f = random.randint(1,3)
    if f == 1:
        f = "s"
        return f
    elif f == 2:
        f = "w"
        return f
    elif f == 3:
        f = "g"
        return f

comp_wins = []
p_wins = []

''' a = comp
    b = p
    c = comp_wins
    d = p_wins
'''

def compare(a,b,c,d):
    if a == "s" and b == "w":
        print(f"Computer chose {a} and player chose {b}.")
        print("Computer wins this round.")
        c.append("x")
    elif a == "w" and b == "s":
        print(f"Computer chose {a} and player chose {b}.")
        print("Player wins this round.")
        d.append("x")
    elif a == "w" and b == "g":
        print(f"Computer chose {a} and player chose {b}.")
        print("Computer wins this round.")
        c.append("x")
    elif a == "g" and b == "w":
        print(f"Computer chose {a} and player chose {b}.")
        print("Player wins this round.")
        d.append("x")
    elif a == "g" and b == "s":
        print(f"Computer chose {a} and player chose {b}.")
        print("Computer wins this round.")
        c.append("x")
    elif a == "s" and b == "g":
        print(f"Computer chose {a} and player chose {b}.")
        print("Player wins this round.")
        d.append("x")
    elif a == "s" and b == "s":
        print(f"Computer chose {a} and player chose {b}.")
        print("Nobody wins this round.")
    elif a == "w" and b == "w":
        print(f"Computer chose {a} and player chose {b}.")
        print("Nobody wins this round.")
    elif a == "g" and b == "g":
        print(f"Computer chose {a} and player chose {b}.")
        print("Nobody wins this round.")
    else:
        pass

for i in range(0,rounds):
    p = start()
    comp = rand()
    compare(comp,p,comp_wins,p_wins)

if len(comp_wins)>len(p_wins):
    print(f'''\nFinal result:\nComputer won {len(comp_wins)} round(s) and Player won {len(p_wins)} round(s).\nComputer wins.''')
elif len(p_wins)>len(comp_wins):
    print(f'''\nFinal result:\nComputer won {len(comp_wins)} round(s) and Player won {len(p_wins)} round(s).\nPlayer wins.''')
elif len(comp_wins)==len(p_wins):
    print(f'''\nFinal result:\nComputer won {len(comp_wins)} round(s) and Player won {len(p_wins)} round(s).\nIts a draw.''')
else:
    pass
