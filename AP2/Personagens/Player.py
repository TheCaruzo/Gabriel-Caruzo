import random

def p1():
    global hp
    hp = random.randint(100, 120)
    status = { "fo" : random.randint(10, 18),
                "de": random.randint(10, 18)
                }
    print(f"O seu HP é {hp}.")
    print(f"O a sua força é {status["fo"]} e a sua defesa é {status["de"]}")


inicio = [0, 0]

def movimentação(move):
    if move.lower() == "w":
        if inicio[1] > 0:
            inicio[1] -= 1
    elif move.lower() == "s":
        if inicio[1] < 10:
            inicio[1] += 1
    elif move.lower() == "d":
        if inicio[0] < 10:
            inicio[0] += 1
    elif move.lower() == "a":
        if inicio[0] > 0:
            inicio[0] -= 1

if __name__ == "__main__":
    print(inicio)
    movimentação("d")
    print(inicio)
    movimentação("a")
    print(inicio)
    movimentação("s")
    print(inicio)
    movimentação("w")
    print(inicio)
    
