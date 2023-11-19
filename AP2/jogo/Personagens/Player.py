import random

posicao = [0, 0]
def p1():
    global hp
    hp = random.randint(100, 120)
    status = { "fo" : random.randint(10, 18),
                "de": random.randint(10, 18)
                }
    print(f"O seu HP é {hp}.")
    print(f"O a sua força é {status["fo"]} e a sua defesa é {status["de"]}")



def movimentação(move):
    if move.lower() == "w":
        if posicao[1] > 0:
            posicao[1] -= 1
    elif move.lower() == "s":
        if posicao[1] < 9:
            posicao[1] += 1
    elif move.lower() == "d":
        if posicao[0] < 9:
            posicao[0] += 1
    elif move.lower() == "a":
        if posicao[0] > 0:
            posicao[0] -= 1

if __name__ == "__main__":
    p1()
    print(posicao)
    movimentação("d")
    print(posicao)
    movimentação("a")
    print(posicao)
    movimentação("s")
    print(posicao)
    movimentação("w")
    print(posicao)
    
