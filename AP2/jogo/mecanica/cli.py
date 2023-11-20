import random
from jogo.ativos import itens, mapa, tesouro
from jogo.Personagens import Player, Monstros

def interagir_item(p, mochila):
    mochila.append(mochila)
    
    
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """
    pass

def movimentar(p1, move, mochila):
    random.choice([True , False])
    if move:
        acao = random.choices(["nada", "item", "monstro"], weights=[0.40, 0.20, 0.40])[0]
        if acao == "nada":
            print(f"{p1}, andou dentro da caverna e não encoutrou nada")
        elif acao == "item":
                roll1 = random.choices(itens.pocoes["Poção de Vida 1", "Poção de Vida 2", "Poção de força 1", "Poção de força 2 ", "Poção de defesa"], weights=[0.50, 0.30, 0.10, 0.05, 0.05])[0]
                potion = roll1
                print(f"Parabéns, o nosso herói achou uma {roll1}")
                mochila.append(potion)
                mochila = []
        elif acao == "monstro":
            print("O nosso herói encontrou um monstro")
            return #combate
    return True
    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """


def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = Player.p1(nome)
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.map(p1, tes)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(p1, op):
                mapa.map(p1, tes)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break